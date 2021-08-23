import paramiko

router_ip = "127.0.0.1"
router_username = "root"
router_password = "123"
komut = "ls -al"
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip,port,router_username,router_password,timeout = 10)

stdin,stdout,stderr = ssh.exec_command(komut)
sonuc = stdout.read()
print(sonuc.decode("utf-8"))

ssh.close()