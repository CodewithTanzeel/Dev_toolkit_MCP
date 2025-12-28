"""
JWT Decoder Tool
Parse and inspect JWT tokens without cryptographic verification
"""

import json
import base64
from datetime import datetime, timezone
from mcp.server import Server


def register_tool(server: Server):
    """Register JWT decoder tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "jwt_decoder",
            "description": "Decode and inspect JWT tokens without verifying signature",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "description": "JWT token to decode"
                    },
                    "verify_signature": {
                        "type": "boolean",
                        "description": "Check token format (not cryptographic verification)",
                        "default": False
                    }
                },
                "required": ["token"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "jwt_decoder":
            try:
                token = arguments["token"].strip()
                
                # Split token into parts
                parts = token.split(".")
                if len(parts) != 3:
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"""❌ Invalid JWT format

Expected 3 parts separated by dots, got {len(parts)}

**JWT structure:** header.payload.signature
**Your token:** {token[:50]}{'...' if len(token) > 50 else ''}"""
                        }]
                    }
                
                # Decode helper function
                def decode_part(part: str) -> dict:
                    # Add padding if needed
                    padding = 4 - len(part) % 4
                    if padding != 4:
                        part += "=" * padding
                    try:
                        decoded = base64.urlsafe_b64decode(part)
                        return json.loads(decoded)
                    except:
                        return {"_error": "Could not decode"}
                
                # Decode header and payload
                header = decode_part(parts[0])
                payload = decode_part(parts[1])
                signature = parts[2][:20] + "..." if len(parts[2]) > 20 else parts[2]
                
                # Build response
                response = "## 🔐 JWT Decoded\n\n"
                
                # Header section
                response += "### Header\n```json\n"
                response += json.dumps(header, indent=2)
                response += "\n```\n\n"
                
                # Payload section
                response += "### Payload\n```json\n"
                response += json.dumps(payload, indent=2)
                response += "\n```\n\n"
                
                # Expiration check
                if "exp" in payload and isinstance(payload["exp"], (int, float)):
                    exp_time = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
                    now = datetime.now(timezone.utc)
                    
                    if exp_time < now:
                        time_diff = now - exp_time
                        if time_diff.days > 0:
                            response += f"⚠️ **Token expired** {time_diff.days} days ago\n"
                        else:
                            hours = time_diff.seconds // 3600
                            response += f"⚠️ **Token expired** {hours} hours ago\n"
                    else:
                        time_diff = exp_time - now
                        if time_diff.days > 0:
                            response += f"✅ **Token valid** for {time_diff.days} more days\n"
                        else:
                            hours = time_diff.seconds // 3600
                            response += f"✅ **Token valid** for {hours} more hours\n"
                
                response += f"\n### Signature (preview)\n`{signature}`\n"
                response += "\n⚠️ **Note:** Signature not cryptographically verified"
                
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
                        "text": f"❌ Error decoding JWT: {str(e)}"
                    }]
                }
