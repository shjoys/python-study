import requests
from bs4 import BeautifulSoup
from json import loads as parseJson


def get_naver_product_info():
    result = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=비타민&oquery=비타민&tqi=hVdBvdp0YihsshKrnKhssssstr0-481166")

    soup = BeautifulSoup(result.text, 'html.parser')

    product_info = soup.find_all('div', {'class':'product_info'})[0:8]

    print(product_info)

    # product_info > a > text
    # product_info > div > class : price > text
    for product in product_info:
        product_name = product.find('a', {'class':'title'}).text
        product_price = product.find('div', {'class':'price'}).text
        # print("name : "+product_name)
        # print("price : "+product_price)
        # print(">>>>>")


get_naver_product_info()


def get_naver_shopping_product_info():
    result = requests.get(
        "https://search.shopping.naver.com/search/all?query=비타민&bt=-1&frm=NVSCPRO",
        params={"query": "비타민", "bt": "-1", "frm": "NVSCPRO"},
        headers = {'user-agent': 'my-app/0.0.1'}
    )

    soup = BeautifulSoup(result.text, 'html.parser')

    response = soup.find('script', {'id':'__NEXT_DATA__'})

    # product_list = parseJson(response)
    print(response)


# get_naver_shopping_product_info()