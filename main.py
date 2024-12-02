import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 配置电子邮件参数
sender_email = "SuperPinnacleOfficial@gmail.com"
# sender_password = "YangHaiTao3135"
sender_password = "lgnk pqzd ilxu pihb"
receiver_email = "3135989009@qq.com"
smtp_server = "smtp.gmail.com"  # 例如：smtp.gmail.com
smtp_port = 587  # 对于Gmail


def send_email():
    # 创建邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "每日报告"

    # 邮件正文内容
    body = "这是您的每日报告。"
    msg.attach(MIMEText(body, 'plain'))

    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"发送邮件时出错: {e}")


send_email()
