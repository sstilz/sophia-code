import requests, time, random
from bs4 import BeautifulSoup

urls = [
 # 'https://jeb.biologists.org/content/213/2/288',
 # 'https://jeb.biologists.org/content/213/22/3920',
 # 'https://jeb.biologists.org/content/210/4/553',
 # 'https://jeb.biologists.org/content/215/22/3965',
 # 'https://jeb.biologists.org/content/214/13/2215.short',
 # 'https://jeb.biologists.org/content/213/3/502',
 # 'https://jeb.biologists.org/content/208/19/3655',
 # 'https://jeb.biologists.org/content/210/13/2244',
 # 'https://jeb.biologists.org/content/220/18/3260',
 # 'https://jeb.biologists.org/content/152/1/41',
 # 'https://jeb.biologists.org/content/213/2/339',
 # 'https://jeb.biologists.org/content/216/7/1152',
 # 'https://jeb.biologists.org/content/210/17/3075',
 # 'https://jeb.biologists.org/content/213/23/4092',
 # 'https://jeb.biologists.org/content/159/1/165',
 # 'https://jeb.biologists.org/content/215/5/785',
 # 'https://jeb.biologists.org/content/210/8/1378',
 # 'https://jeb.biologists.org/content/31/4/491',  # maybe weird?
 # 'https://jeb.biologists.org/content/38/3/659', # maybe weird?
 # 'https://jeb.biologists.org/content/214/12/2047',
 # 'https://jeb.biologists.org/content/211/16/2647',
 # 'https://jeb.biologists.org/content/213/8/1235',
 # 'https://jeb.biologists.org/content/207/18/3131',
 # 'https://jeb.biologists.org/content/198/9/1829',
 # 'https://jeb.biologists.org/content/217/8/1263',
 # 'https://jeb.biologists.org/content/213/17/2967',
 # 'https://jeb.biologists.org/content/210/13/2231',
 # 'https://jeb.biologists.org/content/213/7/1115',
 # 'https://jeb.biologists.org/content/214/23/3960',
 # 'https://jeb.biologists.org/content/207/2/211',
 # 'https://jeb.biologists.org/content/212/17/2835',
 # 'https://jeb.biologists.org/content/217/12/2193',
 # 'https://jeb.biologists.org/content/207/26/4633',
 # 'https://jeb.biologists.org/content/213/20/3457',
 # 'https://jeb.biologists.org/content/210/13/2253',
 # 'https://jeb.biologists.org/content/214/10/1699',
 # 'https://jeb.biologists.org/content/215/7/1151',
 # 'https://jeb.biologists.org/content/221/24/jeb192492',
 # 'https://jeb.biologists.org/content/212/13/1990',
 # 'https://jeb.biologists.org/content/206/6/1059',
 # 'https://jeb.biologists.org/content/214/22/3850',
 # 'https://jeb.biologists.org/content/215/9/1502',
 # 'https://jeb.biologists.org/content/205/5/651',
 # 'https://jeb.biologists.org/content/208/8/1469',
 # 'https://jeb.biologists.org/content/214/6/915',
 # 'https://jeb.biologists.org/content/212/19/3184',
 # 'https://jeb.biologists.org/content/213/19/3364',
 # 'https://jeb.biologists.org/content/208/18/3609.abstract',
 # 'https://jeb.biologists.org/content/208/16/3075',
 # 'https://jeb.biologists.org/content/213/10/1731',
 # 'https://jeb.biologists.org/content/210/15/2593',
 # 'https://jeb.biologists.org/content/207/7/1127',
 # 'https://jeb.biologists.org/content/192/1/45',
 # 'https://jeb.biologists.org/content/202/23/3315',
 # 'https://jeb.biologists.org/content/194/1/263.short',
 # 'https://jeb.biologists.org/content/210/19/3319',
 # 'https://jeb.biologists.org/content/210/14/2548',
 # 'https://jeb.biologists.org/content/212/21/3448',
 # 'https://jeb.biologists.org/content/208/8/1435',
 # 'https://jeb.biologists.org/content/216/23/4473',
 # 'https://jeb.biologists.org/content/55/2/385.article-info',
 'https://jeb.biologists.org/content/212/21/3499',
 'https://jeb.biologists.org/content/212/21/3440',
 'https://jeb.biologists.org/content/213/2/249',
 'https://jeb.biologists.org/content/69/1/127',  # maybe weird?
 'https://jeb.biologists.org/content/209/5/938',
 'https://jeb.biologists.org/content/210/13/2300',
 'https://jeb.biologists.org/content/213/15/2665',
 'https://jeb.biologists.org/content/206/23/4217',
 'https://jeb.biologists.org/content/210/15/2593.long',
 'https://jeb.biologists.org/content/193/1/233',
 'https://jeb.biologists.org/content/213/20/3416',
 'https://jeb.biologists.org/content/214/13/2175',
 'https://jeb.biologists.org/content/218/22/3551',
 'https://jeb.biologists.org/content/152/1/243.short',
 'https://jeb.biologists.org/content/215/12/2072',
 'https://jeb.biologists.org/content/jexbio/201/5/673.full.pdf',
 'https://jeb.biologists.org/content/214/17/2988',
 'https://jeb.biologists.org/content/21/3-4/97',
 'https://jeb.biologists.org/content/213/7/1092',
 'https://jeb.biologists.org/content/163/1/1.short',
 'https://jeb.biologists.org/content/208/23/4467',
 'https://jeb.biologists.org/content/213/5/673',
 'https://jeb.biologists.org/content/216/11/1961',
 'https://jeb.biologists.org/content/202/23/3305',
 'https://jeb.biologists.org/content/213/3/469',
 'https://jeb.biologists.org/content/213/10/1697',
 'https://jeb.biologists.org/content/209/2/202',
 'https://jeb.biologists.org/content/206/20/3581',
 'https://jeb.biologists.org/content/212/24/4002',
 'https://jeb.biologists.org/content/214/5/848',
 'https://jeb.biologists.org/content/208/8/1445',
 'https://jeb.biologists.org/content/135/1/431',
 'https://jeb.biologists.org/content/56/1/195.short',
 'https://jeb.biologists.org/content/159/1/419',
 'https://jeb.biologists.org/content/203/18/2757',
 'https://jeb.biologists.org/content/211/5/717',
 'https://jeb.biologists.org/content/207/24/4249',
 'https://jeb.biologists.org/content/134/1/313',
 'https://jeb.biologists.org/content/211/21/3421',
 'https://jeb.biologists.org/content/215/4/578',
 'https://jeb.biologists.org/content/207/7/1063',
 'https://jeb.biologists.org/content/209/4/748',
 'https://jeb.biologists.org/content/jexbio/203/23/3585.full.pdf',
 'https://jeb.biologists.org/content/113/1/447.abstract',
 'https://jeb.biologists.org/content/215/23/4217',
 'https://jeb.biologists.org/content/212/13/1981',
 'https://jeb.biologists.org/content/212/24/4010',
 'https://jeb.biologists.org/content/69/1/127.abstract',
 'https://jeb.biologists.org/content/202/20/2727.long',
 'https://jeb.biologists.org/content/200/3/557',
 'https://jeb.biologists.org/content/214/4/521',
 'https://jeb.biologists.org/content/88/1/1',
 'https://jeb.biologists.org/content/212/3/429',
 'https://jeb.biologists.org/content/199/4/1005',
 'https://jeb.biologists.org/content/215/8/1247',
 'https://jeb.biologists.org/content/201/11/1681.short'
]

for index, url in enumerate(urls):

    print(f'Article on line {index+66}: {url}')

    # setup
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(random.randint(30, 60))

    # get title
    # title = soup.find('h1', class_='wi-article-title article-title-main').text.strip()

    # get doi
    # doi = self.soup.find('span', class_='citation-doi').text

    # doi = soup.find('div', class_='citation-doi').find('a').get('href')
    # print(f"DOI: {doi}")
    # doi = doi[5:].strip()

    # get abstract
    # given self.html, get the abstract
    abstract = soup.find('section', class_='abstract').text.strip()
    print("Abstract: " + abstract[:50] + "..." + abstract[-50:] + "\n")

    # get full doc link
    # given self.html, get the full_doc_link
    # pdf_link = soup.find('a', class_='article-pdfLink')['href']
    # pdf_link = 'https://journals.biologists.com' + pdf_link