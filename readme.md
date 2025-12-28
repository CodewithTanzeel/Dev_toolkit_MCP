# 🚀 DevKit Max - Complete MCP Project Guide

## 📋 Project Overview

**Project Name**: DevKit Max  
**Tagline**: Your Complete Developer Toolbox in Claude  
**Goal**: Build an MCP server with 9 essential developer utilities in 5 hours  
**Core Philosophy**: "Vibe coding" - Build useful, beautiful tools while enjoying the process

---

## 🎯 Complete Feature Specifications

### **Tool 1: JSON Formatter/Validator** (`json_formatter`)
```yaml
Purpose: Clean, validate, and prettify JSON data
Input Parameters:
  - json_string: string (required) - Raw JSON
  - indent: integer (optional, default: 2) - Indentation spaces
  - sort_keys: boolean (optional, default: false) - Sort object keys
Output: Formatted JSON with syntax highlighting or error details
Example Input: {"name":"john","data":[1,2,3]}
Example Output:
```json
{
  "name": "john",
  "data": [1, 2, 3]
}
```
```

### **Tool 2: Base64 Encoder/Decoder** (`base64_tool`)
```yaml
Purpose: Bidirectional Base64 conversion
Input Parameters:
  - operation: "encode" | "decode" (required)
  - input: string (required) - Text to encode or base64 to decode
  - url_safe: boolean (optional, default: false) - Use URL-safe encoding
  - padding: boolean (optional, default: true) - Include padding characters
Output: Converted string with operation metadata
Example: "Hello World" ↔ "SGVsbG8gV29ybGQ="
```

### **Tool 3: UUID Generator** (`uuid_generator`)
```yaml
Purpose: Generate unique identifiers
Input Parameters:
  - count: integer (optional, default: 1, range: 1-50) - Number of UUIDs
  - version: "v1" | "v4" (optional, default: "v4") - UUID version
  - hyphens: boolean (optional, default: true) - Include hyphens
Output: List of UUIDs in copy-friendly format
Example Output:
Generated 3 UUIDv4:
1. `550e8400-e29b-41d4-a716-446655440000`
2. `6ba7b810-9dad-11d1-80b4-00c04fd430c8`
3. `123e4567-e89b-12d3-a456-426614174000`
```

### **Tool 4: JWT Decoder** (`jwt_decoder`)
```yaml
Purpose: Parse and inspect JWT tokens
Input Parameters:
  - token: string (required) - JWT token
  - verify_signature: boolean (optional, default: false) - Basic format check
Output: Decoded header, payload, and metadata
Example Output:
Header:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Payload:
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "exp": 1516242622
}
```

⚠️ Token expired 2 years ago
```

### **Tool 5: Timestamp Converter** (`timestamp_tool`)
```yaml
Purpose: Convert between time formats
Input Parameters:
  - input: string | number (required) - Time input
  - input_format: "auto" | "unix" | "iso" | "rfc2822" (optional, default: "auto")
  - output_format: "all" | "unix" | "iso" | "human" (optional, default: "all")
  - timezone: string (optional, default: "UTC") - Target timezone
Output: Time in multiple formats
Example Output:
Input: 1672531200
Conversions:
• Unix: 1672531200
• ISO: 2023-01-01T00:00:00+00:00
• Human: January 1, 2023, 12:00:00 AM UTC
• Relative: 1 year ago
```

### **Tool 6: Hash Generator** (`hash_generator`)
```yaml
Purpose: Generate cryptographic hashes
Input Parameters:
  - input: string (required) - Text to hash
  - algorithm: "md5" | "sha1" | "sha256" | "sha512" (optional, default: "sha256")
  - encoding: "hex" | "base64" (optional, default: "hex")
Output: Hash value with algorithm info
Example Output:
SHA256 hash of "hello":
`2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`
```

### **Tool 7: Quick HTTP Tester** (`http_tester`)
```yaml
Purpose: Make HTTP requests from Claude
Input Parameters:
  - method: "GET" | "POST" | "PUT" | "DELETE" | "PATCH" (required)
  - url: string (required) - Full URL with protocol
  - headers: object (optional) - Request headers as JSON
  - body: string | object (optional) - Request body
  - timeout: integer (optional, default: 10) - Timeout in seconds
Output: Response with status, headers, body, and timing
Example Output:
✅ GET https://api.github.com/users/octocat (200 OK)
⏱️ 342ms

Headers:
• content-type: application/json; charset=utf-8
• x-ratelimit-remaining: 59

Body (preview):
```json
{
  "login": "octocat",
  "id": 583231
}
```
```

### **Tool 8: SQL Formatter** (`sql_formatter`)
```yaml
Purpose: Format and prettify SQL queries
Input Parameters:
  - sql: string (required) - Raw SQL query
  - dialect: "mysql" | "postgresql" | "sqlite" | "tsql" (optional, default: "mysql")
  - indent_width: integer (optional, default: 2) - Spaces per indent
  - keyword_case: "upper" | "lower" | "preserve" (optional, default: "upper")
Output: Formatted SQL with syntax highlighting
Example Output:
```sql
SELECT 
  users.id,
  users.name,
  orders.total
FROM 
  users
  JOIN orders ON users.id = orders.user_id
WHERE 
  users.active = TRUE
  AND orders.date > '2023-01-01'
ORDER BY 
  orders.total DESC
LIMIT 10;
```
```

### **Tool 9: Color Converter** (`color_converter`)
```yaml
Purpose: Convert between color formats with visual preview
Input Parameters:
  - color: string (required) - Color input
  - from_format: "auto" | "hex" | "rgb" | "hsl" | "name" (optional, default: "auto")
  - to_format: "all" | "hex" | "rgb" | "hsl" | "name" (optional, default: "all")
