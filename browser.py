import sys
import os
import os.path
import requests
from bs4 import BeautifulSoup
from colorama import Fore

directory_name = sys.argv[1]
saved_websites = []


def create_directory(directory_name):
    try:
        os.mkdir(str(directory_name))
    except FileExistsError:
        pass


def parse_web(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ''
    tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']
    for t in soup.find_all(tags):
        if t.name == 'a':
            text = Fore.BLUE + text + t.get_text() + '\n'
        else:
            text = text + t.get_text() + '\n'
    return text


create_directory(directory_name)

while True:
    website = input()
    if website == 'exit':
        break
    else:
        if "https://" not in website:
            https_website = "https://" + website
        else:
            https_website = website
            website = website.replace("https://", "")
        if website in saved_websites:
            with open(f"./{directory_name}/{website}", "w", encoding='UTF-8') as f:
                print(f.read())
        else:
            try:
                resp = requests.get(https_website)
                text_web = parse_web(resp)
                with open(f"./{directory_name}/{website}", "w", encoding='UTF-8') as f:
                    f.write(text_web)
                saved_websites.append(website)
                print(text_web)
            except requests.exceptions.RequestException as e:
                print("Error: Incorrect URL")
