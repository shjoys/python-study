import requests
from bs4 import BeautifulSoup
from json import loads as parseJson


def get_today_discount(): 
    result = requests.get(
        "https://www.coupang.com/np/recommend/feeds",
        params={"nextFeedsToken": "Ci0IGHIpZmVlZC0wYmQ0M2JiNmIwMjg0OWRkODhkYTExYjEzNTcwODhhOC1mYmkKNghrcjJmZWVkLTBiZDQzYmI2YjAyODQ5ZGQ4OGRhMTFiMTM1NzA4OGE4LWd3X3Byb21vdGlvbhABGiVmZWVkLTBiZDQzYmI2YjAyODQ5ZGQ4OGRhMTFiMTM1NzA4OGE4"}
    )

    print(result)

get_today_discount()