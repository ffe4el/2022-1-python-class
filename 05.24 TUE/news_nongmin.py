import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.nongmin.com"
    res=requests.get("http://www.nongmin.com/news/NEWS/NEW/list")
    soup=BeautifulSoup(res.content, "html.parser")
    res.close()

    # print(soup)
    find_str = soup.find("div", attrs={'class':'card_type03'})
    print(find_str)

if __name__ == "__main__":
    main()