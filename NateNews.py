from urllib import response
import requests
from bs4 import BeautifulSoup


titles = []

def get_nate_new(q, page):
    result = requests.get(
        "https://news.nate.com/search",
        params={
            "q": q,
            "ps": "7d",
            "page": page,
        }
    )
    soup = BeautifulSoup(result.text, 'html.parser')
    news_contents = soup.find("div", {"id": "newsContents"})
    search_list = news_contents.find("ul", {"class", "search-list"})
    items = search_list.find_all("li", {"class", "items"})                  # find_all : list로 return
    
    for item in items:
        title = item.find("span", {"class", "tit"}).text
        titles.append(title)


def get_nate_news_100():

    for i in range(7):
        get_nate_new("금리", i)

    del titles[100:105]

    
get_nate_news_100()
# print(len(titles))
# print(titles)

def count_increase_titles():
    increase_keyword = ["상승", "급증", "인상", "밀물", "최고"]
    
    count = 0
    for title in titles:
        for keyword in increase_keyword:
            if(title.find(keyword) > -1):
                count = count + 1
                break

    print(count)
        

count_increase_titles()


def count_decrease_titles():
    decrease_keyword = ["인하", "하락", "급락", "썰물", "최저"]

    count = 0
    for title in titles:
        for keyword in decrease_keyword:
            if(title.find(keyword) > -1):
                count = count + 1
                break

    print(count)

count_decrease_titles()