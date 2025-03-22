import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# User-Agent to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# Function to scrape books with retry logic
def scrape_books():
    books = []

    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        attempt = 0
        success = False

        while attempt < 3 and not success:  # Retry up to 3 times
            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()  # Raise error for HTTP failures (4xx, 5xx)
                success = True  # If request succeeds, break retry loop
            except requests.exceptions.RequestException as e:
                print(f"⚠️ Error on page {page}: {e} (Retry {attempt+1}/3)")
                attempt += 1
                time.sleep(2)  # Wait before retrying

        if not success:
            print(f"❌ Skipping page {page} after 3 failed attempts")
            continue  # Skip this page if it still fails

        soup = BeautifulSoup(response.text, 'html.parser')

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p")["class"][1]  # Star rating
            availability = book.find("p", class_="instock availability").text.strip()
            books.append([title, price, rating, availability])

    return books

# Save data to CSV
if __name__ == "__main__":
    book_data = scrape_books()
    
    if book_data:
        save_path = r"C:\Users\saniy\OneDrive\Documents\Practice\CodeAlpha Data Analytics\books_data1.csv"
        df = pd.DataFrame(book_data, columns=["Title", "Price", "Rating", "Availability"])
        df.to_csv(save_path, index=False)
        print(f"✅ Scraping completed! Data saved to {save_path}")
    else:
        print("❌ No data scraped!")
