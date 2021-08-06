"""
This code deals with some of the tasks Alex needed help with on 8/5/21.
"""

import pandas as pd

# 1. read new_biomimicry_papers.csv and select/rename appropriate columns
new_biomimicry_papers_df = pd.read_csv('../sophia-data/new_biomimicry_papers.csv')
new_biomimicry_papers_df = new_biomimicry_papers_df[['press_release', 'journal_url', 'doi']]
new_biomimicry_papers_df.rename(
	columns={'press_release': 'press_release_url', 'journal_url': 'paper_url'},
	inplace=True
)

# 2. read no_labels.csv and select/rename appropriate columns
no_labels_df = pd.read_csv('../sophia-data/press_release_alex_task_files/no_labels.csv')
no_labels_df = no_labels_df[['url', 'doi']]
no_labels_df.insert(loc=0, column='press_release_url', value='')
no_labels_df.rename(
	columns={'url': 'paper_url'},
	inplace=True
)

# 3. now that new_biomimicry_papers.csv and no_labels.csv now have the same column names, they can be merged!
# 		combine the 307 press release papers with the 67 unlabelled papers
master_merged_df = pd.concat([new_biomimicry_papers_df, no_labels_df], ignore_index=True)

# 4. before we compare the urls in content_to_be_added.csv with master_merged_df,
# 		we must make sure that content_to_be_added_df has the right columns and column names, with all cells filled amd clean
content_to_be_added_df = pd.read_csv('../sophia-data/press_release_alex_task_files/content_to_be_added.csv')
content_to_be_added_df = content_to_be_added_df[['Press release/Article', 'Paper website']]
content_to_be_added_df.insert(loc=2, column='doi', value='')
content_to_be_added_df.rename(
	columns={'Press release/Article': 'press_release_url', 'Paper website': 'paper_url'},
	inplace=True
)
content_to_be_added_df.dropna(subset=['press_release_url', 'paper_url'], inplace=True)
content_to_be_added_df['press_release_url'] = content_to_be_added_df['press_release_url'].str.replace('<', '')
content_to_be_added_df['press_release_url'] = content_to_be_added_df['press_release_url'].str.replace('>', '')
content_to_be_added_df['press_release_url'] = content_to_be_added_df['press_release_url'].str.strip()

# 5. see which articles are unique to this file: content_to_be_added.csv
# https://stackoverflow.com/questions/28901683/pandas-get-rows-which-are-not-in-other-dataframe
common = content_to_be_added_df.merge(master_merged_df, on=['press_release_url', 'paper_url', 'doi'])
unique_df = content_to_be_added_df[(~content_to_be_added_df.press_release_url.isin(common.press_release_url))]

# 6. print out the results!
unique_df.to_csv('../sophia-data/unique_urls_in_content_to_be_created.csv')

# 7. merge the approved unique urls to master_merged_df
alex_approved_unique_df = pd.read_csv(
	'../sophia-data/press_release_alex_task_files/unique_urls_in_content_to_be_created_AR_edits_08_06_21.csv')
biomimicry_papers_no_labels_df = pd.concat([master_merged_df, alex_approved_unique_df], ignore_index=True)
#		remove the mysterious 'Unnamed' column
biomimicry_papers_no_labels_df = biomimicry_papers_no_labels_df.loc[:, ~biomimicry_papers_no_labels_df.columns.str.contains('^Unnamed')]
biomimicry_papers_no_labels_df.to_csv('../sophia-data/biomimicry_papers_no_labels.csv')

# 8. after using the Semantic Scholar API code, clean the CSV contents
raw_no_labels_paper_info_df = pd.read_csv(
	'../sophia-data/press_release_alex_task_files/raw_biomimicry_papers_no_labels_info.csv')

# 		remove miscellaneous 'header' words that may exist in the abstract pulled from an API response
remove_words = ['ABSTRACT', 'Abstract', 'SUMMARY', 'Summary', 'BACKGROUND', 'INTRODUCTION', 'PURPOSE', 'OBJECTIVE']
pat = r'\b(?:{})\b'.format('|'.join(remove_words))
raw_no_labels_paper_info_df['abstract'] = raw_no_labels_paper_info_df['abstract'].str.replace(pat, '', regex=True)
raw_no_labels_paper_info_df = raw_no_labels_paper_info_df[raw_no_labels_paper_info_df['abstract'].str.contains('\[This corrects the article DOI: ') == False]  # some articles from APIs have this!
raw_no_labels_paper_info_df['abstract'] = raw_no_labels_paper_info_df['abstract'].str.strip()  # some abstracts have lots of white space at the ends of the relevant text

# 		drop duplicate rows
raw_no_labels_paper_info_df = raw_no_labels_paper_info_df.drop_duplicates()

# 		drop the paper info columns that we don't need
raw_no_labels_paper_info_df.drop(
	columns=['press_release_url', 'paper_url'],
	inplace=True)

# 		get the cleaned result!
raw_no_labels_paper_info_df.to_csv('../sophia-data/cleaned_biomimicry_papers_no_labels.csv')