Output: Color in all formats with ASCII preview
Example Output:
🎨 Color: Deep Sky Blue
Preview: ████████████████████████████
• HEX: #00BFFF
• RGB: rgb(0, 191, 255)
• HSL: hsl(195°, 100%, 50%)
• CMYK: cmyk(100%, 25%, 0%, 0%)
• CSS: deepskyblue
```

---

## 🏗️ Technical Architecture

### **Project Structure**
```
devkit-max/
├── server.py              # Main MCP server entry point
├── requirements.txt       # Dependencies
├── config.yaml           # Configuration file
├── README.md            # Documentation
├── tools/               # All tool implementations
│   ├── __init__.py
│   ├── json_formatter.py
│   ├── base64_tool.py
│   ├── uuid_generator.py
│   ├── jwt_decoder.py
│   ├── timestamp_tool.py
│   ├── hash_generator.py
│   ├── http_tester.py
│   ├── sql_formatter.py
│   └── color_converter.py
├── utils/               # Shared utilities
│   ├── __init__.py
│   ├── formatters.py    # Output formatting
│   ├── validators.py    # Input validation
│   ├── errors.py        # Error handling
│   └── constants.py     # Constants and config
└── tests/               # Quick smoke tests
    └── test_quick.py
```

### **Dependencies**
```txt
mcp>=1.0.0              # MCP protocol implementation
fastapi>=0.104.0        # Web framework for MCP
python-dateutil>=2.8.2  # Time parsing
pyjwt>=2.8.0           # JWT decoding
httpx>=0.25.0          # Async HTTP client
pydantic>=2.4.0        # Data validation
colorama>=0.4.6        # Color handling (optional)
```

### **MCP Server Skeleton**
```python
# server.py
from mcp.server import Server, NotificationOptions
import mcp.server.stdio
import asyncio
from typing import List
import importlib
import os

# Initialize server
server = Server("devkit-max")

# Dynamically load all tools
def load_tools():
    tools = []
    tool_files = [f[:-3] for f in os.listdir("tools") 
                  if f.endswith(".py") and f != "__init__.py"]
    
    for tool_file in tool_files:
        try:
            module = importlib.import_module(f"tools.{tool_file}")
            if hasattr(module, "register_tool"):
                module.register_tool(server)
                tools.append(tool_file)
        except Exception as e:
            print(f"⚠️  Failed to load {tool_file}: {e}")
    
    print(f"✅ Loaded {len(tools)} tools: {', '.join(tools)}")
    return tools

@server.list_tools()
async def handle_list_tools():
    # Tools will be registered by individual modules
    return []

async def main():
    # Load all tools
    load_tools()
    
    # Run MCP server
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, NotificationOptions())

if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⏱️ 5-Hour Implementation Plan

### **Hour 1: Foundation & Setup** (0:00-1:00)

#### **15 min: Project Bootstrap**
```bash
# Create project structure
mkdir devkit-max && cd devkit-max
uv init .
echo "mcp>=1.0.0" >> requirements.txt
echo "fastapi>=0.104.0" >> requirements.txt
echo "python-dateutil>=2.8.2" >> requirements.txt
echo "pyjwt>=2.8.0" >> requirements.txt

# Create directory structure
mkdir tools utils tests
touch tools/__init__.py utils/__init__.py

# Create main server file
touch server.py
```

#### **30 min: Core Server & First Tool**
```python
# server.py - Complete with dynamic loading
# (See skeleton above)

# tools/json_formatter.py - Start with the simplest tool
import json
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "json_formatter",
            "description": "Format and validate JSON with pretty printing",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "json_string": {"type": "string", "description": "Raw JSON string"},
                    "indent": {"type": "integer", "description": "Indentation spaces", "default": 2},
                    "sort_keys": {"type": "boolean", "description": "Sort dictionary keys", "default": False}
                },
                "required": ["json_string"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "json_formatter":
            try:
                data = json.loads(arguments["json_string"])
                indent = arguments.get("indent", 2)
                sort_keys = arguments.get("sort_keys", False)
                
                formatted = json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"```json\n{formatted}\n```"
                    }]
                }
            except json.JSONDecodeError as e:
                return {
                    "content": [{
                        "type": "text", 
                        "text": f"❌ Invalid JSON: {e.msg}\nLine {e.lineno}, Column {e.colno}"
                    }]
                }
```

#### **15 min: Tool 2 & 3 - Quick Wins**
```python
# tools/uuid_generator.py
import uuid
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "uuid_generator",
            "description": "Generate UUIDs (version 1 or 4)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "count": {"type": "integer", "description": "Number of UUIDs to generate", "default": 1, "minimum": 1, "maximum": 50},
                    "version": {"type": "string", "description": "UUID version", "enum": ["v1", "v4"], "default": "v4"},
                    "hyphens": {"type": "boolean", "description": "Include hyphens in output", "default": True}
                }
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "uuid_generator":
            count = arguments.get("count", 1)
            version = arguments.get("version", "v4")
            hyphens = arguments.get("hyphens", True)
            
            uuids = []
            for _ in range(count):
                if version == "v1":
                    uid = str(uuid.uuid1())
                else:
                    uid = str(uuid.uuid4())
                
                if not hyphens:
                    uid = uid.replace("-", "")
                
                uuids.append(uid)
            
            output = "\n".join([f"{i+1}. `{uid}`" for i, uid in enumerate(uuids)])
            return {
                "content": [{
                    "type": "text",
                    "text": f"Generated {count} UUID{version}:\n{output}"
                }]
            }
```

### **Hour 2: Core Tools Implementation** (1:00-2:00)

