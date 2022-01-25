import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


def bb_check():
    url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
    r = requests.get(url, headers=headers)
    if r.text.find("data-button-state=\"SOLD_OUT\"") != -1:
        print("Best Buy: Sold Out")
    else:
        print("Best Buy: In Stock")


def wm_check():
    url = "https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/363472942"
    r = requests.get(url, headers=headers)
    if r.text.find("Walmart</a>") == -1:
        print("Walmart: Sold Out")
    else:
        print("Walmart: In Stock")


def tar_check():
    url = "https://www.target.com/p/playstation-5-console/-/A-81114595"
    r = requests.get(url, headers=headers)
    if r.text.find("product not available</div>") != -1:
        print("Target: Sold Out")
    else:
        print("Target: In Stock")

bb_check()
wm_check()
tar_check()
