# --coding:UTF-8--
import paramiko
import so


hostname='192.168.1.21'
username=root
paramiko.util.log_to_File('syslogin.log')

ssh=paramiko.SSHClinet()
ssh.load_system_host_keys()
private_key = os.path.expanduser('/home/key/id_rsa')
key = paramiko.RSAKey.from_private_key_file(privatekey)


ssh.connect(hostname=hostname,username=username,pkey=key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()