import requests
from bs4 import BeautifulSoup
from json import loads as parseJson


def get_cm_pick_product_list(): 
    result = requests.get(
        "https://www.danawa.com/main/ajax/getCmPickProductList.ajax.php",
        params={"type": "large"},
        headers = {'cookie': 'OAX=O7vNW2LL/iAACZuk; ADWEBCOUNTER_UUID2=e8d5b5e5-1543-202a-adba-89dcda455f24; ACEUACS=1655991117403152410; ACEFCID=UID-62CBFE229C08C88191853AD4; ACEUCI=1; danawa-loggingApplicationClient=ab8bcee4-0167-4155-bc93-be3546a13e21; _gcl_au=1.1.328955369.1657536035; _gid=GA1.2.1197264505.1657536035; au_id=009cca290511fbba-79ec3d8618136efe3b9-6ae9; _uni_id=7ec1bc24-9c72-4ec5-ba7b-aa64fa362ba9; AUFAH6A45867192252=1657536034689852571|2|1657536034689852571|1|1657536033852152571; check_uni_send=1; _ga_XWC0NNEPX2=GS1.1.1657536044.1.0.1657536113.60; _gcl_aw=GCL.1657536117.Cj0KCQjwlK-WBhDjARIsAO2sErT16LH8BmMw31JfWykK86W1jlk2pOWQ7lLzEQEAgIcqkvnd47NIFQ8aAoAcEALw_wcB; _ga_287B75YQDL=GS1.1.1657536035.1.1.1657536118.0; _ga=GA1.2.1257687712.1657536035; _gac_UA-37762359-14=1.1657536118.Cj0KCQjwlK-WBhDjARIsAO2sErT16LH8BmMw31JfWykK86W1jlk2pOWQ7lLzEQEAgIcqkvnd47NIFQ8aAoAcEALw_wcB; _INSIGHT_CK_8203=128e980f896ea1e2610b91312824fb1d_36033|8566481199276210f87091312824fb1d_36033:1657538156000; wcs_bt=s_3b3fb74948b1:1657536356'}
    )

    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup)


get_cm_pick_product_list()