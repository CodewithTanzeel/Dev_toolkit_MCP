"""
UUID Generator Tool
Generate unique identifiers (UUIDv1 or UUIDv4)
"""

import uuid
from mcp.server import Server


def register_tool(server: Server):
    """Register UUID generator tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "uuid_generator",
            "description": "Generate UUIDs (version 1 or 4) with formatting options",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer",
                        "description": "Number of UUIDs to generate",
                        "default": 1,
                        "minimum": 1,
                        "maximum": 50
                    },
                    "version": {
                        "type": "string",
                        "description": "UUID version (v1 or v4)",
                        "enum": ["v1", "v4"],
                        "default": "v4"
                    },
                    "hyphens": {
                        "type": "boolean",
                        "description": "Include hyphens in output",
                        "default": True
                    }
                }
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "uuid_generator":
            try:
                count = arguments.get("count", 1)
                version = arguments.get("version", "v4")
                hyphens = arguments.get("hyphens", True)
                
                # Validate count
                count = max(1, min(50, count))
                
                # Generate UUIDs
                uuids = []
                for _ in range(count):
                    if version == "v1":
                        uid = str(uuid.uuid1())
                    else:  # v4
                        uid = str(uuid.uuid4())
                    
                    # Remove hyphens if requested
                    if not hyphens:
                        uid = uid.replace("-", "")
                    
                    uuids.append(uid)
                
                # Format output
                output_lines = [f"Generated {count} UUID{version}:\n"]
                for i, uid in enumerate(uuids, 1):
                    output_lines.append(f"{i}. `{uid}`")
                
                return {
                    "content": [{
                        "type": "text",
                        "text": "\n".join(output_lines)
                    }]
                }
            
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