#### **30 min: Base64 & Hash Tools**
```python
# tools/base64_tool.py
import base64
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "base64_tool",
            "description": "Encode or decode Base64 strings",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "operation": {"type": "string", "description": "Operation to perform", "enum": ["encode", "decode"], "default": "encode"},
                    "input": {"type": "string", "description": "Text to encode or Base64 to decode"},
                    "url_safe": {"type": "boolean", "description": "Use URL-safe encoding", "default": False}
                },
                "required": ["operation", "input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "base64_tool":
            operation = arguments["operation"]
            input_text = arguments["input"]
            url_safe = arguments.get("url_safe", False)
            
            try:
                if operation == "encode":
                    encoded = base64.b64encode(input_text.encode()).decode()
                    if url_safe:
                        encoded = encoded.replace('+', '-').replace('/', '_').rstrip('=')
                    result = encoded
                    action = "Encoded"
                else:  # decode
                    if url_safe:
                        input_text = input_text.replace('-', '+').replace('_', '/')
                        # Add padding if needed
                        padding = 4 - len(input_text) % 4
                        if padding != 4:
                            input_text += '=' * padding
                    decoded = base64.b64decode(input_text).decode()
                    result = decoded
                    action = "Decoded"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"{action} result:\n```\n{result}\n```"
                    }]
                }
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }

# tools/hash_generator.py
import hashlib
import base64
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "hash_generator",
            "description": "Generate cryptographic hashes (MD5, SHA1, SHA256, SHA512)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {"type": "string", "description": "Text to hash"},
                    "algorithm": {"type": "string", "description": "Hash algorithm", "enum": ["md5", "sha1", "sha256", "sha512"], "default": "sha256"},
                    "encoding": {"type": "string", "description": "Output encoding", "enum": ["hex", "base64"], "default": "hex"}
                },
                "required": ["input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "hash_generator":
            input_text = arguments["input"]
            algorithm = arguments.get("algorithm", "sha256")
            encoding = arguments.get("encoding", "hex")
            
            # Select hash algorithm
            if algorithm == "md5":
                hash_obj = hashlib.md5()
            elif algorithm == "sha1":
                hash_obj = hashlib.sha1()
            elif algorithm == "sha256":
                hash_obj = hashlib.sha256()
            else:  # sha512
                hash_obj = hashlib.sha512()
            
            # Compute hash
            hash_obj.update(input_text.encode())
            
            # Encode output
            if encoding == "hex":
                result = hash_obj.hexdigest()
            else:
                result = base64.b64encode(hash_obj.digest()).decode()
            
            return {
                "content": [{
                    "type": "text",
                    "text": f"{algorithm.upper()} hash ({encoding}):\n`{result}`"
                }]
            }
```

#### **30 min: JWT Decoder**
```python
# tools/jwt_decoder.py
import jwt
import json
from datetime import datetime
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "jwt_decoder",
            "description": "Decode and inspect JWT tokens",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "token": {"type": "string", "description": "JWT token to decode"},
                    "verify_signature": {"type": "boolean", "description": "Check token format (not cryptographic verification)", "default": False}
                },
                "required": ["token"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "jwt_decoder":
            token = arguments["token"]
            verify = arguments.get("verify_signature", False)
            
            try:
                # Decode without verification (or with simple format check)
                if verify:
                    decoded = jwt.decode(token, options={"verify_signature": False})
                else:
                    decoded = jwt.decode(token, options={"verify_signature": False})
                
                # Split token parts
                parts = token.split('.')
                if len(parts) != 3:
                    return {
                        "content": [{
                            "type": "text",
                            "text": "❌ Invalid JWT format: Expected 3 parts separated by dots"
                        }]
                    }
                
                # Decode header and payload
                import base64
                import json
                
                # Add missing padding if needed
                def decode_part(part):
                    padding = 4 - len(part) % 4
                    if padding != 4:
                        part += '=' * padding
                    return json.loads(base64.b64decode(part).decode())
                
                header = decode_part(parts[0])
                payload = decoded  # Already decoded
                
                # Build response
                response_text = "## 🔐 JWT Decoded\n\n"
                
                # Header
                response_text += "### Header\n```json\n"
                response_text += json.dumps(header, indent=2)
                response_text += "\n```\n\n"
                
                # Payload
                response_text += "### Payload\n```json\n"
                response_text += json.dumps(payload, indent=2)
                response_text += "\n```\n\n"
                
                # Check expiration
                if 'exp' in payload:
                    exp_time = datetime.fromtimestamp(payload['exp'])
                    now = datetime.now()
                    if exp_time < now:
                        response_text += f"⚠️ **Token expired** on {exp_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    else:
                        response_text += f"✅ Token valid until {exp_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                
                # Signature preview
                response_text += f"\n### Signature (preview)\n`{parts[2][:20]}...`\n"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": response_text
                    }]
                }
                
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error decoding JWT: {str(e)}"
                    }]
                }
