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

url = "https://www.zalando.lv/lauren-ralph-lauren-cape-georgette-dress-kokteilkleitaballisu-kleita-mascarpone-cream-l4221c1c2-a11.html"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all("p", {"class": "_0xLoFW u9KIT8 vSgP6A"})

if myLinks:
  price_raw = myLinks[0].text.strip()
  price_cleaned = ''.join(filter(str.isdigit, price_raw))
  price_float = float(price_cleaned) / 100

  print("Current Price:", price_float)
  desiredPrice = 240.0  # Set the desired price as a float for comparison

  if price_float < desiredPrice:  # Compare prices
    email= f"The price for your product has dropped! Your desired price for this item was {desiredPrice}. The new price {price_float}.\n Link to the product: {url}"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = "griva.santa@gmail.com"
    msg['From'] = username
    msg['Subject'] = "News about price"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg
  else:
    print("Price is not lower than the desired price.")
    s.quit()
else:
  print("Price element not found on the page.")