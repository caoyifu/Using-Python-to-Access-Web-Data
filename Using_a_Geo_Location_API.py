from urllib.request import urlopen
from urllib.parse import urlencode
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for location
location = input("Enter location: ")

# Encode parameters for URL
params = {'q': location}
url = "http://py4e-data.dr-chuck.net/opengeo?" + urlencode(params)

print("Retrieving", url)
data = urlopen(url, context=ctx).read()
print("Retrieved", len(data), "characters")

# Parse JSON
js = json.loads(data)

# Extract plus_code
plus_code = js['features'][0]['properties']['plus_code']
print("Plus code", plus_code)
