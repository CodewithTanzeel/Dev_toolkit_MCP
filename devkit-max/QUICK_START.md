# DevKit Max - Quick Start Guide ⚡

## 30-Second Setup

```bash
# 1. Go to directory
cd devkit-max

# 2. Install
pip install -r requirements.txt

# 3. Test
python test_tools.py

# 4. Done! Tools ready to use.
```

---

## Add to Claude Desktop (2 minutes)

### 1. Find Config File
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Mac:** `~/.config/Claude/claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

### 2. Edit Config
Add this block (replace `/path/to` with actual path):

```json
{
  "mcpServers": {
    "devkit-max": {
      "command": "python",
      "args": ["/absolute/path/to/devkit-max/server.py"]
    }
  }
}
```

### 3. Restart Claude
Close and reopen Claude Desktop.

### 4. Test
In Claude, type: "Generate a UUID"

Done! ✅

---

## The 9 Tools at a Glance

| Tool | What It Does | Example |
|------|---|---|
| **JSON Formatter** | Clean JSON | `{"a":1}` → formatted with indent |
| **Base64** | Encode/decode | `"hello"` ↔ `"aGVsbG8="` |
| **UUID** | Generate IDs | Creates unique identifiers |
| **JWT Decoder** | Inspect tokens | Shows header, payload, expiration |
| **Timestamp** | Convert times | Unix ↔ ISO ↔ Human readable |
| **Hash** | Generate hashes | SHA256, MD5, SHA1, SHA512 |
| **SQL Formatter** | Pretty SQL | Formats queries with indentation |
| **HTTP Tester** | Make requests | GET/POST to any URL |
| **Color** | Convert colors | HEX ↔ RGB ↔ HSL ↔ Names |

---

## Common Usage Examples

### 1. "Format this JSON"
```json
{"name":"john","age":30,"city":"NYC"}
```

Tool: JSON Formatter

Result:
```json
{
  "age": 30,
  "city": "NYC",
  "name": "john"
}
```

### 2. "Generate 5 UUIDs"
Tool: UUID Generator

Result:
```
1. `550e8400-e29b-41d4-a716-446655440000`
2. `6ba7b810-9dad-11d1-80b4-00c04fd430c8`
... etc
```

### 3. "Decode this token: eyJhbGciOiJIUzI1NiJ9..."
Tool: JWT Decoder

Result:
```
Header: {"alg": "HS256"}
Payload: {"sub": "user123"}
Status: ✅ Valid
```

### 4. "Hash 'password123' with SHA256"
Tool: Hash Generator

Result: `ef92b778bafe771e89245d171bafed6f56bc5785e1c2e014f7f7093fc4a79ffe`

### 5. "What time is 1672531200?"
Tool: Timestamp Converter

Result:
- Unix: `1672531200`
- ISO: `2023-01-01T00:00:00Z`
- Human: `January 1, 2023`
- Relative: `1 year ago`

### 6. "Check this URL: https://api.github.com/users/octocat"
Tool: HTTP Tester

Result:
```
✅ 200 OK
⏱️ 342ms

Headers: content-type: application/json
Body: {"login": "octocat", ...}
```

### 7. "Format this SQL"
```sql
SELECT id,name,email FROM users WHERE active=1 ORDER BY name
```

Tool: SQL Formatter

Result:
```sql
SELECT 
  id,
  name,
  email
FROM 
  users
WHERE 
  active = 1
ORDER BY 
  name
```

### 8. "Convert #FF5733 to RGB and HSL"
Tool: Color Converter

Result:
- HEX: `#FF5733`
- RGB: `rgb(255, 87, 51)`
- HSL: `hsla(11, 73%, 24%, 1.00)`
- CSS: `coral`

### 9. "Encode 'Hello World' to Base64"
Tool: Base64 Encoder

Result: `SGVsbG8gV29ybGQ=`

---

## Troubleshooting

### "Tools not showing up in Claude"
1. Check config file syntax (must be valid JSON)
2. Use absolute path, not relative
3. Restart Claude Desktop completely
4. Check that Python path is correct

### "ModuleNotFoundError"
```bash
# Install missing dependencies
pip install -r requirements.txt

# Verify installation
python test_tools.py
```

### "Server won't start"
```bash
# Check Python version (need 3.8+)
python --version

# Try running directly
python server.py
```

---

## File Structure

```
devkit-max/
├── server.py                  ← Main file
├── requirements.txt           ← Dependencies
├── test_tools.py             ← Test script
├── README.md                 ← Full docs
├── IMPLEMENTATION_SUMMARY.md ← Technical details
├── tools/                    ← 9 tools here
│   ├── json_formatter.py
│   ├── base64_tool.py
│   ├── uuid_generator.py
│   ├── jwt_decoder.py
│   ├── timestamp_tool.py
│   ├── hash_generator.py
│   ├── sql_formatter.py
│   ├── http_tester.py
│   └── color_converter.py
└── utils/
```

---

## Environment Variables (Optional)

No environment variables needed! Everything works out of the box.

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Test with `python test_tools.py`
3. ✅ Add to Claude Desktop config
4. ✅ Restart Claude
5. ✅ Start using!

---

## Need Help?

- **Full Docs:** See `README.md`
- **Technical Details:** See `IMPLEMENTATION_SUMMARY.md`
- **Quick Test:** Run `python test_tools.py`

---

## That's It! 🎉

You now have 9 professional developer tools integrated with Claude.

**Start using them!**

Examples:
- "Generate 10 UUIDs"
- "Format this JSON: {...}"
- "Check https://example.com"
- "Hash 'test' with MD5"
- "What's in this JWT?"

Enjoy! 🚀
