"""
The last usage of this script used DOIs from negative biomimicry papers.
These DOIs were obtained from running the script get_negative_paper_dois.py.

Input a CSV file with DOIs to get back a CSV file with the DOI and other paper info from the API.
"""

import requests
import pandas as pd
import time

# since 10,000 negative biomimicry papers is a lot, I ran this code in chunks of 500 (so each run takes 25 minutes):
# doi_df = pd.read_csv('negative_paper_dois.csv', index_col=0)
# doi_df = doi_df.iloc[500:1000]  # second 500 rows
# doi_df = doi_df.iloc[1000:1500]  # third 500 rows


four_col_df = pd.read_csv('../sophia-data/new_biomimicry_papers.csv')
doi_df = four_col_df.filter(['doi']).iloc[178:]  # in this scenario, I only wanted to get paper info for rows 178 onward.

# clean DOIs so they have a consistent format
doi_df['doi'] = doi_df['doi'].str.replace('http://dx.doi.org/', '', regex=True)  # specify regex=True for future updates
doi_df['doi'] = doi_df['doi'].str.replace('https://doi.org/', '', regex=True)
doi_df['doi'] = doi_df['doi'].str.replace('doi:', '', regex=True)
doi_df['doi'] = doi_df['doi'].str.strip()

base_url = 'https://api.semanticscholar.org/v1/paper/'


def request_function(doi):
	time.sleep(3)  # since SS limits 100 requests/5 minutes = 100 requests/300 secs = 1 request/3 secs
	r = requests.get(f'{base_url}{doi}', timeout=10)
	
	if r.status_code == 200:
		response = r.json()
		# so that we don't try to access a value from a key that doesn't exist in the API response
		return [response.get('url', ''), response.get('title', ''), response.get('abstract', ''), response.get('is_open_access', ''), response.get('venue', '')]

	return ['', '', '', '', '']  # returning [] gives errors, so return empty strings instead!


# this splits the 5 API responses (even if one of the responses has an empty string) into 5 new columns in the dataframe
api_df = pd.DataFrame(doi_df['doi'].apply(request_function).values.tolist(), columns=['url', 'title', 'abstract', 'is_open_access', 'journal_name'])

# clean up the column indexes so the concatenated dataframes display correctly
doi_df.reset_index(drop=True, inplace=True)
api_df.reset_index(drop=True, inplace=True)

df_final = pd.concat([doi_df, api_df], axis=1)  # create a dataframe with a doi column + other paper info columns
df_final['is_biomimicry'] = 'True'  # add column to the end of the df with a constant value of 'True'

df_final.to_csv('raw_press_release_paper_info.csv')

