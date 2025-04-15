# + Web Scraping with Requests and BeautifulSoup
# Web scraping is the process of extracting data from websites. It can be done using various libraries in Python, such as Requests and BeautifulSoup.
# Requests is used to make HTTP requests, while BeautifulSoup is used to parse HTML and XML documents.

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/aulas/aula190_site/index.html'
response = requests.get(url)
raw_html = response.text  # Get the raw HTML content of the page
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')  # Parse the HTML content using BeautifulSoup
# Now you can use BeautifulSoup methods to extract data from the parsed HTML


# print(raw_html)  # Print the raw HTML content
# print(parsed_html.prettify())  # Print the parsed HTML content in a readable format
# print(parsed_html.title)  # Print the title of the page
print(parsed_html.title.text)  # Print the title of the page
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading is not None:  # Check if the element was found
    # print(top_jobs_heading.text)  # Print the text of the top jobs heading
    article = top_jobs_heading.parent  # Get the parent element of the heading
    if article is not None:  # Check if the parent element was found
        for p in article.select('p'):
            print(p.text)
