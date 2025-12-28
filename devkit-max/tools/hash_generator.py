"""
Hash Generator Tool
Generate cryptographic hashes (MD5, SHA1, SHA256, SHA512)
"""

import hashlib
import base64
from mcp.server import Server


def register_tool(server: Server):
    """Register hash generator tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "hash_generator",
            "description": "Generate cryptographic hashes (MD5, SHA1, SHA256, SHA512)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Text to hash"
                    },
                    "algorithm": {
                        "type": "string",
                        "description": "Hash algorithm to use",
                        "enum": ["md5", "sha1", "sha256", "sha512"],
                        "default": "sha256"
                    },
                    "encoding": {
                        "type": "string",
                        "description": "Output encoding format",
                        "enum": ["hex", "base64"],
                        "default": "hex"
                    }
                },
                "required": ["input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "hash_generator":
            try:
                input_text = arguments["input"]
                algorithm = arguments.get("algorithm", "sha256").lower()
                encoding = arguments.get("encoding", "hex")
                
                # Select hash algorithm
                if algorithm == "md5":
                    hash_obj = hashlib.md5()
                elif algorithm == "sha1":
                    hash_obj = hashlib.sha1()
                elif algorithm == "sha256":
                    hash_obj = hashlib.sha256()
                elif algorithm == "sha512":
                    hash_obj = hashlib.sha512()
                else:
                    algorithm = "sha256"
                    hash_obj = hashlib.sha256()
                
                # Compute hash
                hash_obj.update(input_text.encode())
                
                # Encode output
                if encoding == "hex":
                    result = hash_obj.hexdigest()
                else:  # base64
                    result = base64.b64encode(hash_obj.digest()).decode()
                
                return {
                    "content": [{
                        "type": "text",
                        "text": f"""✅ Hash Generated

**Algorithm:** {algorithm.upper()}
**Encoding:** {encoding}
**Input:** {input_text[:50]}{'...' if len(input_text) > 50 else ''}
**Input Length:** {len(input_text)} chars

```
{result}
```

**Copy to clipboard:** `{result}`"""
                    }]
                }
            
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
