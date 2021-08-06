## sophia-workflow
Here are descriptions for the code files within the test_pyautogui directory.

- **bad_urls.py**\
  This is a Python list of ```bad_urls.txt```, so that it is easy to make comments on which links are PDFs, which links shouldn't be tested with the PyAutoGUI method, etc. The list is returned within a function so that this list can be accessed from other files through imports.


- **bad_urls.txt**\
  ```bad_urls.txt``` contains links from the C&A AirTable that we were unable to get the DOI from using Jerry's method of searching for ```doi``` in all ```href``` tags.
  

- **get_doi_from_saved_html.py**\
  This file loops through all ```.html``` files within the folder ```downloaded_html_files``` and attempts to get the DOI from the saved HTML, first from ```href``` tags, then by using regex. If nothing is found, then the DOI remains an empty string.
  

- **save_html_files.py**\
  This file uses PyAutoGUI to save the HTML of all the files in the ```urls``` variable of bad_urls.py. The HTML files are saved into a folder called ```downloaded_html_files```, which is located in the directory that ```save_html_files.py``` is located in.  


- **test_pyautogui_using_springer_scraping.py**\
  This file uses PyAutoGUI to scrape the paper info for Springer articles. It was a good way to show that the PyAutoGUI method works; however, this file won't be used because the code is too specific for Springer. This code uses web scraping to "scrape" from the saved HTML (using PyAutoGUI), but we really should be using regex and other methods to "scrape" from the HMTL instead.
  