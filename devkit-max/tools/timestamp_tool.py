"""
Timestamp Converter Tool
Convert between Unix timestamp, ISO 8601, and human-readable formats
"""

from datetime import datetime, timezone
from dateutil import parser as date_parser
from mcp.server import Server


def register_tool(server: Server):
    """Register timestamp converter tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "timestamp_tool",
            "description": "Convert between timestamp formats (Unix, ISO 8601, human-readable)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Time input (Unix timestamp, ISO date, or human date)"
                    },
                    "input_format": {
                        "type": "string",
                        "description": "Input format hint",
                        "enum": ["auto", "unix", "iso", "human"],
                        "default": "auto"
                    },
                    "output_format": {
                        "type": "string",
                        "description": "Output format preference",
                        "enum": ["all", "unix", "iso", "human"],
                        "default": "all"
                    },
                    "timezone": {
                        "type": "string",
                        "description": "Target timezone (e.g., UTC, America/New_York)",
                        "default": "UTC"
                    }
                },
                "required": ["input"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "timestamp_tool":
            try:
                input_str = arguments["input"]
                input_format = arguments.get("input_format", "auto")
                output_format = arguments.get("output_format", "all")
                timezone_str = arguments.get("timezone", "UTC")
                
                dt = None
                
                # Parse input based on format
                if input_format == "auto":
                    # Try Unix timestamp first
                    try:
                        timestamp = float(input_str)
                        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                    except ValueError:
                        try:
                            # Try ISO format
                            dt = date_parser.isoparse(input_str)
                        except:
                            # Try human-readable date
                            dt = date_parser.parse(input_str, ignoretz=False)
                
                elif input_format == "unix":
                    timestamp = float(input_str)
                    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                
                elif input_format == "iso":
                    dt = date_parser.isoparse(input_str)
                
                else:  # human
                    dt = date_parser.parse(input_str, ignoretz=False)
                
                # Ensure timezone aware
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                
                # Generate outputs
                unix_timestamp = int(dt.timestamp())
                iso_format = dt.isoformat()
                human_format = dt.strftime("%B %d, %Y, %I:%M:%S %p %Z")
                
                # Calculate relative time
                now = datetime.now(timezone.utc)
                diff = now - dt.replace(tzinfo=timezone.utc) if dt.tzinfo else now - dt
                seconds = diff.total_seconds()
                
                if seconds < 0:
                    # Future date
                    seconds = abs(seconds)
                    if seconds < 60:
                        relative = "in a few seconds"
                    elif seconds < 3600:
                        minutes = int(seconds / 60)
                        relative = f"in {minutes} minute{'s' if minutes != 1 else ''}"
                    elif seconds < 86400:
                        hours = int(seconds / 3600)
                        relative = f"in {hours} hour{'s' if hours != 1 else ''}"
                    else:
                        days = int(seconds / 86400)
                        relative = f"in {days} day{'s' if days != 1 else ''}"
                else:
                    # Past date
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
                
                # Build response
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
                        "text": f"""❌ Error parsing timestamp

**Error:** {str(e)}

**Try formats:**
- Unix: `1672531200`
- ISO: `2023-01-01T00:00:00Z`
- Human: `January 1, 2023` or `2023-01-01`"""
                    }]
                }
