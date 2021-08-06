import requests

urls = [
    'https://link.springer.com/article/10.1007%2Fs002270000466',
    'https://link.springer.com/article/10.1007%2FBF00300577',
    'https://link.springer.com/article/10.1007/s11104-006-9033-3',
    'https://link.springer.com/article/10.1007%2FBF00340948',
    'https://link.springer.com/article/10.1007%2FBF02381090',
    'https://link.springer.com/article/10.1007/s10886-005-5288-z',  # no title
    'https://link.springer.com/article/10.1007%2Fs11692-009-9069-4?LI=true',
    'https://link.springer.com/article/10.1007%2Fs11692-009-9069-4',
    'https://link.springer.com/article/10.1007%2Fs00359-005-0063-8',
    'https://link.springer.com/article/10.1016%2FS1672-6529%2807%2960015-8',
    'https://link.springer.com/article/10.1007%2Fs00435-007-0031-7',
    'https://link.springer.com/article/10.1007%2FBF00204333',
    'https://link.springer.com/article/10.1007%2Fs00359-011-0658-1',
    'https://link.springer.com/chapter/10.1007/978-3-642-58001-7_21',
    'https://link.springer.com/article/10.1007%2Fs12010-008-8286-0',
    'https://link.springer.com/article/10.1007%2Fs10540-005-2887-4',
    'https://link.springer.com/article/10.1007/s00223-014-9915-y',  # extra whitespace in title
    'https://link.springer.com/article/10.1007%2Fs00253-008-1778-6',
    'https://link.springer.com/article/10.1023/A:1006245605705',
    'https://link.springer.com/article/10.1007%2Fs00359-008-0408-1',
    'https://link.springer.com/article/10.1007%2FBF02135966',
    'https://link.springer.com/article/10.1007%2FBF00660177',
    'https://link.springer.com/article/10.1016%2FS1672-6529%2811%2960018-8',  # title in German, subtitle in English
    'https://link.springer.com/article/10.1007%2FBF01049065',
    'https://link.springer.com/article/10.1007%2Fs00572-013-0529-4',
    'https://link.springer.com/article/10.1007%2Fs10533-005-4279-z',
    'https://link.springer.com/article/10.1007%2FBF03220386',
    'https://link.springer.com/article/10.1007%2Fs00442-006-0614-x',
    'https://link.springer.com/article/10.1007%2Fs00418-011-0904-1',
    'https://link.springer.com/article/10.1007%2Fs00226-005-0065-2',
    'https://link.springer.com/article/10.1007%2FBF01632907',
    'https://link.springer.com/article/10.1007/s003590050335',
    'https://link.springer.com/article/10.1023/A:1023334628751',
    'https://link.springer.com/article/10.1016/S1672-6529(10)60252-1',
    'https://link.springer.com/article/10.1007%2Fs00049-010-0054-2',
    'https://link.springer.com/article/10.1007/s00049-009-0036-4',  # title has extra whitespace
    'https://link.springer.com/article/10.1007/s11721-012-0067-2',
    'https://link.springer.com/article/10.1016%2FS1672-6529%2811%2960014-0',
    'https://link.springer.com/article/10.1007%2Fs10886-009-9707-4',
    'https://link.springer.com/article/10.1023/A:1006243032538',
    'https://link.springer.com/article/10.1140%2Fepje%2Fi2014-14109-y',
    'https://link.springer.com/article/10.1007%2Fs004250100576',
    'https://link.springer.com/article/10.1007%2Fs00425-010-1270-2',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2FBF01632816',
    'https://link.springer.com/article/10.1007%2Fs11160-009-9112-7',
    'https://link.springer.com/article/10.1007/BF02861079',
    'https://link.springer.com/article/10.1023%2FA%3A1006243032538',
    'https://link.springer.com/article/10.1007%2Fs00114-008-0472-y',
    'https://link.springer.com/article/10.1007%2Fs10164-010-0222-4',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2FBF01047102',
    'https://link.springer.com/article/10.1007%2Fs00442-012-2575-6',
    'https://link.springer.com/article/10.1007%2FBF00173949',
    'https://link.springer.com/article/10.1007%2FBF01279256',
    'https://link.springer.com/article/10.1007/BF03399449',
    'https://link.springer.com/article/10.1007%2Fs00435-012-0165-0',
    'https://link.springer.com/article/10.1007%2Fs11274-007-9345-3',  # title has extra whitespace
    'https://link.springer.com/article/10.1007/s00265-005-0019-6',
    'https://link.springer.com/article/10.1007/s00227-009-1266-2',
    'https://link.springer.com/article/10.1007/s11157-006-9118-8',
    'https://link.springer.com/chapter/10.1007%2F978-1-4757-9724-4_3',
    'https://link.springer.com/chapter/10.1007%2F978-1-4612-4018-1_14',
    'https://link.springer.com/article/10.1007%2Fs11837-010-0009-7',
    'https://link.springer.com/article/10.1007%2Fs10404-007-0163-6',
    'https://link.springer.com/article/10.1007/s00468-010-0417-x',
    'https://link.springer.com/article/10.1007%2Fs002210100774',
    'https://link.springer.com/article/10.1007%2FBF00344858',
    'https://link.springer.com/article/10.1023/A:1009223730317',
    'https://link.springer.com/chapter/10.1007/978-3-319-75596-0_10',
    'https://link.springer.com/article/10.1007/BF00438357',
    'https://link.springer.com/article/10.1007/s11258-014-0401-4',
    'https://link.springer.com/article/10.1672/0277-5212(2006)26[322:HTSSMV]2.0.CO;2',
    'https://link.springer.com/article/10.1007%2Fs00360-010-0470-1',
    'https://link.springer.com/article/10.1016%2FS1672-6529%2807%2960008-0',
    'https://link.springer.com/article/10.1007%2FBF00692371',
    'https://link.springer.com/article/10.1007%2FBF00610241',
    'https://link.springer.com/article/10.1007/s11829-007-9012-5',
    'https://link.springer.com/article/10.1023%2FA%3A1017506914063?LI=true',
    'https://link.springer.com/article/10.1007%2FBF00615085?LI=true',
    'https://link.springer.com/article/10.1007%2Fs00359-010-0522-8',  # title has extra whitespace
    'https://link.springer.com/article/10.1007/s00265-010-0911-6',
    'https://link.springer.com/article/10.1007/BF00384549',
    'https://link.springer.com/article/10.1007/s12600-010-0087-7',
    'https://link.springer.com/article/10.1007/BF00018716#page-1',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2Fs00425-001-0718-9',
    'https://link.springer.com/article/10.1007%2Fs000400050026',
    'https://link.springer.com/article/10.1007/BF03399488',
    'https://link.springer.com/article/10.1065/espr2004.08.213',
    'https://link.springer.com/article/10.1007%2Fs00425-008-0766-5',
    'https://link.springer.com/article/10.1023/A:1020537319805',
    'https://link.springer.com/article/10.1007%2Fs00114-005-0069-7',
    'https://link.springer.com/article/10.1007%2FBF00312146',
    'https://link.springer.com/article/10.1007%2Fs00114-009-0596-8',
    'https://link.springer.com/article/10.1007/s00332-002-0513-1',
    'https://link.springer.com/article/10.1007%2FBF00610867',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2Fs00425-002-0878-2?LI=true',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2Fs11829-007-9002-7',
    # 'https://www.springer.com/gp/book/9780412561603',  # should delete
    'https://link.springer.com/article/10.1007%2FBF00611243?LI=true',
    'https://link.springer.com/article/10.1007%2Fs00359-010-0556-y',
    'https://link.springer.com/article/10.1007/s004420050198',
    'https://link.springer.com/article/10.1007%2FBF00317628',
    'https://link.springer.com/article/10.1007%2Fs00049-011-0077-3',
    'https://link.springer.com/article/10.1007%2Fs004350050084',
    'https://link.springer.com/article/10.1007%2Fs007920050010',  # title has extra whitespace
    'https://rd.springer.com/chapter/10.1007/978-94-007-4441-7_2',
    'https://link.springer.com/article/10.1007/BF02112137',
    'https://link.springer.com/article/10.1007%2Fs00049-010-0059-x',  # title has extra whitespace
    'https://link.springer.com/article/10.1023/A:1006259402496',
    'https://link.springer.com/article/10.1007%2Fs11160-009-9155-9',
    'https://link.springer.com/article/10.1007%2Fs00253-002-0938-3',
    'https://link.springer.com/article/10.1007/s00227-001-0710-8',
    'https://link.springer.com/article/10.1007%2FBF00346343',
    'https://link.springer.com/article/10.1023/A:1022421515027',
    'https://link.springer.com/article/10.1007%2Fs00468-001-0153-3?LI=true',
    'https://link.springer.com/article/10.1023/A:1020587206351',
    'https://link.springer.com/chapter/10.1007/b98314',
    'https://link.springer.com/article/10.1007%2Fs10811-010-9505-y',  # title has extra whitespace
    'https://link.springer.com/article/10.1007%2Fs00227-004-1334-6'  # title has extra whitespace
]

