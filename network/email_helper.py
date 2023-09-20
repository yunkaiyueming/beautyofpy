# coding=utf8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from email.mime.image import MIMEImage

sender = 'xx'
pwd = 'xx'
receivers = ['xx@qq.com']
smt_server = 'smtp.exmail.qq.com:25'

def send_emai_with_attach():
        message = MIMEMultipart()
        message['From'] = Header("自动化报警", 'utf-8')
        message['To'] = Header("报警箱", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是我的Python 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="data.txt"'
        message.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="data.txt.bk"'
        message.attach(att2)

        try:
                server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
                server.login(sender, pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()  # 关闭连接

                print "邮件发送成功"
        except smtplib.SMTPException:
                print "Error: 无法发送邮件"


def send_mail_with_img_view():
        message = MIMEMultipart()
        message['From'] = Header("自动化报警", 'utf-8')
        message['To'] = Header("报警箱", 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是我的Python 邮件发送测试……', 'html', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="data.txt"'
        message.attach(att1)

        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">报警链接</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 指定图片为当前目录
        fp = open('test.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)
        try:
                server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
                server.login(sender, pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(sender, receivers, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()  # 关闭连接

                print "邮件发送成功"
        except smtplib.SMTPException:
                print "Error: 无法发送邮件"

def common_mail():
        ret = True
        try:
                msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
                msg['From'] = formataddr(["自动化报警账户", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['To'] = formataddr(["接收账户", receivers])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['Subject'] = "配置信息错误"  # 邮件的主题，也可以说是标题

                server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
                server.login(sender, pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
                server.sendmail(sender, receivers, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                ret = False
        return ret

#ret = mail()
# if ret:
#         print("邮件发送成功")
# else:
#         print("邮件发送失败")

#send_emai_with_attach()

send_mail_with_img_view()
