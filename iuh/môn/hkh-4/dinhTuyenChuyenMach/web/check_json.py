import paramiko, json, sys

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.2.128', username='root', password='eve')
stdin, stdout, stderr = client.exec_command("cat $(ls -t /root/*.json | head -n 1)")
output = stdout.read().decode('utf-8')
try:
    data = json.loads(output)
    for dev in data.get('devices', []):
        print(f"--- {dev['name']} ---")
        for cmd in dev.get('config', []):
            print(cmd)
except Exception as e:
    print("Error parsing JSON:", e)
    print("Output was:", output)
