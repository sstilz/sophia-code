# Code obtained from:
# https://stackoverflow.com/questions/30335474/merging-multiple-csv-files-without-headers-being-repeated-using-python

import glob

interesting_files = glob.glob("../data/negative_paper_info_chunks/*.csv")

header_saved = False
with open('../data/final_negative_paper_info.csv', 'w') as file_out:
    for filename in interesting_files:
        with open(filename) as file_in:
            header = next(file_in)
            if not header_saved:
                file_out.write(header)
                header_saved = True
            for line in file_in:
                file_out.write(line)
