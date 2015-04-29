#! /usr/bin/env python
# coding:utf-8
import os, sys
import pexpect

# 实现的还有问题 

# 用pexpect执行ssh，查看远程uptime和df -h看硬盘状况
def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    #ssh.logfile=sys.stdout
    r = ''
    try:
        while 1:
            #i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
            i = ssh.expect('.*assword: ')  # password or Password
            #i = ssh.expect(['Password:', 'password:', pexpect.EOF, pexpect.TIMEOUT])  # not ok
            if i == 0:
                print("sendline passwd")
                ssh.sendline(passwd)
                break
            elif i == 1:
                ssh.sendline('yes')
    except pexpect.EOF:
        print("#### EOF")
        ssh.close()
    else:
        r = ssh.read()
        ssh.expect(pexpect.EOF)
        ssh.close()
    return r

hosts = '''
192.168.14.217:root:123456:df -h,uptime
192.168.14.215:root:zxcvbnm:df -h,uptime
'''

for host in hosts.split("\n"):
    if host:
        print(host.split(":"))
        ip, user, passwd, cmds = host.split(":")
        for cmd in cmds.split(","):
            print "######    %s run:%s    ######" % (ip, cmd)
            print ssh_cmd(ip, user.strip(), passwd.strip(), cmd)
