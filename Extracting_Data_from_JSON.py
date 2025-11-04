import urllib.request
import json

# Prompt for URL
url = input("Enter URL: ")

# Read data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse JSON
info = json.loads(data)

# Extract comment counts and compute the sum
total = 0
for item in info['comments']:
    total += int(item['count'])

print("Sum of counts:", total)
