import schedule, time, os, smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

quotes = []
f = open("quotes.txt", "r")
quotes = eval(f.read())
f.close()
randomQuote = random.choice(quotes)

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
  email = randomQuote
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host = server, port = port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg['To'] = "griva.santa@gmail.com"
  msg['From'] = username
  msg['Subject'] = "Random quote of the day for me from me"
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg)
  del msg

sendMail()

def printMe():
  print("⏰")

schedule.every(2).minutes.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(60)