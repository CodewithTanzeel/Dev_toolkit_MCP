#!/usr/bin/env python3
"""
DevKit Max - MCP Server with 9 Developer Tools
Main server entry point with dynamic tool loading
"""

import asyncio
import importlib
import os
import sys
from typing import List

from mcp.server import Server, NotificationOptions
import mcp.server.stdio

# Initialize server
server = Server("devkit-max")

# Track loaded tools
loaded_tools: List[str] = []


def load_tools():
    """Dynamically load all tools from tools directory"""
    global loaded_tools
    
    tools_dir = os.path.join(os.path.dirname(__file__), "tools")
    
    # Find all Python files in tools directory
    tool_files = [
        f[:-3] for f in os.listdir(tools_dir)
        if f.endswith(".py") and f != "__init__.py"
    ]
    
    print(f"📦 Loading {len(tool_files)} tools...", file=sys.stderr)
    
    for tool_file in sorted(tool_files):
        try:
            # Dynamically import tool module
            module = importlib.import_module(f"tools.{tool_file}")
            
            # Call register_tool function if it exists
            if hasattr(module, "register_tool"):
                module.register_tool(server)
                loaded_tools.append(tool_file)
                print(f"  ✅ {tool_file}", file=sys.stderr)
            else:
                print(f"  ⚠️  {tool_file} - missing register_tool function", file=sys.stderr)
        except Exception as e:
            print(f"  ❌ {tool_file} - {str(e)}", file=sys.stderr)
    
    print(f"\n✨ Loaded {len(loaded_tools)} tools successfully!", file=sys.stderr)
    return loaded_tools


async def main():
    """Main entry point for the MCP server"""
    # Load all tools
    load_tools()
    
    # Run MCP server over stdio
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, NotificationOptions())


if __name__ == "__main__":
    asyncio.run(main())
