import time
import pyautogui
import os
from bad_urls import bad_urls_list


def save_html_files(url):
	time.sleep(2)  # the time it takes to open up Chrome
	
	# open a new tab, enter the url, and wait for the site to load
	pyautogui.hotkey('command', 't')
	pyautogui.typewrite(f'{url}\n')
	time.sleep(2)
	
	pyautogui.hotkey('command', 's')  # bring up the pop-up for saving files
	time.sleep(1)  # wait for the pop-up to load
	
	path = os.getcwd()  # the path to the directory which save_html_files.py is in
	file_name = round(time.time())  # current time in seconds
	
	pyautogui.typewrite(
		f'{path}/downloaded_html_files/{file_name}.html')  # this '\n' is for confirming the path of the to-be-saved file
	time.sleep(1)  # wait a second. It won't work if you press 'enter' instantly after typing in the path!
	pyautogui.typewrite('\n\n')  # need 2 '\n's - one to confirm the path, and one to confirm the download
	time.sleep(5)  # wait for the file to download
	
	# close the tab since the loaded website is now saved
	pyautogui.hotkey('command', 'w')


########################################################################################################################
# to use this function:
bad_urls = open('bad_urls.txt', 'r').readlines()  # list of urls that have stubborn DOIs for scraping

count = 0
for url in bad_urls_list():
	count += 1
	print(f'On line {count}')
	save_html_files(url)
