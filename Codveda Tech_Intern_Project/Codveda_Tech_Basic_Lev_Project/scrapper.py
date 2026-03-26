import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# loop through all pages
for page in range(1, 51):

    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text.replace("£", "")

        rating = book.p["class"][1]

        availability = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "Title": title,
            "Price (£)": price,
            "Rating": rating,
            "Availability": availability
        })

    print(f"Page {page} scraped")

    time.sleep(1)   # polite delay


# convert to dataframe
df = pd.DataFrame(all_books)

# save dataset
df.to_csv("books_full_dataset.csv", index=False)

print("Scraping complete")
print("Total books scraped:", len(df))