```

### **Hour 3: Advanced Tools - Part 1** (2:00-3:00)

#### **45 min: Timestamp Converter**
```python
# tools/timestamp_tool.py
from datetime import datetime, timezone
import dateutil.parser
import time
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "timestamp_tool",
            "description": "Convert between timestamp formats (Unix, ISO, human readable)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {"type": "string", "description": "Timestamp input (Unix, ISO, or human date)"},
                    "input_format": {"type": "string", "description": "Input format", "enum": ["auto", "unix", "iso", "human"], "default": "auto"},
                    "output_format": {"type": "string", "description": "Output format", "enum": ["all", "unix", "iso", "human"], "default": "all"},
                    "timezone": {"type": "string", "description": "Target timezone (e.g., 'UTC', 'America/New_York')", "default": "UTC"}
                },
                "required": ["input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "timestamp_tool":
            input_str = arguments["input"]
            input_format = arguments.get("input_format", "auto")
            output_format = arguments.get("output_format", "all")
            tz = arguments.get("timezone", "UTC")
            
            try:
                # Parse input based on format
                dt = None
                
                if input_format == "auto":
                    # Try different formats
                    try:
                        # Try Unix timestamp (integer or float)
                        timestamp = float(input_str)
                        dt = datetime.fromtimestamp(timestamp, timezone.utc)
                    except ValueError:
                        try:
                            # Try ISO format
                            dt = dateutil.parser.isoparse(input_str)
                        except ValueError:
                            # Try human date
                            dt = dateutil.parser.parse(input_str)
                
                elif input_format == "unix":
                    timestamp = float(input_str)
                    dt = datetime.fromtimestamp(timestamp, timezone.utc)
                
                elif input_format == "iso":
                    dt = dateutil.parser.isoparse(input_str)
                
                else:  # human
                    dt = dateutil.parser.parse(input_str)
                
                # Convert to target timezone
                from dateutil import tz as tzutil
                try:
                    target_tz = tzutil.gettz(tz)
                    if target_tz:
                        dt = dt.astimezone(target_tz)
                except:
                    pass  # Keep UTC if timezone invalid
                
                # Generate outputs
                unix_timestamp = int(dt.timestamp())
                iso_format = dt.isoformat()
                human_format = dt.strftime("%B %d, %Y, %I:%M:%S %p %Z")
                
                # Relative time
                now = datetime.now(timezone.utc)
                diff = now - dt.replace(tzinfo=timezone.utc)
                seconds = diff.total_seconds()
                
                if seconds < 60:
                    relative = "just now"
                elif seconds < 3600:
                    minutes = int(seconds / 60)
                    relative = f"{minutes} minute{'s' if minutes != 1 else ''} ago"
                elif seconds < 86400:
                    hours = int(seconds / 3600)
                    relative = f"{hours} hour{'s' if hours != 1 else ''} ago"
                elif seconds < 2592000:
                    days = int(seconds / 86400)
                    relative = f"{days} day{'s' if days != 1 else ''} ago"
                else:
                    months = int(seconds / 2592000)
                    relative = f"{months} month{'s' if months != 1 else ''} ago"
                
                # Build response based on output format
                if output_format == "all":
                    response = f"""## 🕐 Timestamp Conversion

**Input:** `{input_str}`
**Parsed as:** {dt.strftime('%Y-%m-%d %H:%M:%S %Z')}

**Conversions:**
• **Unix timestamp:** `{unix_timestamp}`
• **ISO 8601:** `{iso_format}`
• **Human readable:** {human_format}
• **Relative time:** {relative}"""
                
                elif output_format == "unix":
                    response = f"Unix timestamp: `{unix_timestamp}`"
                elif output_format == "iso":
                    response = f"ISO 8601: `{iso_format}`"
                else:  # human
                    response = f"Human readable: {human_format}"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": response
                    }]
                }
                
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error parsing timestamp: {str(e)}\n\nTry formats:\n- Unix: 1672531200\n- ISO: 2023-01-01T00:00:00Z\n- Human: 'January 1, 2023'"
                    }]
                }
```

### **Hour 4: Advanced Tools - Part 2** (3:00-4:00)

#### **30 min: SQL Formatter**
```python
# tools/sql_formatter.py
import re
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "sql_formatter",
            "description": "Format SQL queries with proper indentation",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "sql": {"type": "string", "description": "SQL query to format"},
                    "dialect": {"type": "string", "description": "SQL dialect", "enum": ["mysql", "postgresql", "sqlite", "tsql", "generic"], "default": "generic"},
                    "indent_width": {"type": "integer", "description": "Spaces per indent level", "default": 2},
                    "keyword_case": {"type": "string", "description": "Case for SQL keywords", "enum": ["upper", "lower", "preserve"], "default": "upper"}
                },
                "required": ["sql"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "sql_formatter":
            sql = arguments["sql"].strip()
            dialect = arguments.get("dialect", "generic")
            indent_width = arguments.get("indent_width", 2)
            keyword_case = arguments.get("keyword_case", "upper")
            
            try:
                # Simple SQL formatter (for 5-hour project)
                keywords = [
                    'SELECT', 'FROM', 'WHERE', 'JOIN', 'LEFT', 'RIGHT', 'INNER', 'OUTER',
                    'ON', 'AND', 'OR', 'NOT', 'IN', 'BETWEEN', 'LIKE', 'IS', 'NULL',
                    'GROUP BY', 'ORDER BY', 'HAVING', 'LIMIT', 'OFFSET', 'INSERT INTO',
                    'VALUES', 'UPDATE', 'SET', 'DELETE FROM', 'CREATE TABLE', 'DROP TABLE',
                    'ALTER TABLE', 'ADD', 'COLUMN', 'PRIMARY KEY', 'FOREIGN KEY', 'REFERENCES',
                    'UNION', 'ALL', 'DISTINCT', 'AS', 'CASE', 'WHEN', 'THEN', 'ELSE', 'END',
                    'EXISTS', 'ANY', 'ALL', 'SOME', 'WITH', 'RECURSIVE'
                ]
                
                # Apply keyword case
                if keyword_case == "upper":
                    def upper_keywords(match):
                        return match.group(0).upper()
                    # Simple regex to find SQL keywords
                    pattern = r'\b(' + '|'.join([re.escape(kw.lower()) for kw in keywords]) + r')\b'
                    sql = re.sub(pattern, upper_keywords, sql, flags=re.IGNORECASE)
                elif keyword_case == "lower":
                    pattern = r'\b(' + '|'.join(keywords) + r')\b'
                    sql = re.sub(pattern, lambda m: m.group(0).lower(), sql, flags=re.IGNORECASE)
                
                # Basic formatting
                indent = ' ' * indent_width
                lines = []
                current_indent = 0
                in_parentheses = 0
                
                # Split by clauses
                sql_lower = sql.lower()
                clause_patterns = [
                    r'(\bselect\b)', r'(\bfrom\b)', r'(\bwhere\b)', r'(\bjoin\b)',
                    r'(\bgroup by\b)', r'(\border by\b)', r'(\blimit\b)', r'(\boffset\b)',
                    r'(\bunion\b)', r'(\bintersect\b)', r'(\bexcept\b)'
                ]
                
                # Add newlines before major clauses
                formatted_sql = sql
                for pattern in clause_patterns:
                    formatted_sql = re.sub(pattern, r'\n\1', formatted_sql, flags=re.IGNORECASE)
                
                # Handle commas in SELECT
                formatted_sql = re.sub(r',\s*', ',\n' + indent, formatted_sql)
                
                # Clean up multiple newlines
                formatted_sql = re.sub(r'\n\s*\n', '\n', formatted_sql)
                
                # Add indentation
                lines = formatted_sql.split('\n')
                formatted_lines = []
                current_indent = 0
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Decrease indent for closing parentheses
                    if line.startswith(')'):
                        current_indent = max(0, current_indent - 1)
                    
                    formatted_lines.append((' ' * indent_width * current_indent) + line)
                    
                    # Increase indent for opening parentheses
                    if '(' in line and not line.startswith('('):
                        current_indent += 1
                
                result = '\n'.join(formatted_lines)
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"```sql\n{result}\n```"
                    }]
                }
                
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"```sql\n{sql}\n```\n\nNote: Could not format fully. Error: {str(e)}"
                    }]
                }
