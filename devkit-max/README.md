# DevKit Max - Complete Developer Toolbox 🚀

Your ultimate developer companion as an MCP server for Claude Desktop.

## Overview

**DevKit Max** is a collection of 9 essential developer tools delivered as an MCP server. Each tool is carefully crafted to solve real development challenges with beautiful, user-friendly responses.

### The 9 Tools

1. **JSON Formatter** - Validate and prettify JSON with optional key sorting
2. **Base64 Encoder/Decoder** - Bidirectional Base64 conversion with URL-safe support
3. **UUID Generator** - Generate unique identifiers (v1 or v4) in multiple formats
4. **JWT Decoder** - Parse JWT tokens and inspect claims and expiration
5. **Timestamp Converter** - Convert between Unix, ISO, and human-readable formats
6. **Hash Generator** - Generate MD5, SHA1, SHA256, SHA512 hashes in hex or Base64
7. **SQL Formatter** - Format and prettify SQL queries with customizable indentation
8. **HTTP Tester** - Make HTTP requests and inspect responses with full details
9. **Color Converter** - Convert between HEX, RGB, HSL, and CSS color names

---

## Quick Start

### Prerequisites
- Python 3.8+
- pip or uv (recommended)

### Installation

```bash
# Clone or download the project
cd devkit-max

# Install dependencies
pip install -r requirements.txt
# or with uv:
# uv pip install -r requirements.txt
```

### Running the Server

```bash
# Method 1: Direct Python
python server.py

# Method 2: With explicit module
python -m server

# Method 3: For Claude Desktop
# Add to claude_desktop_config.json:
{
  "mcpServers": {
    "devkit-max": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

---

## Tool Usage Examples

### 1. JSON Formatter

**Use Case:** Clean up and validate JSON data

```
Input: {"name":"john","data":[1,2,3]}
Output:
{
  "data": [
    1,
    2,
    3
  ],
  "name": "john"
}
```

**Parameters:**
- `json_string` (required) - JSON to format
- `indent` (optional, default: 2) - Spaces per indent level
- `sort_keys` (optional, default: false) - Sort object keys

---

### 2. Base64 Encoder/Decoder

**Use Case:** Encode/decode Base64 strings for API authentication or data encoding

```
Encode: "Hello World" → "SGVsbG8gV29ybGQ="
Decode: "SGVsbG8gV29ybGQ=" → "Hello World"
```

**Parameters:**
- `operation` (required) - "encode" or "decode"
- `input` (required) - Text or Base64 string
- `url_safe` (optional, default: false) - Use URL-safe Base64

---

### 3. UUID Generator

**Use Case:** Generate unique identifiers for databases, APIs, or distributed systems

```
Generated 3 UUIDv4:
1. `550e8400-e29b-41d4-a716-446655440000`
2. `6ba7b810-9dad-11d1-80b4-00c04fd430c8`
3. `123e4567-e89b-12d3-a456-426614174000`
```

**Parameters:**
- `count` (optional, default: 1, max: 50) - Number of UUIDs to generate
- `version` (optional, default: "v4") - "v1" or "v4"
- `hyphens` (optional, default: true) - Include hyphens

---

### 4. JWT Decoder

**Use Case:** Inspect JWT tokens for debugging authentication issues

```
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Header:
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload:
{
  "sub": "1234567890",
  "name": "John Doe",
  "exp": 1516242622
}

Status: ⚠️ Token expired 2 years ago
```

**Parameters:**
- `token` (required) - JWT token to decode
- `verify_signature` (optional, default: false) - Check format

---

### 5. Timestamp Converter

**Use Case:** Convert between different time formats

```
Input: 1672531200
Conversions:
• Unix: 1672531200
• ISO: 2023-01-01T00:00:00+00:00
• Human: January 1, 2023, 12:00:00 AM UTC
• Relative: 1 year ago
```

**Parameters:**
- `input` (required) - Unix timestamp, ISO date, or human date
- `input_format` (optional, default: "auto") - Format hint
- `output_format` (optional, default: "all") - Which format to output
- `timezone` (optional, default: "UTC") - Target timezone

---

### 6. Hash Generator

**Use Case:** Generate cryptographic hashes for data integrity verification

```
Input: "hello"
SHA256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

**Parameters:**
- `input` (required) - Text to hash
- `algorithm` (optional, default: "sha256") - md5, sha1, sha256, or sha512
- `encoding` (optional, default: "hex") - "hex" or "base64"

---

### 7. SQL Formatter

**Use Case:** Clean up SQL queries for readability

```
Input: SELECT * FROM users WHERE active=1 AND age>18 ORDER BY name

Output:
SELECT 
  id,
  name,
  email
FROM 
  users
WHERE 
  active = 1
  AND age > 18
ORDER BY 
  name
```

**Parameters:**
- `sql` (required) - SQL query to format
- `dialect` (optional, default: "generic") - mysql, postgresql, sqlite, tsql
- `indent_width` (optional, default: 2) - Spaces per indent
- `keyword_case` (optional, default: "upper") - upper, lower, or preserve

