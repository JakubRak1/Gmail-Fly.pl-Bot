from email.message import EmailMessage
import ssl
import smtplib
from logins.logins import EMAIL_ADDRESS, EMAIL_APP_PASSWORD, EMAIL_RECEIVER


def Gmail(hotel_name, price, date):
    cap_hotel_name = hotel_name.upper()
    subject: str = 'Alarm from BOT!! PRICE HAS CHANGED'
    body: str = f'''The price for {cap_hotel_name} has changed and now its {price} in {date}.'''
    message = EmailMessage()
    message['From'] = EMAIL_ADDRESS
    message['To'] = EMAIL_RECEIVER
    message['Subject'] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_RECEIVER, message.as_string())