```

#### **30 min: Color Converter**
```python
# tools/color_converter.py
import re
import colorsys
from mcp.server import Server

# CSS color names
CSS_COLORS = {
    'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7', 'aqua': '#00FFFF',
    'aquamarine': '#7FFFD4', 'azure': '#F0FFFF', 'beige': '#F5F5DC',
    'bisque': '#FFE4C4', 'black': '#000000', 'blanchedalmond': '#FFEBCD',
    'blue': '#0000FF', 'blueviolet': '#8A2BE2', 'brown': '#A52A2A',
    'burlywood': '#DEB887', 'cadetblue': '#5F9EA0', 'chartreuse': '#7FFF00',
    'chocolate': '#D2691E', 'coral': '#FF7F50', 'cornflowerblue': '#6495ED',
    'cornsilk': '#FFF8DC', 'crimson': '#DC143C', 'cyan': '#00FFFF',
    'darkblue': '#00008B', 'darkcyan': '#008B8B', 'darkgoldenrod': '#B8860B',
    'darkgray': '#A9A9A9', 'darkgreen': '#006400', 'darkgrey': '#A9A9A9',
    'darkkhaki': '#BDB76B', 'darkmagenta': '#8B008B', 'darkolivegreen': '#556B2F',
    'darkorange': '#FF8C00', 'darkorchid': '#9932CC', 'darkred': '#8B0000',
    'darksalmon': '#E9967A', 'darkseagreen': '#8FBC8F', 'darkslateblue': '#483D8B',
    'darkslategray': '#2F4F4F', 'darkslategrey': '#2F4F4F', 'darkturquoise': '#00CED1',
    'darkviolet': '#9400D3', 'deeppink': '#FF1493', 'deepskyblue': '#00BFFF',
    'dimgray': '#696969', 'dimgrey': '#696969', 'dodgerblue': '#1E90FF',
    'firebrick': '#B22222', 'floralwhite': '#FFFAF0', 'forestgreen': '#228B22',
    'fuchsia': '#FF00FF', 'gainsboro': '#DCDCDC', 'ghostwhite': '#F8F8FF',
    'gold': '#FFD700', 'goldenrod': '#DAA520', 'gray': '#808080',
    'green': '#008000', 'greenyellow': '#ADFF2F', 'grey': '#808080',
    'honeydew': '#F0FFF0', 'hotpink': '#FF69B4', 'indianred': '#CD5C5C',
    'indigo': '#4B0082', 'ivory': '#FFFFF0', 'khaki': '#F0E68C',
    'lavender': '#E6E6FA', 'lavenderblush': '#FFF0F5', 'lawngreen': '#7CFC00',
    'lemonchiffon': '#FFFACD', 'lightblue': '#ADD8E6', 'lightcoral': '#F08080',
    'lightcyan': '#E0FFFF', 'lightgoldenrodyellow': '#FAFAD2', 'lightgray': '#D3D3D3',
    'lightgreen': '#90EE90', 'lightgrey': '#D3D3D3', 'lightpink': '#FFB6C1',
    'lightsalmon': '#FFA07A', 'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA',
    'lightslategray': '#778899', 'lightslategrey': '#778899', 'lightsteelblue': '#B0C4DE',
    'lightyellow': '#FFFFE0', 'lime': '#00FF00', 'limegreen': '#32CD32',
    'linen': '#FAF0E6', 'magenta': '#FF00FF', 'maroon': '#800000',
    'mediumaquamarine': '#66CDAA', 'mediumblue': '#0000CD', 'mediumorchid': '#BA55D3',
    'mediumpurple': '#9370DB', 'mediumseagreen': '#3CB371', 'mediumslateblue': '#7B68EE',
    'mediumspringgreen': '#00FA9A', 'mediumturquoise': '#48D1CC', 'mediumvioletred': '#C71585',
    'midnightblue': '#191970', 'mintcream': '#F5FFFA', 'mistyrose': '#FFE4E1',
    'moccasin': '#FFE4B5', 'navajowhite': '#FFDEAD', 'navy': '#000080',
    'oldlace': '#FDF5E6', 'olive': '#808000', 'olivedrab': '#6B8E23',
    'orange': '#FFA500', 'orangered': '#FF4500', 'orchid': '#DA70D6',
    'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98', 'paleturquoise': '#AFEEEE',
    'palevioletred': '#DB7093', 'papayawhip': '#FFEFD5', 'peachpuff': '#FFDAB9',
    'peru': '#CD853F', 'pink': '#FFC0CB', 'plum': '#DDA0DD',
    'powderblue': '#B0E0E6', 'purple': '#800080', 'rebeccapurple': '#663399',
    'red': '#FF0000', 'rosybrown': '#BC8F8F', 'royalblue': '#4169E1',
    'saddlebrown': '#8B4513', 'salmon': '#FA8072', 'sandybrown': '#F4A460',
    'seagreen': '#2E8B57', 'seashell': '#FFF5EE', 'sienna': '#A0522D',
    'silver': '#C0C0C0', 'skyblue': '#87CEEB', 'slateblue': '#6A5ACD',
    'slategray': '#708090', 'slategrey': '#708090', 'snow': '#FFFAFA',
    'springgreen': '#00FF7F', 'steelblue': '#4682B4', 'tan': '#D2B48C',
    'teal': '#008080', 'thistle': '#D8BFD8', 'tomato': '#FF6347',
    'turquoise': '#40E0D0', 'violet': '#EE82EE', 'wheat': '#F5DEB3',
    'white': '#FFFFFF', 'whitesmoke': '#F5F5F5', 'yellow': '#FFFF00',
    'yellowgreen': '#9ACD32'
}

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "color_converter",
            "description": "Convert between color formats (HEX, RGB, HSL, CSS names) with visual preview",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "color": {"type": "string", "description": "Color input in any format"},
                    "from_format": {"type": "string", "description": "Input format", "enum": ["auto", "hex", "rgb", "hsl", "name"], "default": "auto"},
                    "to_format": {"type": "string", "description": "Output format", "enum": ["all", "hex", "rgb", "hsl", "name"], "default": "all"}
                },
                "required": ["color"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "color_converter":
            color_input = arguments["color"].strip().lower()
            from_format = arguments.get("from_format", "auto")
            to_format = arguments.get("to_format", "all")
            
            try:
                # Parse color
                r, g, b = 0, 0, 0
                hex_color = ""
                color_name = ""
                
                if from_format == "auto":
                    # Try to auto-detect format
                    # Check if it's a CSS color name
                    if color_input in CSS_COLORS:
                        hex_color = CSS_COLORS[color_input]
                        color_name = color_input
                    # Check if it's hex
                    elif re.match(r'^#?[0-9a-f]{6}$', color_input.replace('#', '')):
                        hex_color = '#' + color_input.replace('#', '')
                    # Check if it's rgb/rgba
                    elif re.match(r'^rgb\(', color_input):
                        from_format = "rgb"
                    # Check if it's hsl
                    elif re.match(r'^hsl\(', color_input):
                        from_format = "hsl"
                    else:
                        from_format = "name"  # Try as name
                
                if from_format == "hex" or (from_format == "auto" and hex_color):
                    if not hex_color:
                        hex_color = '#' + color_input.replace('#', '')
                    # Validate hex
                    if len(hex_color) != 7:
                        hex_color = '#' + hex_color[1:].zfill(6)
                    r = int(hex_color[1:3], 16)
                    g = int(hex_color[3:5], 16)
                    b = int(hex_color[5:7], 16)
                
                elif from_format == "rgb":
                    # Parse rgb(r, g, b) or rgba(r, g, b, a)
                    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color_input)
                    if match:
                        r = int(match.group(1))
                        g = int(match.group(2))
                        b = int(match.group(3))
                        hex_color = f"#{r:02x}{g:02x}{b:02x}"
                
                elif from_format == "hsl":
                    # Parse hsl(h, s%, l%)
                    match = re.match(r'hsl\((\d+),\s*(\d+)%,\s*(\d+)%', color_input)
                    if match:
                        h = int(match.group(1)) / 360.0
                        s = int(match.group(2)) / 100.0
                        l = int(match.group(3)) / 100.0
                        # Convert HSL to RGB
                        r, g, b = [int(x * 255) for x in colorsys.hls_to_rgb(h, l, s)]
                        hex_color = f"#{r:02x}{g:02x}{b:02x}"
                
                elif from_format == "name":
                    if color_input in CSS_COLORS:
                        hex_color = CSS_COLORS[color_input]
                        color_name = color_input
                        r = int(hex_color[1:3], 16)
                        g = int(hex_color[3:5], 16)
                        b = int(hex_color[5:7], 16)
                    else:
                        # Try to find closest color
                        import math
                        def color_distance(c1, c2):
                            r1, g1, b1 = c1
                            r2, g2, b2 = c2
                            return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)
                        
                        # Try to parse as hex anyway
                        if re.match(r'^#?[0-9a-f]{3,6}$', color_input.replace('#', '')):
                            hex_input = color_input.replace('#', '')
                            if len(hex_input) == 3:
                                hex_input = ''.join([c*2 for c in hex_input])
                            hex_color = '#' + hex_input.zfill(6)
                            r = int(hex_color[1:3], 16)
                            g = int(hex_color[3:5], 16)
                            b = int(hex_color[5:7], 16)
                        else:
                            return {
                                "content": [{
                                    "type": "text",
                                    "text": f"❌ Unknown color name: '{color_input}'\nTry: red, #FF0000, rgb(255,0,0), or hsl(0, 100%, 50%)"
                                }]
                            }
                
                # Generate outputs
                if not hex_color:
                    hex_color = f"#{r:02x}{g:02x}{b:02x}"
                
                # RGB
                rgb_str = f"rgb({r}, {g}, {b})"
                
                # HSL
                h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
                hsl_str = f"hsl({int(h*360)}, {int(s*100)}%, {int(l*100)}%)"
                
                # CMYK (approximation)
                if r == 0 and g == 0 and b == 0:
                    c, m, y, k = 0, 0, 0, 100
                else:
                    c = 1 - (r / 255.0)
                    m = 1 - (g / 255.0)
                    y = 1 - (b / 255.0)
                    k = min(c, m, y)
                    if k == 1:
                        c = m = y = 0
                    else:
                        c = (c - k) / (1 - k)
                        m = (m - k) / (1 - k)
                        y = (y - k) / (1 - k)
                
                cmyk_str = f"cmyk({int(c*100)}%, {int(m*100)}%, {int(y*100)}%, {int(k*100)}%)"
                
                # Find closest CSS color name
                if not color_name:
                    import math
                    min_dist = float('inf')
                    closest_name = ""
                    for name, hex_val in CSS_COLORS.items():
                        cr = int(hex_val[1:3], 16)
                        cg = int(hex_val[3:5], 16)
                        cb = int(hex_val[5:7], 16)
                        dist = math.sqrt((r-cr)**2 + (g-cg)**2 + (b-cb)**2)
                        if dist < min_dist:
                            min_dist = dist
                            closest_name = name
                    color_name = closest_name
                
                # Build response
                # Create ASCII color block
                color_block = "██" * 10
                
                response = f"""## 🎨 Color Converter

**Input:** `{color_input}`
**Preview:** `{color_block}`

**Formats:**
• **HEX:** `{hex_color.upper()}`
• **RGB:** `{rgb_str}`
• **HSL:** `{hsl_str}`
• **CMYK:** `{cmyk_str}`
• **CSS Name:** `{color_name}`"""
                
                if to_format != "all":
                    if to_format == "hex":
                        response = f"HEX: `{hex_color.upper()}`"
                    elif to_format == "rgb":
                        response = f"RGB: `{rgb_str}`"
                    elif to_format == "hsl":
                        response = f"HSL: `{hsl_str}`"
                    elif to_format == "name":
                        response = f"CSS Name: `{color_name}`"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": response
                    }]
                }
                
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error converting color: {str(e)}\n\nTry formats:\n- HEX: #FF5733 or FF5733\n- RGB: rgb(255, 87, 51)\n- HSL: hsl(11, 100%, 60%)\n- Name: red, blue, green"
                    }]
                }
