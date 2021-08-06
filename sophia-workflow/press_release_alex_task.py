"""
This code deals with some of the tasks Alex needed help with on 8/5/21.
Find the list of press release
"""
import pandas as pd

# 1. read new_biomimicry_papers.csv and select/rename appropriate columns
new_biomimicry_papers_df = pd.read_csv('../data/new_biomimicry_papers.csv')
new_biomimicry_papers_df = new_biomimicry_papers_df[['press_release', 'journal_url', 'doi']]
new_biomimicry_papers_df.rename(
	columns={'press_release': 'press_release_url', 'journal_url': 'paper_url'},
	inplace=True
)

# 2. read no_labels.csv and select/rename appropriate columns
no_labels_df = pd.read_csv('../data/no_labels.csv')
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
content_to_be_added_df = pd.read_csv('../data/content_to_be_added.csv')
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
master_merged_urls_1 = set(master_merged_df['press_release_url'].tolist())
content_to_be_added_urls_1 = set(content_to_be_added_df['press_release_url'].tolist())
unique_urls_1 = list(content_to_be_added_urls_1 - master_merged_urls_1)  # a list of the overlapping urls

master_merged_urls_2 = set(master_merged_df['paper_url'].tolist())
content_to_be_added_urls_2 = set(content_to_be_added_df['paper_url'].tolist())
unique_urls_2 = list(content_to_be_added_urls_2 - master_merged_urls_2)  # a list of the overlapping urls

# master_merged_urls = set(master_merged_df['press_release_url'].tolist())
# content_to_be_added_urls = set(content_to_be_added_df['press_release_url'].tolist())
# unique_urls = list(content_to_be_added_urls - master_merged_urls)  # a list of the overlapping urls

for url in unique_urls_1:
	print(f'{url}')
	# print('row:', content_to_be_added_df.loc[content_to_be_added_df['press_release_url'] == url])

print()

for url in unique_urls_2:
	print(f'{url}')
	# print('row :', content_to_be_added_df.loc[content_to_be_added_df['paper_url'] == url])

