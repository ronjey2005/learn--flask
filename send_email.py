import smtplib
from email.mime.text import MIMEText
import smtplib

class EmailModule:
    def __init__(self, email, height):
        self.email = email
        self.height = height

    def send_email(self, avg_height, total_sample):
        from_email = "rjusuf@gmail.com"
        from_password = "sometrix"
        to_email = self.email

        subject = "Height Data"
        message = f"{self.email}'s height : <strong>{self.height}</strong>cm. Average height is {avg_height} out of {total_sample} samples"

        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['To'] = to_email
        msg['From'] = from_email

        gmail = smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)