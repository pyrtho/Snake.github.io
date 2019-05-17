import os
from lxml import html
import requests
import pyperclip
from bs4 import BeautifulSoup

hello = input("Website: ")
page = requests.get(hello)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
wow = soup.find_all(class_="username")
print(wow)
print(w)
