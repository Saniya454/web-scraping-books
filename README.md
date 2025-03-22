This project is a web scraper that extracts book details (title, price, rating, and availability) from Books to Scrape.
It processes all 50 pages of the website and saves the data into a CSV file for further analysis.
Uses BeautifulSoup for parsing and requests for fetching webpage data
How It Works:
1️. The script loops through all 50 pages of the website.
2️. It sends HTTP requests to fetch the page content.
3️. Uses BeautifulSoup to extract book title, price, rating, and availability.
4️. Stores the extracted data into a Pandas DataFrame.
5️. Saves the data into a CSV file for further analysis.