```

### **Hour 5: Final Tool & Polish** (4:00-5:00)

#### **45 min: HTTP Tester (The Most Complex Tool)**
```python
# tools/http_tester.py
import httpx
import json
import time
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "http_tester",
            "description": "Make HTTP requests (GET, POST, PUT, DELETE) and inspect responses",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "method": {"type": "string", "description": "HTTP method", "enum": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"], "default": "GET"},
                    "url": {"type": "string", "description": "Full URL with protocol (http:// or https://)"},
                    "headers": {"type": "object", "description": "Request headers as JSON object", "default": {}},
                    "body": {"type": "string", "description": "Request body (for POST, PUT, PATCH)", "default": ""},
                    "params": {"type": "object", "description": "Query parameters as JSON object", "default": {}},
                    "timeout": {"type": "integer", "description": "Timeout in seconds", "default": 10},
                    "follow_redirects": {"type": "boolean", "description": "Follow HTTP redirects", "default": True}
                },
                "required": ["method", "url"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "http_tester":
            method = arguments["method"].upper()
            url = arguments["url"]
            headers = arguments.get("headers", {})
            body = arguments.get("body", "")
            params = arguments.get("params", {})
            timeout = arguments.get("timeout", 10)
            follow_redirects = arguments.get("follow_redirects", True)
            
            # Validate URL
            if not url.startswith(('http://', 'https://')):
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Invalid URL: Must start with http:// or https://\nYou provided: {url}"
                    }]
                }
            
            try:
                # Prepare request
                request_headers = dict(headers)
                if body and 'content-type' not in [k.lower() for k in request_headers.keys()]:
                    request_headers['Content-Type'] = 'application/json'
                
                # Prepare request data
                request_data = None
                if body:
                    try:
                        # Try to parse as JSON
                        json.loads(body)
                        request_data = body
                    except:
                        # Use as plain text
                        request_data = body
                
                # Make request
                start_time = time.time()
                
                async with httpx.AsyncClient(
                    timeout=timeout,
                    follow_redirects=follow_redirects
                ) as client:
                    response = await client.request(
                        method=method,
                        url=url,
                        headers=request_headers,
                        content=request_data,
                        params=params
                    )
                
                end_time = time.time()
                response_time = int((end_time - start_time) * 1000)  # ms
                
                # Parse response
                status_emoji = "✅" if 200 <= response.status_code < 300 else "⚠️" if 300 <= response.status_code < 400 else "❌"
                
                # Try to parse response body
                response_body = response.text
                content_type = response.headers.get('content-type', '').lower()
                
                # Format response body
                formatted_body = response_body
                if 'application/json' in content_type:
                    try:
                        json_data = json.loads(response_body)
                        formatted_body = json.dumps(json_data, indent=2)
                        language = "json"
                    except:
                        language = "text"
                elif 'html' in content_type:
                    language = "html"
                    # Truncate large HTML
                    if len(formatted_body) > 1000:
                        formatted_body = formatted_body[:1000] + "\n... [truncated]"
                elif 'xml' in content_type:
                    language = "xml"
                else:
                    language = "text"
                
                # Build response
                response_text = f"""## 🌐 HTTP Response

{status_emoji} **{method} {url}** ({response.status_code} {response.reason_phrase})
⏱️ {response_time}ms

### Request Details
**Method:** {method}
**URL:** `{url}`
**Timeout:** {timeout}s
**Redirects:** {'✅ Followed' if follow_redirects else '❌ Not followed'}

### Response Headers
"""
                
                # Add headers
                for key, value in response.headers.items():
                    if key.lower() not in ['set-cookie', 'cookie']:  # Skip sensitive headers
                        response_text += f"• **{key}:** {value}\n"
                
                response_text += f"\n### Response Body"
                
                # Truncate very large responses
                if len(formatted_body) > 3000:
                    preview = formatted_body[:3000]
                    response_text += f" (first 3000 chars):\n```{language}\n{preview}\n... [truncated]\n```"
                else:
                    response_text += f":\n```{language}\n{formatted_body}\n```"
                
                # Add size info
                size_kb = len(response_body) / 1024
                response_text += f"\n**Size:** {size_kb:.1f} KB"
                
                return {
                    "content": [{
                        "type": "text",
                        "text": response_text
                    }]
                }
                
            except httpx.TimeoutException:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"⏱️ Request timed out after {timeout} seconds"
                    }]
                }
            except httpx.ConnectError:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"🔌 Connection failed. Check:\n1. URL is correct\n2. Server is running\n3. Network connection"
                    }]
                }
            except httpx.HTTPStatusError as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ HTTP Error: {e.response.status_code}\nResponse: {e.response.text[:500]}"
                    }]
                }
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
```

#### **15 min: Final Integration & Error Handling**
```python
# utils/errors.py - Add this file
class ToolError(Exception):
    def __init__(self, message, tool_name=None, user_friendly=True):
        self.message = message
        self.tool_name = tool_name
        self.user_friendly = user_friendly
        super().__init__(self.message)

