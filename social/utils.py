# 工具库
"""
    邮件
"""
import random
import smtplib
# 导入文件文本
from email.mime.text import MIMEText
# 导入邮件分类
from email.mime.multipart import MIMEMultipart

# 随机码的存储
from database import r


# 邮件发送类
class SendEmail:
    """
        邮箱创建类
    """

    def __init__(self):
        # 初始化邮箱数据
        self.__sender_email = "SuperPinnacleOfficial@gmail.com"
        self.__sender_password = "lgnk pqzd ilxu pihb"
        self.__smtp_port = 587  # 对于Gmail
        self.__smtp_server = "smtp.gmail.com"  # 例如：smtp.gmail.com

    def send_mail(self, _toUser: str, _title: str, _content: str):
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


class CreateCode:
    """
        验证码创建
    """

    # 初始化操作
    def __init__(self, abc=True, length=4):
        if abc:
            self.__code = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            self.__code = "0123456789"
        self.__length = length

    # 生成逻辑
    def return_code(self):
        return "".join([random.choice(self.__code) for _ in range(self.__length)])


class SaveCode:
    """
        验证码存储类
    """

    def __init__(self):
        self.r = r

    def save_code(self, userEmail: str, code: str, lifeTime: int) -> bool:
        """
            原子操作：要么都执行，要么都不执行
            必须将存储和设置生命周期一起执行
        """
        # 使用 UserEmail 作为键，将 code 存储到 Redis 中
        # r.setex(邮箱，生命周期，验证码)
        return self.r.setex(userEmail, lifeTime, code)

    def show_code(self, userEmail: str) -> str:
        return self.r.get(userEmail)


if __name__ == '__main__':
    s = SendEmail()
    msg = CreateCode(False, 6).return_code()
    _email = input("请输入邮箱 : ")
    s.send_mail(_email, "验证码", "您社交平台的验证码为 : " + msg)
    SaveCode_class = SaveCode()
    print(SaveCode_class.save_code(_email, msg, 300))
    print(SaveCode_class.show_code(_email))
