"""
JSON Formatter/Validator Tool
Cleans, validates, and prettifies JSON data
"""

import json
from mcp.server import Server


def register_tool(server: Server):
    """Register JSON formatter tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "json_formatter",
            "description": "Format and validate JSON with pretty printing, optional key sorting",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "json_string": {
                        "type": "string",
                        "description": "Raw JSON string to format"
                    },
                    "indent": {
                        "type": "integer",
                        "description": "Indentation spaces",
                        "default": 2,
                        "minimum": 0
                    },
                    "sort_keys": {
                        "type": "boolean",
                        "description": "Sort dictionary keys alphabetically",
                        "default": False
                    }
                },
                "required": ["json_string"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "json_formatter":
            try:
                json_string = arguments["json_string"]
                indent = arguments.get("indent", 2)
                sort_keys = arguments.get("sort_keys", False)
                
                # Parse JSON
                data = json.loads(json_string)
                
                # Format with options
                formatted = json.dumps(
                    data,
                    indent=indent if indent > 0 else None,
                    sort_keys=sort_keys,
                    ensure_ascii=False
                )
                
                # Count elements for summary
                if isinstance(data, dict):
                    item_count = f"{len(data)} keys"
                elif isinstance(data, list):
                    item_count = f"{len(data)} items"
                else:
                    item_count = "scalar value"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"""✅ Valid JSON ({item_count})

```json
{formatted}
```"""
                    }]
                }
            
            except json.JSONDecodeError as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"""❌ Invalid JSON

**Error:** {e.msg}
**Location:** Line {e.lineno}, Column {e.colno}

```
{arguments['json_string']}
{' ' * (e.colno - 1)}^
```"""
                    }]
                }
            
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
