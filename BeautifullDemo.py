import requests
from bs4 import BeautifulSoup
import time
import random

url = 'https://example.com'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print all links
links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])


# Add a new paragraph to the body
new_tag = soup.new_tag('p')
new_tag.string = 'This is a new paragraph.'
soup.body.append(new_tag)

# Remove all script tags
for script in soup.find_all('script'):
    script.decompose()

print(soup.prettify())
