import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in ['test1.json', 'test2.json', 'test3.json']:
    url = f"http://localhost:8080/data/{t}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
        print(f"{t}: loaded {len(data['questions'])} questions successfully over HTTP!")
