import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from slacker import Slacker

def send_mail():
    mail_content="Found"
    sender_address = 'xxx.com'
    sender_pass = 'xxx'
    receiver_address = 'xxx@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = (title)
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def slack():
    slack=Slacker('bot api')
    message=(title)
    slack.chat.post_message('#general',message)
    print("slack send")


URL="https://www.reddit.com/r/mechmarket/new/"
headers={"User-Agent":"xxxx"}
page=requests.get(URL, headers=headers)
soup=BeautifulSoup(page.content, "html.parser")
title=soup.find(attrs={"_eYtD2XCVieq6emjKBH3m"}).get_text()
title=str(title)
while True:
    URL="https://www.reddit.com/r/mechmarket/new/"
    headers={"User-Agent":"xxxx"}
    page=requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content, "html.parser")
    title=soup.find(attrs={"_eYtD2XCVieq6emjKBH3m"}).get_text()
    title=str(title)
    title2=title.lower()
    print(title2)
    aranan=str("tangerine")
    aranan2=str("tangerines")
    aranan3=str("giveaway")
    aranan4=str("c3")
    aranan5=str("[giveaway]")
    aranan6=str("[gb]")
    if aranan in title2 or aranan2 in title2 or aranan3 in title2 or aranan4 in title2 or aranan5 in title2 or aranan6 in title2:
        send_mail()
        slack()
        time.sleep(30)
    else:
        continue
