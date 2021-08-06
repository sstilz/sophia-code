import pyautogui
import time
from bs4 import BeautifulSoup

urls = [
	'https://www.jstor.org/stable/24874508?seq=1',
	'https://www.jstor.org/stable/2399893?origin=crossref&seq=1',
	'https://www.jstor.org/stable/23436271?seq=1',
	'https://www.jstor.org/stable/3706047?seq=1',
	'https://www.jstor.org/stable/3882752?seq=1',
	'https://www.jstor.org/stable/1442721?origin=crossref&seq=1',
	'https://www.jstor.org/stable/2410663?origin=crossref',
	'https://www.jstor.org/stable/2260070?origin=crossref&seq=1',
	'https://www.jstor.org/stable/176791?seq=1',
	'https://www.jstor.org/stable/1309104?seq=1#metadata_info_tab_contents',  # I had to tweak this url
	'https://www.jstor.org/stable/1538612?seq=1',
	'https://www.jstor.org/stable/2388496?seq=1',
	'https://www.jstor.org/stable/2441335?seq=1',
	'https://www.jstor.org/stable/27855549?seq=1',
	'https://www.jstor.org/stable/2388018?seq=1',
	'https://www.jstor.org/stable/2406628?seq=1#metadata_info_tab_contents',
	'https://www.jstor.org/stable/2388599?seq=1',
	'https://www.jstor.org/stable/2835178?seq=1',
	'https://www.jstor.org/stable/1366197?seq=1#metadata_info_tab_contents',
	'https://www.jstor.org/stable/1542085?seq=1',
	'https://www.jstor.org/stable/2388261?origin=crossref&seq=1',  # duplicate
	'https://www.jstor.org/stable/2259780?origin=crossref&seq=1',
	'https://www.jstor.org/stable/23384962?seq=1#page_scan_tab_contents',
	'https://www.jstor.org/stable/3762235?seq=1',
	'https://www.jstor.org/stable/1565146?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1447748?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1565367?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1564398?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1310784',
	'https://www.jstor.org/stable/10.1086/678955?seq=1',
	'https://www.jstor.org/stable/2398919?seq=1',
	'https://www.jstor.org/stable/4159449?seq=1',
	'https://www.jstor.org/stable/1443948?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1438539?seq=1',
	# 'https://www.jstor.org/stable/2388261?seq=1', # duplicate
	'https://www.jstor.org/stable/1447745?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1446299?origin=crossref&seq=1',
	'https://www.jstor.org/stable/1565147?origin=crossref&seq=1'
]


def save_files():
	time.sleep(2)  # the time it takes to open up Chrome
	
	for url in urls:
		pyautogui.hotkey('command', 't')  # for every new website, open a new tab
		
		pyautogui.typewrite(f'{url}\n')  # type url and hit enter
		time.sleep(5)  # max time it takes for a site to load
		
		pyautogui.hotkey('command', 's')  # save the website
		time.sleep(2)  # it takes time to enter in the file name!
		
		url_fragment = url.split('/')[-1].split('?')[0]  # ex, 2480681
		pyautogui.typewrite(f'{url_fragment}.html\n')  # name of file saved


def scrape_html():
	for index, url in enumerate(urls):
		url_fragment = url.split('/')[-1].split('?')[0]  # ex, 2480681
		html = open(f'/Users/sophiastiles/Downloads/{url_fragment}.html', "r").read()
		soup = BeautifulSoup(html, 'html.parser')
		
		# get DOI
		doi_tag = soup.find(class_='doi')
		doi = doi_tag.get('href') if doi_tag else ''
		
		# extra - get title, abstract, and PDF link
		title = soup.find(class_='title-font').text.strip()
		abstract = soup.find(class_='summary-paragraph').text.strip()
		
		# is not open access
		# pdf_class = soup.find(class_='primary-access')
		# pdf_link = 'https://jstor.org' + pdf_class['href']
		
		print(f'Article {index + 1}: {url}\nDOI: {doi}\nTitle: {title}\nAbstract: {abstract[:30]}...{abstract[-30:]}\n')


scrape_html()
