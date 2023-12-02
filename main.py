from imap_tools import MailBox
from imap_tools import AND, OR, NOT
from bs4 import BeautifulSoup
import requests
import re

# Get date, subject and body len of all emails from INBOX folder
# get list of email bodies from INBOX folder
with MailBox('imap.gmail.com').login('ericmlantz@gmail.com', 'yxmn gpdp vafz ohqs', 'INBOX') as mailbox:
    bodies = [msg.html for msg in mailbox.fetch(AND(subject='your email subject'), reverse = True)]
   

# soup = BeautifulSoup(str(bodies))
# links = []
# for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
#     links.append(link.get('href'))
# links # in this you will have to check the link number starting from 0. 

# result = links[5] # mine was 5th
# result


# resp = requests.get(result)

# output = open('test.csv', 'wb')
# output.write(resp.content)
# output.close()