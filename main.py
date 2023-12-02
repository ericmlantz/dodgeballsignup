from imap_tools import MailBox
from imap_tools import AND, OR, NOT
from bs4 import BeautifulSoup
import requests
import re
from config import USERNAME, PASSWORD
import urllib.parse

# Get date, subject and body len of all emails from INBOX folder
# get list of email bodies from INBOX folder
with MailBox('imap.gmail.com').login(USERNAME, PASSWORD, 'INBOX') as mailbox:
  bodies = [msg.html for msg in mailbox.fetch(AND(from_='dodgeball@bigapplerecsports.com'), reverse = True, limit=1)]

email_contents = BeautifulSoup(str(bodies),"html.parser")

# print(soup)
links = []
for link in email_contents.findAll('a', attrs={'href': re.compile("^https://")}):
  links.append(link.get('href'))
# links # in this you will have to check the link number starting from 0. 
result = links[0]

# Decode Url so you can put in browser and go to it
decoded_url = urllib.parse.unquote(result)
# print(decoded_url)

# Regex to only get the part of that url that is a link for google form
form_url = re.findall("https://docs.google.com/forms.*viewform",decoded_url)
print("Google Form URL:",form_url)

# Get contents of the page with the form on the internet
webpage = requests.get(form_url)
soup = BeautifulSoup(webpage.content,"html.parser")


# output = open('test.csv', 'wb')
# output.write(resp.content)
# output.close()