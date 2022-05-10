import os
import smtplib
from email.message import EmailMessage

EXAMPLE_ADDRESS = os.environ.get('EMAIL_USER')
EXAMPLE_PASSWORD = os.environ.get('EMAIL_PASS')
TEST_ADDRESS = os.environ.get('TEST_EMAIL')


class EmailSender:
    sender = EXAMPLE_ADDRESS
    receiver = TEST_ADDRESS

    @staticmethod
    def plain_text(message):
        msg = EmailMessage()
        msg['Subject'] = 'Test email using Python'
        msg['From'] = EmailSender.sender
        msg['To'] = EmailSender.receiver
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EmailSender.sender, EXAMPLE_PASSWORD)

            smtp.send_message(msg)

    @staticmethod
    def pdf(content, message):
        msg = EmailMessage()
        msg['Subject'] = 'OMG ITS PDF'
        msg['From'] = EmailSender.sender
        msg['To'] = EmailSender.receiver
        msg.set_content(content)

        files = message
        for pdf in files:
            with open(pdf, 'rb') as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(file_data, maintype='application', subtype='octet-string', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EXAMPLE_ADDRESS, EXAMPLE_PASSWORD)
            smtp.send_message(msg)


letter = 'Account properly engage belonging know ' \
         'seeing walls plan y unknown parish.'

file = ['Sergeev_Nikita.pdf']

Email = EmailSender()

Email.plain_text(letter)
