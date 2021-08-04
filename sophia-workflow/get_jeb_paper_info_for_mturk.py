"""
Note: This code uses segments of get_paper_info_using_ss_api and clean_paper_info_data.py.
This code can be used as a reference for how you might utilize the contents of the 2 scripts mentioned above.
"""

import requests
import time
import pandas as pd
import numpy as np

# TODO - read input CSV & delete index column
df = pd.read_csv('jeb_paper_info.csv', index_col=0)
df = df.sample(700)  # run 700 out of the 10,000 rows so that there will safely be 500 ready-to-be-posted HITs

# TODO - remove the 'http://dx.doi.org' from all DOI links
df['doi'] = df['doi'].str.replace('http://dx.doi.org/', '', regex=True)  # specify regex=True for future updates

# TODO - clean long PubMed IDs
# https://www.codegrepper.com/code-examples/python/python+split+values+in+cell
df['pmid'] = df['pmid'].str.split('\n', n=1, expand=True)

# TODO - drop all empty rows
df.replace('', np.nan, inplace=True)  # this ensures all rows will have DOIs for the API requests
df.dropna(inplace=True)

# TODO - get title, abstract, and open access info from SS API
# https://stackoverflow.com/questions/23690284/pandas-apply-function-that-returns-multiple-values-to-rows-in-pandas-dataframe
base_url = 'https://api.semanticscholar.org/v1/paper/'
query = '("The Journal of experimental biology"[Journal]) AND (("2002/01/01"[Date - Publication] : "2020/10/10"[Date - Publication]))'


def request_function(doi):
	time.sleep(3)  # wait 5 seconds between every request
	response = requests.get(f'{base_url}{doi}?{query}',
							timeout=10).json()  # this will fail if request stalls for more than 20 secs
	responses = []
	
	# so that we don't try to access a value from a key that doesn't exist in the API response
	if 'title' in response:
		responses.append(response['title'])
	if 'abstract' in response:
		responses.append(response['abstract'])
	if 'is_open_access' in response:
		responses.append(response['is_open_access'])
		
	return responses


# https://stackoverflow.com/questions/40924332/splitting-a-list-in-a-pandas-cell-into-multiple-columns
# https://stackoverflow.com/questions/39050539/how-to-add-multiple-columns-to-pandas-dataframe-in-one-assignment

# split the 3 API responses into 3 new columns
api_df = pd.DataFrame(df['doi'].apply(request_function).values.tolist(), columns=['api_title', 'api_abstract', 'api_is_open_access'])

# clean up the column indexes so the concatenated dataframes display correctly
df.reset_index(drop=True, inplace=True)
api_df.reset_index(drop=True, inplace=True)

df_concat = pd.concat([df, api_df], axis=1)

# TODO - remove 'ABSTRACT'/'SUMMARY' text from the beginning of cells in 'api_abstract' column
# https://stackoverflow.com/questions/45447848/check-for-words-from-list-and-remove-those-words-in-pandas-dataframe-column
remove_words = ['ABSTRACT ', 'SUMMARY ']
pat = r'\b(?:{})\b'.format('|'.join(remove_words))
df_concat['api_abstract_cleaned'] = df_concat['api_abstract'].str.replace(pat, '', regex=True)
df_filtered = df_concat[df_concat['api_is_open_access']]  # only include rows where is_open_access=True

# TODO - save cleaned file
df_filtered.to_csv('cleaned_jeb_data.csv')  # this file can be found in the sophia-data folder
