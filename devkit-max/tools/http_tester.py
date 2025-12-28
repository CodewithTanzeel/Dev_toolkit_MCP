"""
HTTP Tester Tool
Make HTTP requests and inspect responses
"""

import httpx
import json
import time
import asyncio
from mcp.server import Server


def register_tool(server: Server):
    """Register HTTP tester tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "http_tester",
            "description": "Make HTTP requests (GET, POST, PUT, DELETE, PATCH) and inspect responses",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "method": {
                        "type": "string",
                        "description": "HTTP method",
                        "enum": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"],
                        "default": "GET"
                    },
                    "url": {
                        "type": "string",
                        "description": "Full URL with protocol (http:// or https://)"
                    },
                    "headers": {
                        "type": "object",
                        "description": "Request headers as JSON object",
                        "default": {}
                    },
                    "body": {
                        "type": "string",
                        "description": "Request body (for POST, PUT, PATCH)",
                        "default": ""
                    },
                    "timeout": {
                        "type": "integer",
                        "description": "Timeout in seconds",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 60
                    }
                },
                "required": ["method", "url"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "http_tester":
            try:
                method = arguments["method"].upper()
                url = arguments["url"]
                headers = arguments.get("headers", {})
                body = arguments.get("body", "")
                timeout = arguments.get("timeout", 10)
                
                # Validate URL
                if not url.startswith(('http://', 'https://')):
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"""❌ Invalid URL

Must start with http:// or https://
You provided: `{url}`"""
                        }]
                    }
                
                # Prepare request
                request_headers = dict(headers) if isinstance(headers, dict) else {}
                if body and 'content-type' not in [k.lower() for k in request_headers.keys()]:
                    request_headers['Content-Type'] = 'application/json'
                
                # Make request
                start_time = time.time()
                
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(
                        method=method,
                        url=url,
                        headers=request_headers,
                        content=body if body else None
                    )
                
                end_time = time.time()
                response_time = int((end_time - start_time) * 1000)
                
                # Parse response
                status_emoji = "✅" if 200 <= response.status_code < 300 else "⚠️" if 300 <= response.status_code < 400 else "❌"
                
                response_body = response.text
                content_type = response.headers.get('content-type', '').lower()
                
                # Format body for display
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
                    if len(formatted_body) > 500:
                        formatted_body = formatted_body[:500] + "\n... [truncated]"
                else:
                    language = "text"
                
                # Build response text
                response_text = f"{status_emoji} **{method} {url}** ({response.status_code})\n"
                response_text += f"⏱️ {response_time}ms\n\n"
                
                # Headers section
                response_text += "**Response Headers:**\n"
                for key, value in list(response.headers.items())[:10]:
                    if key.lower() not in ['set-cookie']:
                        response_text += f"• {key}: {value}\n"
                
                response_text += f"\n**Response Body:**\n"
                
                # Truncate very large responses
                if len(formatted_body) > 2000:
                    preview = formatted_body[:2000]
                    response_text += f"```{language}\n{preview}\n... [truncated]\n```"
                else:
                    response_text += f"```{language}\n{formatted_body}\n```"
                
                # Size info
                size_kb = len(response_body) / 1024
                response_text += f"\n**Size:** {size_kb:.2f} KB"
                
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
                        "text": f"⏱️ Request timed out after {arguments.get('timeout', 10)} seconds"
                    }]
                }
            except httpx.ConnectError:
                return {
                    "content": [{
                        "type": "text",
                        "text": "🔌 Connection failed. Check URL and network connection."
                    }]
                }
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
