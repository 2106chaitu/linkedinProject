import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def get_soup(url):
    """GET a URL and return a BeautifulSoup object."""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, "html.parser")


def scrape_page(url):
    """
    Scrape one catalog page.
    Returns: list[dict] with books on that page, and the absolute URL to the next page (or None)
    """
    soup = get_soup(url)
    books_data = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"].strip()

        price_text = book.select_one(".price_color").text.strip()  # e.g. '£51.77'
        price = price_text.replace("£", "").strip()

        rating_text = book.p.get("class", ["", "Zero"])[1]  # ['star-rating', 'Three'] -> 'Three'
        rating_int = RATING_MAP.get(rating_text, 0)

        product_rel_url = book.h3.a["href"]
        product_url = urljoin(url, product_rel_url)

        books_data.append({
            "title": title,
            "price": price,
            "rating_text": rating_text,
            "rating_int": rating_int,
            "product_url": product_url
        })

    # Find next page (if exists)
    next_tag = soup.select_one("li.next a")
    next_url = urljoin(url, next_tag["href"]) if next_tag else None

    return books_data, next_url


def main():
    start_url = BASE_URL
    current_url = start_url
    total_books = 0
    page_no = 1

    with open("books.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "price", "rating_text", "rating_int", "product_url"]
        )
        writer.writeheader()

        while current_url:
            print(f"Scraping page {page_no}: {current_url}")
            books, next_url = scrape_page(current_url)

            for row in books:
                writer.writerow(row)
            total_books += len(books)

            current_url = next_url
            page_no += 1

            # Be polite to the server
            time.sleep(0.5)

    print(f"✅ Done! Scraped {total_books} books into books.csv")


if __name__ == "__main__":
    main()
