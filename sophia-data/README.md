## sophia-data
Here are descriptions for all the (relevant) data files I used throughout my internship.

- **negative_paper_info_chunks**\
  These were the 20 chunks of 500 rows that were produced upon running the commented-out code at the top of ```get_paper_info_using_ss_api.py```.
  

- **press_release_alex_task_files**\
  This folder contains all the files I used to complete the task I worked on with Alex, where we merged unique press release-derived biomimicry paper to the Golden Sheet. Click on the ```README.md``` file within that folder to see more detailed descriptions of those files.
  

- **50_jeb_hits**\
  Contains the HIT ID and URL to the most recent batch of 50 MTurk HITs.  


- **cleaned_jeb_data.csv**\
  Contains paper info for the 600-something JEB articles that we used as HITs for our binary labeling MTurk task. This was the result of running ```get_jeb_paper_info_for_mturk.py```.
  Note: the ```api_title``` column contains the true ```title``` values for the papers, while the ```api_abstract_cleaned``` column contains the true ```abstract``` values for the papers.
  
  
- **cleaned_negative_paper_info.csv**\
  Contains paper info for the 10,000 negative biomimicry papers obtained from 5 different biomimicry journals. Columns include ```doi```, ```url```, ```title```, ```abstract```, ```is_open_access```, ```journal_name```, and ```is_biomimicry```.


- **cleaned_press_release_paper_info.csv**\
  Contains paper info for the papers in ```new_biomimicry_papers.csv``` (file described below), starting line 180. Columns include ```doi```, ```url```, ```title```, ```abstract```, ```is_open_access```, ```journal_name```, and ```is_biomimicry```.
  

- **negative_paper_dois.csv**\
  Given a CSV file with DOIs, use the Semantic Scholar API to get the URL, title, abstract, is_open_access status, and journal name of a paper.
  

- **new_biomimicry_papers.csv**\
  Contains 300 or so new biomimicry papers from press releases. In rows 180-307, Alex and I manually obtained the URL to the published biomimicry paper which the press release was referring to, as well as the DOI for that published biomimicry paper. 
  

- **raw_jeb_paper_info.csv**\
  Contains the paper info CSV of ~10,000 JEB papers that Alex sent me to-be-posted on MTurk. After fixing some of the metacharacter problems in the title/abstract, long PubMed IDs, etc, the cleaned result of this file (for the first 600 rows) was exported as ```cleaned_jeb_data.csv``` (see description of that file above).


- **raw_press_release_paper_info.csv**\
  Contains rows 180 and beyond of ```new_biomimicry_papers.csv```. This CSV file contained abstracts with unnecessary headers (ex, "SUMMARY: "). There were also unfilled abstract cells. The cleaned version of this file is called ```clean_press_release_paper_info.csv```.
  

- **urls_not_in_jingle_sheet.py**\
  Contains a Python list of all the URLs in the Colleen & Alex tab of the AirTable which didn't have DOIs, but somehow didn't make it into the "Jingle Spreadsheet" for manual DOI scraping. The only reason this was in a Python file was so that I could make Python comments for every URL that was problematic (PDF, bad link, etc). The list of URLs was originally given to me by Herb in the form of a ```.txt``` file, but I used the ```make_url_python_list``` file within the ```sophia-workflow``` folder to convert it to a Python file.