def create_error_response(error_msg, suggestion=""):
    """Create consistent error responses"""
    base = f"❌ {error_msg}"
    if suggestion:
        base += f"\n💡 Tip: {suggestion}"
    return {
        "content": [{
            "type": "text",
            "text": base
        }]
    }

# utils/formatters.py - Add this file
def format_success_response(data, tool_name, metadata=None):
    """Format successful tool responses consistently"""
    if metadata is None:
        metadata = {}
    
    response = {
        "content": [{
            "type": "text",
            "text": data
        }]
    }
    
    if metadata:
        response["metadata"] = metadata
    
    return response

# Update all tools to use these utilities
```

#### **Final 10 minutes: Celebration & Testing**
```bash
# 1. Create a quick test script
echo '#!/usr/bin/env python3
import asyncio
import sys
sys.path.append(".")

from server import main

if __name__ == "__main__":
    print("🚀 Starting DevKit Max Server...")
    print("Loaded tools: JSON, Base64, UUID, JWT, Time, Hash, HTTP, SQL, Color")
    print("Press Ctrl+C to stop")
    asyncio.run(main())
' > run.py

# 2. Create README
echo '# DevKit Max 🚀

Complete developer toolbox as an MCP server for Claude Desktop.

## Features
- JSON Formatter/Validator
- Base64 Encoder/Decoder  
- UUID Generator
- JWT Decoder
- Timestamp Converter
- Hash Generator
- HTTP Tester
- SQL Formatter
- Color Converter

