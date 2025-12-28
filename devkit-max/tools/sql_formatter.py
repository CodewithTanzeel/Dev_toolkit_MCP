"""
SQL Formatter Tool
Format and prettify SQL queries with customizable indentation
"""

import re
from mcp.server import Server


def register_tool(server: Server):
    """Register SQL formatter tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "sql_formatter",
            "description": "Format SQL queries with proper indentation and keyword casing",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "SQL query to format"
                    },
                    "dialect": {
                        "type": "string",
                        "description": "SQL dialect",
                        "enum": ["mysql", "postgresql", "sqlite", "tsql", "generic"],
                        "default": "generic"
                    },
                    "indent_width": {
                        "type": "integer",
                        "description": "Spaces per indent level",
                        "default": 2,
                        "minimum": 1,
                        "maximum": 8
                    },
                    "keyword_case": {
                        "type": "string",
                        "description": "Case for SQL keywords",
                        "enum": ["upper", "lower", "preserve"],
                        "default": "upper"
                    }
                },
                "required": ["sql"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "sql_formatter":
            try:
                sql = arguments["sql"].strip()
                dialect = arguments.get("dialect", "generic")
                indent_width = arguments.get("indent_width", 2)
                keyword_case = arguments.get("keyword_case", "upper")
                
                # SQL keywords for case conversion
                keywords = [
                    'SELECT', 'FROM', 'WHERE', 'JOIN', 'LEFT', 'RIGHT', 'INNER', 'OUTER',
                    'ON', 'AND', 'OR', 'NOT', 'IN', 'BETWEEN', 'LIKE', 'IS', 'NULL',
                    'GROUP', 'BY', 'ORDER', 'HAVING', 'LIMIT', 'OFFSET', 'INSERT', 'INTO',
                    'VALUES', 'UPDATE', 'SET', 'DELETE', 'CREATE', 'TABLE', 'DROP', 'ALTER',
                    'ADD', 'COLUMN', 'PRIMARY', 'KEY', 'FOREIGN', 'REFERENCES', 'UNION',
                    'ALL', 'DISTINCT', 'AS', 'CASE', 'WHEN', 'THEN', 'ELSE', 'END',
                    'WITH', 'RECURSIVE', 'CROSS', 'FULL', 'NATURAL', 'USING'
                ]
                
                # Apply keyword case
                formatted_sql = sql
                if keyword_case != "preserve":
                    for keyword in keywords:
                        pattern = r'\b' + re.escape(keyword) + r'\b'
                        if keyword_case == "upper":
                            formatted_sql = re.sub(pattern, keyword, formatted_sql, flags=re.IGNORECASE)
                        else:  # lower
                            formatted_sql = re.sub(pattern, keyword.lower(), formatted_sql, flags=re.IGNORECASE)
                
                # Add newlines before major clauses
                clause_patterns = [
                    (r'\bSELECT\b', '\nSELECT'),
                    (r'\bFROM\b', '\nFROM'),
                    (r'\bWHERE\b', '\nWHERE'),
                    (r'\bJOIN\b', '\nJOIN'),
                    (r'\bLEFT\s+JOIN\b', '\nLEFT JOIN'),
                    (r'\bRIGHT\s+JOIN\b', '\nRIGHT JOIN'),
                    (r'\bINNER\s+JOIN\b', '\nINNER JOIN'),
                    (r'\bGROUP\s+BY\b', '\nGROUP BY'),
                    (r'\bHAVING\b', '\nHAVING'),
                    (r'\bORDER\s+BY\b', '\nORDER BY'),
                    (r'\bLIMIT\b', '\nLIMIT'),
                    (r'\bUNION\b', '\nUNION'),
                    (r'\bUNION\s+ALL\b', '\nUNION ALL'),
                ]
                
                for pattern, replacement in clause_patterns:
                    formatted_sql = re.sub(pattern, replacement, formatted_sql, flags=re.IGNORECASE)
                
                # Handle AND/OR with indentation
                formatted_sql = re.sub(r'\s+AND\s+', '\n  AND ', formatted_sql, flags=re.IGNORECASE)
                formatted_sql = re.sub(r'\s+OR\s+', '\n  OR ', formatted_sql, flags=re.IGNORECASE)
                
                # Handle commas in SELECT
                formatted_sql = re.sub(r',\s*', ',\n  ', formatted_sql)
                
                # Clean up multiple newlines
                formatted_sql = re.sub(r'\n\s*\n', '\n', formatted_sql)
                
                # Apply indentation
                lines = formatted_sql.split('\n')
                formatted_lines = []
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Determine indentation level
                    indent_level = 0
                    if any(line.upper().startswith(kw) for kw in ['AND', 'OR']):
                        indent_level = 1
                    elif any(kw in line.upper() for kw in ['JOIN', 'WHERE', 'GROUP', 'ORDER', 'HAVING', 'LIMIT', 'UNION']):
                        indent_level = 0
                    else:
                        indent_level = 1
                    
                    formatted_lines.append((' ' * (indent_width * indent_level)) + line)
                
                result = '\n'.join(formatted_lines)
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"""✅ SQL Formatted

**Dialect:** {dialect}
**Indent:** {indent_width} spaces
**Keyword case:** {keyword_case}

```sql
{result}
```"""
                    }]
                }
            
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"""```sql
{arguments['sql']}
```

⚠️ Could not format. Error: {str(e)}"""
                    }]
                }
