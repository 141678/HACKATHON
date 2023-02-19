# -*- coding: UTF-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup

movie_url = 'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular'

def download_page(url):
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}

	data = requests.get(url, headers = headers).content
	return data

def paser_html(html):
	soup = BeautifulSoup(html, 'lxml')
	df = pd.DataFrame(columns=['FilmName'])
	span_elements = soup.find_all("span", {"data-qa": "discovery-media-list-item-title"})
	for x in range(1,6):
		data_dict={'FilmName':span_elements[x].text.strip()}
		df=df.append(data_dict, ignore_index=True)
		df.to_csv('C:\\Users\\Spark\\Desktop\\Hackathon\\Advanced_Version.json', index=False)
def main():
#print(paser_html(download_page(movie_url)))
	paser_html(download_page(movie_url))
#
if __name__ == '__main__':
	main()
