import requests
from parsel import Selector

URL = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
BASE_URL = "http://books.toscrape.com/catalogue/"

response = requests.get(URL)
selector = Selector(text=response.text)

title = selector.css(".product_main h1::text").get()
price = selector.css(".product_main .price_color::text").re_first(
    r"\d+\.\d{2}"
)
description = selector.css("#product_description ~ p::text").get()
image_url = BASE_URL + selector.css(".item img::attr(src)").get()
avaliable_info = selector.css(".availability::text").extract()

if description.endswith(" ...more"):
    description = description[: -len(" ...more")]

avaliable = "".join([n for n in avaliable_info[1] if n.isdigit()])

print(title, price, description, image_url, avaliable, sep=",")
