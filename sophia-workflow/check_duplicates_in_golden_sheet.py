"""
Per Alex's request, see if the press release papers in new_biomimicry_papers.csv are within the
unlabeled papers (no_labels.csv) of the Golden Sheet or not.
"""

import pandas as pd


def convert_to_csv():
	fat_df = pd.read_csv("../sophia-data/press_release_alex_task_files/no_labels.csv")
	skinny_df = pd.read_csv("../sophia-data/new_biomimicry_papers.csv")
	
	fat_urls = set(fat_df['url'].tolist())
	skinny_urls = set(skinny_df['journal_url'].tolist())
	
	return list(fat_urls & skinny_urls)  # a list of the overlapping urls


print(convert_to_csv())  # print the overlap!

