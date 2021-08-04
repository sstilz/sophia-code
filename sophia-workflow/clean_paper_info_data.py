import pandas as pd
import numpy as np

# read input CSV & delete index column
df = pd.read_csv('jeb_paper_info.csv', index_col=0)  # can change the name of the input CSV accordingly

# if the df you're working with is the result of multiple merged CSVs, the indices can be messed up. This is a fix!
df.reset_index(drop=True, inplace=True)

# ensures all DOIs have the same format of '10.1002/esp.4933', rather than 'http://dx.doi.org/10.1002/esp.4933', etc
df['doi'] = df['doi'].str.replace('http://dx.doi.org/', '', regex=True)  # specify regex=True since in future updates,
df['doi'] = df['doi'].str.replace('https://doi.org/', '', regex=True)  # the new default will be regex=False
df['doi'] = df['doi'].str.replace('doi:', '', regex=True)
df['doi'] = df['doi'].str.strip()

# remove miscellaneous 'header' words that may exist in the abstract pulled from an API response
remove_words = ['ABSTRACT', 'Abstract', 'SUMMARY', 'Summary', 'BACKGROUND', 'INTRODUCTION', 'PURPOSE', 'OBJECTIVE']
pat = r'\b(?:{})\b'.format('|'.join(remove_words))
df['abstract'] = df['abstract'].str.replace(pat, '', regex=True)
df = df[df['abstract'].str.contains('\[This corrects the article DOI: ') == False]  # some articles from APIs have this!
df['abstract'] = df['abstract'].str.strip()  # some abstracts have lots of white space at the ends of the relevant text

# fix the PubMed IDs that are long and result in broken links
df['pmid'] = df['pmid'].str.split('\n', n=1, expand=True)

# drop all empty rows - helpful if you want to make sure all rows have DOIs to make API requests with
df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)

# remove duplicate rows
df = df.drop_duplicates()

# remove rows that aren't open access
df['is_open_access'] = df['is_open_access'].astype('bool')  # just in case the column is of String type and not bool
df_filtered = df[df['is_open_access']]  # creates a new dataframe with only is_open_access being 'TRUE'
