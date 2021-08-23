
import paramiko

sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.load_system_host_keys()
sshClient.connect('192.168.106.128',22,'dmtgl','Passsword')

ftp_client= sshClient.open_sftp()
try:
     #Yerelden uzak makineye dosya yükleme
     ftp_client.put('C:\\Users\\lenovo\\Desktop\\subuntu_file.txt','/home/dmtgl/ubuntu_file')

     #Uzak makineden dosya indirme
     ftp_client.get('/home/dmtgl/subuntu_file','C:/Users/lenovo/Desktop/ubuntu.txt',None)
except Exception as e:
    print(str(e))
ftp_client.close()
sshClient.close()

