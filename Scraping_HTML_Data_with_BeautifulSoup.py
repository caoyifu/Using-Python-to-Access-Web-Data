
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for the URL
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup('span')

# Extract numbers and compute sum
numbers = [int(tag.contents[0]) for tag in tags if 'comments' in tag.get('class', [])]
print('Sum:', sum(numbers))
