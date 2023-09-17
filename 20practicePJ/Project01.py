import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_sender = 'quocthinhleviet@gmail.com'
email_password =  'deih uvwi qxkt ffqy' # Đặt mật khẩu của bạn ở đây
email_receiver ='levietquocthinh@gmail.com'
subject = 'Subject of the email'
body = 'This is the email body.'

# Tạo một đối tượng MIMEMultipart
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject

# Thêm nội dung của email

# Khởi tạo kết nối SSL đến máy chủ SMTP của Gmail
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    try:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print('Email could not be sent. Error:', str(e))
