## sophia-workflow
Here are descriptions for all the (relevant) code files I wrote and used throughout my internship.

- **journal_scraping**\
  A folder which contains the individual web scraping files I made for the JEB, JSTOR, and Springer journals. This folder might not be useful anymore since the contents of all this web scraping is already updated in ```get_paper_info.py```.
  

- **test_pyautogui**\
  A folder containing all the code I used in regards to PyAutoGUI this internship.  
  

- **check_duplicates_in_golden_sheet.py**\
  Checks to see if a CSV containing URLs has already been merged into the Golden Sheet. This code could easily be modified to check for DOI or abstract overlaps, as opposed to URLs.
  
  
- **clean_paper_info_data.py**\
  Contains all the code necessary to clean common problems in the data from API responses (ex, inconsistent DOIs, abstracts with unnecessary headers, etc). If there are certain parts of the code that don't serve a purpose for your particular dataset of paper info, it should be ok to just comment that part of the code out.
  
  
- **clean_press_release_paper_info..py**\
  This code cleans ```raw_press_release_paper_info.csv```, where the result is stored in ```cleaned_press_release_paper_info.csv```.
  
  
- **get_jeb_paper_info_for_mturk.py**\
  This code obtains the paper info for the JEB papers that have been published as MTurk HITs. Alex had originally given me 10,000 JEB papers with the DOI, title, and abstract filled in. However, the title and abstract frequently had metacharacters which caused the rest of the text to be omitted. So, this code uses Semantic Scholar API requests (an adaptation of ```get_paper_info_using_ss_api.py```) to get back titles and abstracts without metacharacter problems. This code also cleans some 'messy' API responses, an adaptation of ```clean_paper_info_data.py```. 
  

- **get_negative_paper_dois.py**\
  This code uses the PyMed API to pull the first 2,000 non-biomimicry papers from 5 different journals for a total of 10,000 negative papers. The code could easily be modified to obtain DOIs (or titles, abstracts, urls, etc) of papers from other journals!
  

- **get_paper_info_using_ss_api.py**\
  Given a CSV file with DOIs, use the Semantic Scholar API to get the URL, title, abstract, is_open_access status, and journal name of a paper. This is the most important/used file in the workflow directory.
  

- **join_20_chunks_of_500.csv**\
  Helpful code that I found from Stack Overflow. Sometimes, if you need to run ```get_paper_info_using_ss_api.py```, it may help to run in chunks of 500 - this way the code doesn't take too long to run and lag out. In one case where I had to make 10,000 API requests, I chose to run the SS code in 20 chunks of 500, in which the results were all stored as CSV files in a common folder. Then I used this code to join the CSV chunks together. Note: even though the command line's ```cat``` command is quick, it doesn't omit the column headers of the latter 19 CSV chunks when merging. So, this Stack Overflow code might be a better alternative for now.
  

- **make_url_python_list.py**\
  This code converts the contents of the ```.txt``` file and prints out a Python list so you can easily make comments next to URLs that may be problematic or worth noting for some reason. I've used this code to make comments to the ```bad_urls.txt``` file, which helps for cleaning the data that I'll use for PyAutoGUI.
  

- **mturk_hit_utilities.py**\
  Contains useful functions to perform on MTurk HITs within ```mturk-manage```. Currently, there is code to change the expiration date of a HIT as well as code to delete a HIT.


- **press_release_alex_task.py**\
  Code to complete the most recent task from Alex, where I needed to determine all press release papers in ```content_to_be_added.csv``` that weren't in ```new_biomimicry_papers.csv``` nor ```no_labels.csv``` (see descriptions of these files in the sophia-data README.md file). The majority of this code focuses on renaming and cleaning various dataframes so that they can be concatenated together and compared.