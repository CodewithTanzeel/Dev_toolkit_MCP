"""
Base64 Encoder/Decoder Tool
Bidirectional Base64 conversion with URL-safe support
"""

import base64
from mcp.server import Server


def register_tool(server: Server):
    """Register Base64 tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "base64_tool",
            "description": "Encode or decode Base64 strings with optional URL-safe formatting",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform",
                        "enum": ["encode", "decode"],
                        "default": "encode"
                    },
                    "input": {
                        "type": "string",
                        "description": "Text to encode or Base64 to decode"
                    },
                    "url_safe": {
                        "type": "boolean",
                        "description": "Use URL-safe Base64 encoding (replaces + with -, / with _)",
                        "default": False
                    }
                },
                "required": ["operation", "input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "base64_tool":
            try:
                operation = arguments["operation"]
                input_text = arguments["input"]
                url_safe = arguments.get("url_safe", False)
                
                if operation == "encode":
                    # Encode to Base64
                    if url_safe:
                        encoded = base64.urlsafe_b64encode(input_text.encode()).decode().rstrip("=")
                    else:
                        encoded = base64.b64encode(input_text.encode()).decode()
                    
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"""✅ Encoded to Base64 ({len(input_text)} chars → {len(encoded)} chars)

```
{encoded}
```

**Copy to clipboard:** `{encoded}`"""
                        }]
                    }
                
                else:  # decode
                    # Decode from Base64
                    try:
                        if url_safe:
                            # Add padding if needed
                            padding = 4 - len(input_text) % 4
                            padded = input_text if padding == 4 else input_text + "=" * padding
                            decoded = base64.urlsafe_b64decode(padded).decode()
                        else:
                            decoded = base64.b64decode(input_text).decode()
                        
                        return {
                            "content": [{
                                "type": "text",
                                "text": f"""✅ Decoded from Base64 ({len(input_text)} chars → {len(decoded)} chars)

```
{decoded}
```

**Copy to clipboard:** `{decoded}`"""
                            }]
                        }
                    
                    except Exception as e:
                        return {
                            "content": [{
                                "type": "text",
                                "text": f"""❌ Failed to decode Base64

**Error:** {str(e)}

**Troubleshooting:**
- Ensure input is valid Base64
- Check if URL-safe option should be enabled
- Remove any extra whitespace"""
                            }]
                        }
            
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
