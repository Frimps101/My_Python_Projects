#! open_multiple_tabs.py- A simple python script or snippet to open all the links of a website in mutiple tabs.
# That is each link in a new tab
# Project idea gotten from Automate The Boring Stuff With Python by Al Sweigart
# 
# Josephine Frimpomaa Kwakye
# 03/09/2020
# 00:40


from bs4 import BeautifulSoup
import requests, webbrowser

url = input("Please enter URL of website \n") #egs https://xkcd.com
request = requests.get(url)
requests_data = request.text
beau_soup = BeautifulSoup(requests_data)

# print(soup)

for conn in beau_soup.find_all("a"):
    webbrowser.open_new_tab(conn.get("href"))
