"""
Color Converter Tool
Convert between color formats (HEX, RGB, HSL, CSS names)
"""

import re
import colorsys
import math
from mcp.server import Server


# CSS color names dictionary
CSS_COLORS = {
    'red': '#FF0000', 'blue': '#0000FF', 'green': '#008000', 'white': '#FFFFFF',
    'black': '#000000', 'yellow': '#FFFF00', 'cyan': '#00FFFF', 'magenta': '#FF00FF',
    'gray': '#808080', 'grey': '#808080', 'silver': '#C0C0C0', 'maroon': '#800000',
    'olive': '#808000', 'lime': '#00FF00', 'aqua': '#00FFFF', 'teal': '#008080',
    'navy': '#000080', 'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB',
    'brown': '#A52A2A', 'gold': '#FFD700', 'coral': '#FF7F50', 'salmon': '#FA8072',
    'khaki': '#F0E68C', 'plum': '#DDA0DD', 'turquoise': '#40E0D0', 'violet': '#EE82EE',
    'indigo': '#4B0082', 'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7',
    'darkblue': '#00008B', 'darkgreen': '#006400', 'darkred': '#8B0000',
    'lightyellow': '#FFFFE0', 'lightgreen': '#90EE90', 'lightblue': '#ADD8E6',
}


def register_tool(server: Server):
    """Register color converter tool with the server"""
    
    @server.list_tools()
    async def handle_list_tools():
        return [{
            "name": "color_converter",
            "description": "Convert between color formats (HEX, RGB, HSL, CSS names) with visual preview",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "color": {
                        "type": "string",
                        "description": "Color input in any format"
                    },
                    "from_format": {
                        "type": "string",
                        "description": "Input format",
                        "enum": ["auto", "hex", "rgb", "hsl", "name"],
                        "default": "auto"
                    },
                    "to_format": {
                        "type": "string",
                        "description": "Output format",
                        "enum": ["all", "hex", "rgb", "hsl", "name"],
                        "default": "all"
                    }
                },
                "required": ["color"]
            }
        }]
    
    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict):
        if name == "color_converter":
            try:
                color_input = arguments["color"].strip().lower()
                from_format = arguments.get("from_format", "auto")
                to_format = arguments.get("to_format", "all")
                
                r, g, b = 0, 0, 0
                hex_color = ""
                color_name = ""
                
                # Parse color input
                if from_format == "auto":
                    # Try CSS color name first
                    if color_input in CSS_COLORS:
                        hex_color = CSS_COLORS[color_input]
                        color_name = color_input
                        r = int(hex_color[1:3], 16)
                        g = int(hex_color[3:5], 16)
                        b = int(hex_color[5:7], 16)
                    # Try hex format
                    elif re.match(r'^#?[0-9a-f]{6}$', color_input.replace('#', '')):
                        hex_color = '#' + color_input.replace('#', '').upper()
                        r = int(hex_color[1:3], 16)
                        g = int(hex_color[3:5], 16)
                        b = int(hex_color[5:7], 16)
                    # Try rgb format
                    elif re.match(r'^rgb\(', color_input):
                        from_format = "rgb"
                    # Try hsl format
                    elif re.match(r'^hsl\(', color_input):
                        from_format = "hsl"
                    else:
                        return {
                            "content": [{
                                "type": "text",
                                "text": f"""❌ Unknown color format: '{color_input}'

Try formats:
- Hex: `#FF0000` or `FF0000`
- RGB: `rgb(255, 0, 0)`
- HSL: `hsl(0, 100%, 50%)`
- Name: `red`, `blue`, `green`"""
                            }]
                        }
                
                if from_format == "hex" and not hex_color:
                    hex_color = '#' + color_input.replace('#', '').upper()
                    r = int(hex_color[1:3], 16)
                    g = int(hex_color[3:5], 16)
                    b = int(hex_color[5:7], 16)
                
                elif from_format == "rgb":
                    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color_input)
                    if match:
                        r = int(match.group(1))
                        g = int(match.group(2))
                        b = int(match.group(3))
                        hex_color = f"#{r:02X}{g:02X}{b:02X}"
                
                elif from_format == "hsl":
                    match = re.match(r'hsl\((\d+),\s*(\d+)%,\s*(\d+)%', color_input)
                    if match:
                        h = int(match.group(1)) / 360.0
                        s = int(match.group(2)) / 100.0
                        l = int(match.group(3)) / 100.0
                        r_f, g_f, b_f = colorsys.hls_to_rgb(h, l, s)
                        r, g, b = int(r_f * 255), int(g_f * 255), int(b_f * 255)
                        hex_color = f"#{r:02X}{g:02X}{b:02X}"
                
                elif from_format == "name":
                    if color_input in CSS_COLORS:
                        hex_color = CSS_COLORS[color_input]
                        color_name = color_input
                        r = int(hex_color[1:3], 16)
                        g = int(hex_color[3:5], 16)
                        b = int(hex_color[5:7], 16)
                
                # Ensure we have hex_color
                if not hex_color:
                    hex_color = f"#{r:02X}{g:02X}{b:02X}"
                
                # Find closest CSS color name if not already set
                if not color_name:
                    min_dist = float('inf')
                    for name, hex_val in CSS_COLORS.items():
                        cr = int(hex_val[1:3], 16)
                        cg = int(hex_val[3:5], 16)
                        cb = int(hex_val[5:7], 16)
                        dist = math.sqrt((r-cr)**2 + (g-cg)**2 + (b-cb)**2)
                        if dist < min_dist:
                            min_dist = dist
                            color_name = name
                
                # Generate all formats
                rgb_str = f"rgb({r}, {g}, {b})"
                
                # HSL
                h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
                hsl_str = f"hsl({int(h*360)}, {int(s*100)}%, {int(l*100)}%)"
                
                # Build response
                color_block = "████████"
                
                if to_format == "all":
                    response = f"""## 🎨 Color Converter

**Input:** `{color_input}`
**Preview:** `{color_block}`

**Formats:**
• **HEX:** `{hex_color.upper()}`
• **RGB:** `{rgb_str}`
• **HSL:** `{hsl_str}`
• **CSS Name:** `{color_name}`"""
                
                elif to_format == "hex":
                    response = f"`{hex_color.upper()}`"
                elif to_format == "rgb":
                    response = f"`{rgb_str}`"
                elif to_format == "hsl":
                    response = f"`{hsl_str}`"
                else:  # name
                    response = f"`{color_name}`"
                
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
                        "text": f"❌ Error: {str(e)}"
                    }]
                }
