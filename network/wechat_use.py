#coding=utf8
import itchat
import time

# 每 3 秒循环执行
if __name__ == '__main__':
        itchat.auto_login()
        while True:
                try:
                        msg = raw_input("输入要发送的信息：")
                        itchat.send(msg, toUserName='tt')
                        print msg
                except KeyboardInterrupt:
                        itchat.send("send over", toUserName='tt')
                        print "send over"
                        break