base_api_url = "http://api.springernature.com/meta/v2/json"

for i, url in enumerate(urls):
    print(f'Article on line {i+5}: {url}')

    # get DOI *************************************
    doi = 'https://doi.org/'  # base of DOI
    doi += url.split('chapter/')[-1] if 'chapter' in url else url.split('article/')[-1]
    
    # fixing up some parts of the DOI url
    if 'LI=true' in doi:
        doi = doi.split('?LI=true')[0]
        
    elif '%28' in doi:
        doi = doi.replace('%2F', '/').replace('%28', '(').replace('%29', ')')
        
    elif '#' in doi:
        doi = doi.split('#')[0]
        
    # create API request *************************************
    doi_query = doi.split('.org/')[1]
    query = f'doi:"{doi_query}"'
    
    SPRINGER_API_KEY = '81cdeea18b51f346c4df14eb45dc4eda'  # not sure how to hide this
    params = {'q': query, 'api_key': SPRINGER_API_KEY}
    payload_str = "&".join("%s=%s" % (k, v) for k, v in params.items())  # don't understand this
    response = requests.get(base_api_url, params=payload_str)
    query_results = response.json()

    # get title *************************************
    title = query_results['records'][0]['title'].strip()

    # get abstract *************************************
    abstract = query_results['records'][0]['abstract'].strip()

    # get PDF *************************************
    pdf_link = query_results['records'][0]['url'][0]['value']  # only some articles give access to PDF!
    
    # for debugging
    print(f'DOI: {doi}')
    print(f'Title: {title}')
    print(f'Abstract: {abstract[:20]}...{abstract[-20:]}')
    print(f'PDF link: {pdf_link}\n')