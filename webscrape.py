# import bs4 and urlib packages and scrape the link we need to collect data from.
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# Checking how many HTML containers are present in the link
containers = page_soup.findAll("div", { "class": "_3O0U0u"})
print(len(containers))

print(soup.prettify(containers[0]))

# Checking first item in page
container = containers[0]
print(container.div.img["alt"])

# Checking price of this item
price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
print(price[0].text)

# Rating of item
ratings = container.findAll("div", {"class": "niH0FQ"})
print(ratings[0].text)

# Creating a CSV file and store all item with their name, price and rating 
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)

# Reviewing the CSV we created
for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text
    print("Product_Name:"+ product_name)
    print("Price: " + price)
    print("Ratings:" + rating)
