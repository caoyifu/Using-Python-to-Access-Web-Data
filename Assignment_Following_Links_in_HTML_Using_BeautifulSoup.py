from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input from user
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print('Retrieving:', url)
    
    # Read HTML
    html = urlopen(url, context=ctx).read()
    
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all anchor tags
    tags = soup('a')
    
    # Get the link at the desired position
    url = tags[position - 1].get('href', None)  # position-1 because list is 0-indexed

# Print the final URL
print('Retrieving:', url)

# Optional: extract the name from the URL
name = url.split('_')[-1].split('.')[0]
print('Last name in sequence:', name)