## Quick Start
```bash
# Install dependencies
uv pip install -r requirements.txt

# Run the server
python run.py

# In Claude Desktop, add MCP server:
# Protocol: stdio
# Command: python /path/to/run.py
```

## Usage Examples
- "Format this JSON: {\"test\":1}"
- "Generate 3 UUIDs"
- "Decode this JWT: eyJ0eXAiOiJKV1Qi..."
- "Convert timestamp 1672531200 to human date"
- "Make a GET request to https://api.github.com"

Built with ❤️ in 5 hours of vibe coding.' > README.md

# 3. Celebrate!
echo "🎉 DevKit Max completed in 5 hours!"
echo "✨ 9 tools ready to use in Claude Desktop"
echo "🚀 Go build something amazing!"
```

---

## 🎯 Final Checklist Before Hour 5 Ends

### **Technical Completion**
- [ ] All 9 tools implemented
- [ ] Server runs without errors
- [ ] Tools accessible through MCP
- [ ] Basic error handling in place
- [ ] Response formatting looks good

### **User Experience**
- [ ] Clear tool descriptions
- [ ] Helpful error messages
- [ ] Pretty output formatting
- [ ] Works in Claude Desktop

### **Documentation**
- [ ] README with setup instructions
- [ ] Example usage for each tool
- [ ] One-line run command

### **Celebration**
- [ ] Take a screenshot of working tool
- [ ] Test your favorite tool
- [ ] Share with a friend
- [ ] Tweet your accomplishment! 🚀

---

## 🎮 The Vibe Coding Experience

### **Why This Will Be Epic**
1. **Hour 1**: "I built something!" - JSON & UUID tools working
2. **Hour 2**: "This is getting cool" - Base64, Hash, JWT done
3. **Hour 3**: "Time wizardry!" - Timestamp converter with relative time
4. **Hour 4**: "Making it pretty" - SQL formatting & color conversion
5. **Hour 5**: "Full power!" - HTTP tester completes the suite

### **Pro Tips for Maximum Vibe**
```python
# Keep the energy high:
# 1. Play your favorite coding playlist 🎵
# 2. Take 5-minute breaks every hour 🚶
# 3. Celebrate each completed tool 🎉
# 4. Keep water/snacks nearby 🍵
# 5. Remember: This is FUN, not work! ✨
```

### **When You Finish**
```python
print("""
╔═══════════════════════════════════════╗
║        🎉 DEVKIT MAX COMPLETE! 🎉      ║
╠═══════════════════════════════════════╣
║ 9 tools built in 5 hours             ║
║ Your developer workflow just leveled ║
║ up!                                 ║
║                                     ║
║ Go use your new powers! 🚀          ║
╚═══════════════════════════════════════╝
""")
```

---

## 🚀 Ready, Set, Code!

**Your mission**: Follow this guide, build all 9 tools, and have a complete MCP server running in 5 hours.

**Remember**: 
- Start simple (JSON formatter)
- Build momentum (quick wins)
- Embrace challenges (HTTP tester)
- Finish strong (polish & celebrate)


