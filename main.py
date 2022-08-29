#IMPORTS
from email.message import EmailMessage
from email.utils import formataddr
import smtplib
from imports import *

#CONTACT SCREEN
class ContactPage(MDScreen):
    Builder.load_file('contact.kv')
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def send_message(self, name, sender_email, message):
        email = open('logDetails.txt').readlines()[0].strip()
        password = open('logDetails.txt').readlines()[1].strip()
        msg = EmailMessage()
        msg['Subject'] = "New Contact Form Enquiry"
        msg['To'] = email
        msg['From'] = formataddr(name.text, sender_email.text)
        msg.set_content(f"Hi, my name is {name}.\n{message}")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)
        name.text = ""
        sender_email.text = ""
        message.text = ""

#MAIN APP
class MainApp(MDApp):
    def build(self):
        return ContactPage()

#RUN
if __name__ == '__main__':
    MainApp().run()