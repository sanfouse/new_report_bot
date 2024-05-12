from email.mime.image import MIMEImage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import settings


class EmailSender:
    def __init__(self, login, password, smtp_server="smtp.mail.ru", smtp_port=587):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_message(self, body, recipient, subject, photo_data):
        message = MIMEMultipart()
        message["From"] = self.login
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        if photo_data:
            with open(photo_data, "rb") as f:
                image_data = f.read()
                image = MIMEImage(image_data)
                image.add_header('Content-Disposition', 'attachment', filename='photo.jpg')
                message.attach(image)

        return message

    def send_email(self, body, recipient=settings.EMAIL_ADDRESS, subject="Жалоба", photo_data=None):
        message = self.create_message(body, recipient, subject, photo_data)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.login, self.password)
            text = message.as_string()
            server.sendmail(self.login, recipient, text)


sender = EmailSender(
    login=settings.EMAIL_LOGIN,
    password=settings.EMAIL_PASSWORD
)