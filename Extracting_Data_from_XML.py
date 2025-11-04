import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
# Convert text to integers and sum
nums = [int(count.text) for count in counts]

print('Count:', len(nums))
print('Sum:', sum(nums))

