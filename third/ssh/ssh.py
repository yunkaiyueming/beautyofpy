# coding=utf8

import paramiko

machines_data = {"182.254.230.16":"rayjoy", "139.199.159.211":"rayjoy"}
# ip = '182.254.230.16'
# username = 'rayjoy'
password = ''
port = 10220

# 设置记录日志
paramiko.util.log_to_file('ssh.log')

# 生成ssh客户端实例
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print "Starting"
private_key = "C:/Users/Rsy/rayjoy_ssh/id_rsa"

for ip,user in machines_data.items():
        #print k,v
        s.connect(ip, port, user, password,key_filename=private_key)
        stdin, stdout, stderr = s.exec_command('pushd /data/plattech/tmp; ls -l')
        print stdout.read()
s.close()
