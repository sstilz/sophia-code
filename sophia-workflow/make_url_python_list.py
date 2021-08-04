"""
To run this file, modify the run configurations!
"""

import argparse
import sys

parser = argparse.ArgumentParser(prog=sys.argv[0], description="create a Python list with the items from .txt file")
parser.add_argument("txt_file", help="the .txt file that needs to be converted to a Python list", type=str)
args = parser.parse_args()
txt_file = args.txt_file


with open(txt_file) as txt:
	lines = txt.readlines()
	python_list = '\n'
	for line in lines:
		line = line.replace('\n', '')
		python_list += f"\t'{line}', \n"
		
print(f'[{python_list}]')  # you can copy & paste the output Python list that is printed to the screen
