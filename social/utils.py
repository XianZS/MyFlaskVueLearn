# 工具库
"""
    邮件
"""
import smtplib
from email.mime.message import MIMEMessage
# 导入文件文本
from email.mime.text import MIMEText
# 导入邮件分类
from email.mime.multipart import MIMEMultipart


# 邮件发送类
class SendEmail:
    def __init__(self):
        # 初始化邮箱数据
        # 邮箱
        self.__email = "3820105232@qq.com"
        # 密钥
        self.__password = "lkcyswstfgbmccba"

    def send_mail(self, _toUser, _title, _content):
        # 构建邮件体
        msg = MIMEMultipart()
        # 邮件标题
        msg['Subject'] = _title
        # 邮件发送者
        msg['From'] = self.__email
        # 邮件接收者
        msg['To'] = _toUser
        # 构建邮件内容
        part = MIMEText('测试邮件', 'plain', 'utf-8')
        msg.attach(part)
        # 建立链接对象
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登陆邮箱
        s.ehlo()
        s.login(self.__email, self.__password)

        # 发送邮件
        s.sendmail(self.__email, _toUser, msg.as_string())
        # 关闭邮件
        s.quit()


if __name__ == '__main__':
    s = SendEmail()
    s.send_mail("2038704030@qq.com", "测试一下", "脚本测试")
