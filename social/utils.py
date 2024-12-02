# 工具库
"""
    邮件
"""
import smtplib
# 导入文件文本
from email.mime.text import MIMEText
# 导入邮件分类
from email.mime.multipart import MIMEMultipart


# 邮件发送类
class SendEmail:
    def __init__(self):
        # 初始化邮箱数据
        self.__sender_email = "SuperPinnacleOfficial@gmail.com"
        self.__sender_password = "lgnk pqzd ilxu pihb"
        self.__smtp_port = 587  # 对于Gmail
        self.__smtp_server = "smtp.gmail.com"  # 例如：smtp.gmail.com
        self.__smtp_port = 587

    def send_mail(self, _toUser, _title, _content):
        msg = MIMEMultipart()
        msg['From'] = self.__sender_email
        msg['To'] = _toUser
        msg['Subject'] = _title

        # 邮件正文内容
        msg.attach(MIMEText(_content, 'plain'))

        # 发送邮件
        try:
            server = smtplib.SMTP(self.__smtp_server, self.__smtp_port)
            server.starttls()
            server.login(self.__sender_email, self.__sender_password)
            text = msg.as_string()
            server.sendmail(self.__sender_email, _toUser, text)
            server.quit()
            print("邮件发送成功")
        except Exception as e:
            print(f"发送邮件时出错: {e}")


if __name__ == '__main__':
    s = SendEmail()
    _toUser = input("请输入邮件地址 : ")
    _title = input("请输入邮件标题 : ")
    _content = input("请输入邮件内容 : ")
    s.send_mail(_toUser, _title, _content)
