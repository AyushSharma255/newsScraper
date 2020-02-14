# Import requests
import requests

newsRequest = requests.get("https://news.google.com")  # Request to Google News
text = newsRequest.text  # text from Google News
# Import bs4's bs
from bs4 import BeautifulSoup

nySoup = BeautifulSoup(text, "lxml")  # soup of Google News
headlines = nySoup.find_all('a', {'class': 'DY5T1d'})  # Find all links with this class

for line in headlines:
    print(line.contents[0])  # Print the text inside of them all
