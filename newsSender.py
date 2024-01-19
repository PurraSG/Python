import schedule
import time
import os
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

password = os.environ['mailPassword']
username = os.environ['mailUsername']

url = "https://www.shecandoit.lv/#jaunumi"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all("h3", {"class": "heading-11"})

keywords = ["ai", "python", "javascript"]

relevant_news = []
for link in myLinks:
    link_text = link.text
    textWords = link.text.split()
    hasKeyword = False

    for word in textWords:
        if word.lower() in keywords:
            hasKeyword = True
            relevant_news.append(link_text)

def sendMail():
    if relevant_news:
        email = "<br>".join(relevant_news)  # Join news articles with line breaks for email body

        server = "smtp.gmail.com"
        port = 587
        s = smtplib.SMTP(host=server, port=port)
        s.starttls()
        s.login(username, password)

        msg = MIMEMultipart()
        msg['To'] = "griva.santa@gmail.com"
        msg['From'] = username
        msg['Subject'] = "News from SheCanDoIT"
        msg.attach(MIMEText(email, 'html'))

        s.send_message(msg)
        del msg
        s.quit()

        print("Email sent successfully 💌")
    else:
        print("No relevant news found")

def printMe():
    print("⏰")

schedule.every(2).minutes.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(60)
