from bs4 import BeautifulSoup
import re
import os


def get_doi_from_saved_html(file):
	soup = BeautifulSoup(file, 'html.parser')
	doi = ''
	
	# search the HTML for DOIs displayed as hrefs
	for a in soup.find_all('a', href=True):
		link = a['href']
		
		if 'https://www.doi.org/' in link:
			doi = link.split('https://www.doi.org/')[1]
			break
	
	# search the HTML for DOIs displayed as strings
	if len(doi) == 0:
		print('Using regex method.')
		
		pattern = re.compile("\W10.\d{4,9}/[-._;()/:A-Za-z0-9]+\W")
		matches = soup.find_all(string=pattern)
		
		if matches:
			first_match = matches[0]
			first_match_info = re.search(pattern, first_match)
			
			indices_tuple = first_match_info.span()  # (301, 326)
			index_1 = indices_tuple[0]
			index_2 = indices_tuple[1]
			
			doi = first_match[index_1:index_2]
			
			if '/10.' in doi:
				doi = doi.split('10.')[0]
	
	return doi


########################################################################################################################
# to use this function:
folder_path = f'{os.getcwd()}/downloaded_html_files'  # the folder which contains all your downloaded HTML files

for file_name in os.listdir(folder_path):
	if file_name.endswith('.html'):
		file = f'{folder_path}/{file_name}'
		print(f"DOI: {get_doi_from_saved_html(open(file, 'r'))}\n")
