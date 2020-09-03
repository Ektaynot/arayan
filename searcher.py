import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    mail_content='''mech market bot'''
    sender_address = 'xx@gmail.com'
    sender_pass = 'xxxxx'
    receiver_address = 'xxxx@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = title
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def check_new():
    URL="https://www.reddit.com/r/mechmarket/new/"
    headers={"User-Agent":"Mozilla/5.0"}
    page=requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content, "html.parser")
    title=soup.find(attrs={"_eYtD2XCVieq6emjKBH3m"}).get_text()
    title=str(title)
    title2=title.lower()
    aranan=str("tangerine")
    aranan2=str("tangerines")
    if aranan in title2 or aranan2 in title2:
        print("Finded")
        send_mail()

while True:
    check_new()
