import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") # Get the web page data.
    soup = BeautifulSoup(r.text, "html.parser") # Parsing web page data with html.parser.
    sel = soup.select("div.title a") # Get all <a> tags in <div class="title"></div> in HTML tags.
    for s in sel :
        print(s["href"], s.text)
    #print(r.text) # print HTML

    return 0

main()