---

### 8. HTTP Tester

**Use Case:** Make HTTP requests directly from Claude

```
GET https://api.github.com/users/octocat

Response:
✅ 200 OK
⏱️ 342ms

Headers:
• content-type: application/json
• x-ratelimit-remaining: 59

Body:
{
  "login": "octocat",
  "id": 1
}
```

**Parameters:**
- `method` (required) - GET, POST, PUT, DELETE, PATCH, HEAD
- `url` (required) - Full URL with protocol
- `headers` (optional) - Request headers as JSON object
- `body` (optional) - Request body for POST/PUT
- `timeout` (optional, default: 10) - Timeout in seconds

---

### 9. Color Converter

**Use Case:** Convert between color formats with visual preview

```
Input: #FF5733

Output:
🎨 Color: RGB(255, 87, 51)
Preview: ████████████████
• HEX: #FF5733
• RGB: rgb(255, 87, 51)
• HSL: hsl(11, 100%, 60%)
• CSS: coral
```

**Parameters:**
- `color` (required) - Color input in any format
- `from_format` (optional, default: "auto") - hex, rgb, hsl, or name
- `to_format` (optional, default: "all") - Output format preference

---

## Project Structure

```
devkit-max/
├── server.py              # Main MCP server entry point
├── requirements.txt       # Dependencies
├── test_tools.py          # Quick functionality tests
├── README.md             # Documentation (this file)
├── tools/                # Tool implementations
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
└── utils/                # Shared utilities
    └── __init__.py
```

---

## Development

### Running Tests

```bash
# Quick functionality test
python test_tools.py

# Output should show all 7+ tests passing
```

### Adding New Tools

To add a new tool:

1. Create `tools/my_tool.py`
2. Implement `register_tool(server)` function
3. Define tool schema with `@server.list_tools()`
4. Implement handler with `@server.call_tool()`
5. Server automatically loads on startup

Example template:

```python
from mcp.server import Server

def register_tool(server: Server):
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "my_tool",
            "description": "What it does",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "param1": {"type": "string", "description": "..."}
                },
                "required": ["param1"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "my_tool":
            # Tool logic here
            return {
                "content": [{
                    "type": "text",
                    "text": "Result here"
                }]
            }
```

---

## Dependencies

- **mcp** ≥1.0.0 - MCP protocol implementation
- **python-dateutil** ≥2.8.2 - Robust date parsing
- **PyJWT** ≥2.8.0 - JWT decoding
- **httpx** ≥0.25.0 - Async HTTP client
- **pydantic** ≥2.4.0 - Data validation

Optional:
- **colorama** - Better color output in terminal

---

## Configuration

### Claude Desktop Integration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "devkit-max": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

### Troubleshooting

**Tools not loading?**
- Check Python version (requires 3.8+)
- Verify all dependencies installed: `pip list | grep -E "mcp|httpx|pydantic|dateutil"`
- Run `python test_tools.py` to verify basic functionality

**HTTP Tester times out?**
- Increase timeout parameter (up to 60 seconds)
- Check network connectivity
- Verify target URL is accessible

**Color Converter not recognizing colors?**
- Try different format: `#FF0000` instead of `FF0000`
- Use full color names (e.g., `darkred` not `dred`)
- Check hex format (must be 6 characters + # optional)

---

## Performance

- **JSON Formatter:** Instant (<10ms)
- **UUID Generator:** Instant (<5ms per UUID)
- **Base64 Operations:** Instant (<5ms)
- **Hash Generator:** <50ms for typical inputs
- **Timestamp Converter:** Instant (<10ms)
- **SQL Formatter:** <100ms for typical queries
- **HTTP Tester:** Depends on network (typically 100-1000ms)
- **Color Converter:** Instant (<5ms)
- **JWT Decoder:** <20ms for typical tokens

---

## Limitations & Notes

- **HTTP Tester:** Responses truncated at 2000 characters for display
- **JWT Decoder:** Signature not cryptographically verified (inspection only)
- **SQL Formatter:** Basic formatting; complex dialects may need manual adjustment
- **Color Converter:** CSS color names limited to common colors
- **UUID Generator:** Limited to 50 UUIDs per request to prevent abuse

---

## License

MIT License - Feel free to use and modify!

---

## Contributing

Found a bug? Want to add a tool?

1. Test thoroughly with `test_tools.py`
2. Follow the existing code style
3. Add docstrings to functions
4. Update this README with examples

---

## Support & Issues

If you encounter issues:

1. Run `python test_tools.py` to check basic functionality
2. Check error messages in tool responses
3. Verify dependencies with `pip list`
4. Ensure Claude Desktop can access the server path

---

## What's Next?

Ideas for expanding DevKit Max:

- [ ] Database query builder
- [ ] Markdown to HTML converter
- [ ] Regular expression tester
- [ ] IP address calculator
- [ ] XML formatter
- [ ] YAML validator
- [ ] Environment variable manager
- [ ] Code snippet formatter (Python, JS, etc.)

---

**Built with ❤️ for developers, by developers.**

Happy coding! 🚀
