#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

import numpy.random as rn

genre = rn.choice([
    "success",
    "humor",
    "inspirational",
    "life-lessons",
    "life",
    "hope",
    "happiness",
    "wisdom",
    "stoicism",
    "stoic"
])

print(f"_tag_ {genre}")

url=f"https://www.goodreads.com/quotes/tag/{genre}?page={rn.randint(9)}"
response = requests.get(url)
response.raise_for_status()
html_contents = response.text

soup = BeautifulSoup(html_contents, 'html.parser')

quote_divs = soup.find_all('div', class_="quoteText")
quotes = [div.text.strip() for div in quote_divs]

# Filter out empty divs and extract the quote and the author.
quotes = [[div.text.strip().split('\n',2)[0], div.text.strip().split('\n',2)[2]]
          for div in quote_divs if div.text.strip()]


idx = rn.randint(len(quotes))


print(quotes[idx][0])
print(''.join(quotes[idx][1].split("\n")))
