import urllib.request
import sys

try:
    with urllib.request.urlopen("http://localhost:8080/data/test1.json", timeout=3) as resp:
        print("Status code:", resp.status)
        print("Test 1 length:", len(resp.read()))
except Exception as e:
    print("Server not responding:", e)
