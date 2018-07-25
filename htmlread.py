from bs4 import BeautifulSoup as BS
import urllib.request
import certifi
import image_scraper
with urllib.request.urlopen("https://www.deere.com/en/index.html", cafile=certifi.where()) as url:
	html = url.read()
	soup = BS(html,'html.parser')
	#for link in soup.find_all('a'):
		#print(link.get('href'))
	#for link in soup.find_all('div'):
		#print(link.attrs['class'].['industry-img'])
	imglinks = []
	for imglink in soup.find_all('img'):
		print(imglink.attrs['src'])
		imglinks.append(imglink.attrs['src'])
	print(imglinks)
	image_scraper.scrape_images('https://github.com')	