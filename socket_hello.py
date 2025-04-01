import paramiko

nao_ip = '192.168.15.121'  # Replace with your NAO's IP
nao_user = 'nao'
nao_password = 'nao'     # default password unless changed

command = '/usr/bin/python -c "from naoqi import ALProxy; ALProxy(\'ALTextToSpeech\', \'127.0.0.1\', 9559).say(\'Hello, how are you?\')"'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to NAO at {nao_ip} via SSH...")
    ssh.connect(nao_ip, username=nao_user, password=nao_password)
    print("✅ Connected via SSH. Sending speak command...")

    stdin, stdout, stderr = ssh.exec_command(command)
    stdout.channel.recv_exit_status()  # Wait for command to finish

    print("🗣️ NAO said: Hello, how are you?")
except Exception as e:
    print("❌ Error:", e)
finally:
    ssh.close()
    print("🔒 SSH connection closed.")
