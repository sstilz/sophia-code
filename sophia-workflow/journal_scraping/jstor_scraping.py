import requests, time, random
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
 'https://www.jstor.org/stable/1309104 seq=1#metadata_info_tab_contents',
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
 'https://www.jstor.org/stable/2388261?origin=crossref&seq=1',
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
 'https://www.jstor.org/stable/2388261?seq=1',
 'https://www.jstor.org/stable/1447745?origin=crossref&seq=1',
 'https://www.jstor.org/stable/1446299?origin=crossref&seq=1',
 'https://www.jstor.org/stable/1565147?origin=crossref&seq=1'
]

for index, url in enumerate(urls):
    print(f'Article on line {index+4}: {url}')

    # setup
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(random.randint(30, 60))
    
    # get title
    title = soup.find(class_='title-font').text.strip()
    
    # get doi
    doi = ''
    doi_tag = soup.find(class_='doi')
    if doi_tag:
        doi = doi_tag.get('href')
        
    # get abstract
    abstract = soup.find(class_='summary-paragraph').text.strip()
    
    # for debugging
    print(f'Title: {title}\nDOI: {doi}\nAbstract: {abstract[:30]}...{abstract[-30:]}\n\n')