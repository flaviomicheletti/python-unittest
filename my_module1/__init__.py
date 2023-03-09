# my_module.py
import smtplib


def send_email(from_addr, to_addr, subject, body):
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login("user@gmail.com", "password")
    message = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"
    smtp_server.sendmail(from_addr, to_addr, message)
    smtp_server.quit()
