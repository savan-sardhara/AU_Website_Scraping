import requests
from bs4 import BeautifulSoup

url = 'https://atmiyauni.ac.in/facultylist/computer-science-information-technology/97'
response = requests.get(url)
robots_txt = response.text
with open('facultytest.html', 'w', encoding='utf-8', errors='ignore') as file:
    file.write(robots_txt)

with open('facultytest.html', 'r', encoding='utf-8', errors='ignore') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

for faculty in soup.find_all('b'):
    faculty_name = faculty.get_text().replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_') + '.txt'
    with open(faculty_name, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(faculty.get_text())