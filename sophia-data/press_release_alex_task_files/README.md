## press_release_alex_task_files
Here are descriptions for all the data files I used to complete the most recent task in my internship: getting new, unique press release-derived biomimicry papers for the Golden Sheet. I know that reading these descriptions in alphabetical order can be confusing, so I added numbers next to the file names in parenthesis to indicate the relative order that these files were used in my code.


- **biomimicry_papers_no_labels.csv (4)**\
  CSV containing ```press_release_url```, ```paper_url```, and ```doi```. This was the result of merging ```new_biomimicry_papers.csv```, ```no_labels.csv```, and ```content_to_be_added.csv```. Duplicate rows are already removed from this file.


- **biomimicry_papers_no_labels_with_dois (5)**\
  An updated version of ```biomimicry_papers_no_labels.csv``` with all cells in the DOI column filled. Alex and I filled them in manually, since it is too complicated to use code to get DOIs at the moment. 
  

- **cleaned_biomimicry_papers_no_labels.csv (7)**\
  The result of applying code from ```clean_paper_info_data.py``` on ```raw_biomimicry_papers_no_labels_info.csv```. Part of the cleaning included dropping duplicate, stripping text in the ```abstract``` column, etc.
  

- **content_to_be_added.csv (1)**\
  A file given to me from Alex containing additional press release papers and the scientific papers that the press release papers refer to. In one of Alex's tasks, she asked me to see if there were any papers in ```content_to_be_added.csv``` that weren't already included in ```new_biomimicry_papers.csv```. This way we could filter out unique press release papers to add to the Golden Sheet.


- **no_labels.csv (1)**\
  Contains all the rows in the current Golden Sheet that don't have labels.  


- **raw_biomimicry_papers_no_labels_info.csv (6)**\
  The result of running a slightly modified version of ```get_paper_info_using_ss_api.py``` using ```biomimicry_papers_no_labels.csv``` (see description of that file above). This file contains the raw paper info for the new press release papers to-be-added to the Golden Sheet.
  

- **unique_urls_in_content_to_be_created.csv (2)**\
  Contains all press release-derived biomimicry in ```content_to_be_added.csv``` that weren't already in ```new_biomimicry_papers.csv``` or ```no_labels.csv```. These papers were then sent to Alex for review, where she determined if the papers should be eventually merged to the Golden Sheet or not.
  

- **unique_urls_in_content_to_be_created_AR_edits_08_06_21.csv (3)**\
  This is the result of Alex reviewing ```unique_urls_in_content_to_be_created.csv``` and deleting any articles that she didn't want to be included in the Golden Sheet.
