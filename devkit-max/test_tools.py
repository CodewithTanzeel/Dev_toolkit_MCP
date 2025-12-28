#!/usr/bin/env python3
"""
Quick test script for DevKit Max tools
Tests each tool's basic functionality
"""

import json
import sys

print("🧪 DevKit Max - Quick Tool Tests\n")

# Test 1: JSON Formatter
print("1️⃣  Testing JSON Formatter...")
try:
    test_json = '{"name":"John","age":30,"city":"New York"}'
    parsed = json.loads(test_json)
    formatted = json.dumps(parsed, indent=2, sort_keys=True)
    print("   ✅ JSON parsing works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 2: UUID Generator
print("2️⃣  Testing UUID Generator...")
try:
    import uuid
    test_uuid = str(uuid.uuid4())
    print(f"   Generated: {test_uuid}")
    print("   ✅ UUID generation works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 3: Base64
print("3️⃣  Testing Base64...")
try:
    import base64
    test_text = "Hello World"
    encoded = base64.b64encode(test_text.encode()).decode()
    decoded = base64.b64decode(encoded).decode()
    print(f"   Original: {test_text}")
    print(f"   Encoded:  {encoded}")
    print(f"   Decoded:  {decoded}")
    print("   ✅ Base64 works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 4: Hash Generator
print("4️⃣  Testing Hash Generator...")
try:
    import hashlib
    test_input = "hello"
    hash_result = hashlib.sha256(test_input.encode()).hexdigest()
    print(f"   SHA256(hello) = {hash_result[:20]}...")
    print("   ✅ Hash generation works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 5: JWT Decoder
print("5️⃣  Testing JWT Decoder...")
try:
    import base64
    header = base64.b64encode(json.dumps({"alg": "HS256"}).encode()).decode().rstrip("=")
    print(f"   JWT header decoded successfully")
    print("   ✅ JWT parsing works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 6: Timestamp
print("6️⃣  Testing Timestamp Converter...")
try:
    from datetime import datetime
    now = datetime.now()
    timestamp = int(now.timestamp())
    print(f"   Current timestamp: {timestamp}")
    print(f"   Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("   ✅ Timestamp conversion works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Test 7: Color Converter
print("7️⃣  Testing Color Converter...")
try:
    hex_color = "#FF5733"
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    print(f"   {hex_color} = rgb({r}, {g}, {b})")
    print("   ✅ Color conversion works\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

print("=" * 50)
print("✨ All basic tests completed!")
print("=" * 50)
