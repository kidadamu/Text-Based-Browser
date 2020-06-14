from typing import TextIO
import sys
import os
import os.path


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


websites_withCom = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}
websites_noCom = {'bloomberg': bloomberg_com, 'nytimes': nytimes_com }
directory = sys.argv[1]
saved = []


def track_back(stack, website_name=None, pop=False):
    if website_name in websites_noCom or website_name in websites_withCom:
        stack.append(website_name)
        print(stack)
    if pop:
        if len(stack) >= 2:
            return stack.pop(-2)
        else:
            return None


def create_directory(directory_name):
    try:
        os.mkdir(str(directory_name))
    except FileExistsError:
        pass


def save_website(directory_name, website_name):
    if website_name in websites_withCom:
        website_name = website_name.replace(".com", "")
    with open(f"./{directory_name}/{website_name}", "w") as f:
        f.write(websites_noCom[website_name])


def track_back(stack, website_name=None, pop=False):
    if website_name in websites_noCom or website_name in websites_withCom:
        stack.append(website_name)
        print(stack)
    if pop:
        if stack:
            return stack.pop(-2)
        else:
            return None


create_directory(directory)

while True:
    website = input()
    if website == 'exit':
        break
    elif website == 'back':
        back_website = track_back(saved, None, True)
        if back_website:
            back_website = back_website.replace(".com", "")
            print(websites_noCom[back_website])
    elif website in websites_withCom:
        print(websites_withCom[website])
        track_back(saved, website)
        website_clean = website.replace(".com", "")
        if not os.path.exists(f"./{directory}/{website_clean}"):
            save_website(directory, website_clean)
    elif website in websites_noCom:
        print(websites_noCom[website])
        track_back(saved, website)
    else:
        print("Error: Incorrect URL")




