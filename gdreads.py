import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_goodreads_books(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = []
    authors = []
    ratings = []

    for book_title in soup.select('a.bookTitle span'):
        titles.append(book_title.text.strip())

    for author_name in soup.select('span[itemprop="author"] span[itemprop="name"]'):
        authors.append(author_name.text.strip())

    for rating_span in soup.select('span.minirating'):
        try:
            rating_value = float(rating_span.text.strip().split()[0])
            ratings.append(rating_value)
        except ValueError:
            print("Error converting rating to float:", rating_span.text.strip())


    min_length = min(len(titles), len(authors), len(ratings))
    titles = titles[:min_length]
    authors = authors[:min_length]
    ratings = ratings[:min_length]

    book_data = {'Title': titles, 'Author': authors, 'Rating': ratings}
    return pd.DataFrame(book_data)


def main():
    url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=1'
    book_df = scrape_goodreads_books(url)  # Create the DataFrame
    print("Scraped data:")
    print(book_df)  # Print the DataFrame
    book_df.to_csv('book_data.csv', index=False)  # Save DataFrame to CSV file
    print("Scraped data saved to 'book_data.csv'")

if __name__ == "__main__":
    main()
