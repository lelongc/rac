import paramiko, time, json
with open('app.py') as f: code = f.read()
import re
match = re.search(r'EVE_MASTER_SCRIPT = r?\"\"\"(.*?)\"\"\"', code, re.DOTALL)
eve_master = match.group(1)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.2.128', username='root', password='eve')

sftp = client.open_sftp()
sftp.put('d:/folder/rac/iuh/môn/hkh-4/dinhTuyenChuyenMach/lab/lab1/Bai5_lab1.json', '/root/Bai5_lab1.json')
with sftp.file('/root/autoeve_master.py', 'w') as f: f.write(eve_master)
sftp.close()

lab_name = 'Bai5_Static_Routing'
print('Stopping and wiping...')
client.exec_command(f'/opt/unetlab/wrappers/unl_wrapper -a stop -T 0 -F /opt/unetlab/labs/{lab_name}.unl')
time.sleep(3)
client.exec_command(f'/opt/unetlab/wrappers/unl_wrapper -a wipe -T 0 -F /opt/unetlab/labs/{lab_name}.unl')
time.sleep(2)

print('Building...')
stdin, stdout, stderr = client.exec_command('python3 /root/autoeve_master.py build /root/Bai5_lab1.json')
print(stdout.read().decode())
print(stderr.read().decode())

print('Starting...')
client.exec_command(f'/opt/unetlab/wrappers/unl_wrapper -a start -T 0 -F /opt/unetlab/labs/{lab_name}.unl')
time.sleep(45)

print('Pushing config...')
stdin, stdout, stderr = client.exec_command('python3 /root/autoeve_master.py push /root/Bai5_lab1.json')
print(stdout.read().decode())

print('Waiting for routing to converge (30s)...')
time.sleep(30)

print('Verifying...')
stdin, stdout, stderr = client.exec_command('python3 /root/autoeve_master.py verify /root/Bai5_lab1.json')
print(stdout.read().decode())

print('Checking report...')
stdin, stdout, stderr = client.exec_command(f'cat /root/report_{lab_name}.txt')
print(stdout.read().decode()[:1000])
