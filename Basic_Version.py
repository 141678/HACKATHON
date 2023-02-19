# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

movie_url = 'https://www.rottentomatoes.com/m/antman'

def download_page(url):
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}

	data = requests.get(url, headers = headers).content
	return data

def paser_html(html):
	soup = BeautifulSoup(html, 'lxml')
	title = soup.find('div', {'class': 'movie_synopsis'}).text.strip()

	return title

def main():
	print(paser_html(download_page(movie_url)))
title=paser_html(download_page(movie_url))
with open("C:\\Users\\Spark\\Desktop\\Hackathon\\Basic_Version.txt","w") as file:
    file.write(title)



if __name__ == '__main__':
	main()
