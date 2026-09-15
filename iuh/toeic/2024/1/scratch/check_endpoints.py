import urllib.request

for endpoint in ["/", "/index.html", "/data/test1.json", "/data/test10.json", "/data/vocab_bank.json", "/assets/audio/test2/part1.mp3", "/assets/images/test2/q1.png"]:
    url = f"http://127.0.0.1:8080{endpoint}"
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req) as resp:
        print(f"{endpoint:35s} -> HTTP {resp.status} (Content-Length: {resp.headers.get('Content-Length')})")

print("All endpoints tested OK!")
