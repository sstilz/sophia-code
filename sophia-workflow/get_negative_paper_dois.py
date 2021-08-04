"""
The last usage of this script was to get the first 2,000 DOIs from the PyMed API for 5 different journals,
for a total of 10,000 DOIs of negative biomimicry papers.

Alternative journals that would provide good negative biomimicry papers are
'Journal of Biomechanics', 'Planta', 'Functional Ecology', 'Marine Biology', and 'Journal of Experimental Botany'.

Note: 'Plant, Cell & Environment' was not recognized by the PyMed API, likely because of the ampersand in its name.
"""

from pymed import PubMed
import pandas as pd

# get DOIs from PubMed
journals = ['Cell', 'PLoS Biology', 'Journal of Structural Biology', 'Journal of Comparative Physiology', 'Journal of Biomechanics']
df = pd.DataFrame(columns=['doi'])
df = df.convert_dtypes()

count = 0  # this variable will be printed while the code runs to show how far you are in the DOI-grabbing process
for journal in journals:
    pubmed = PubMed(tool="MyTool", email="my@email.address")
    query = f'({journal}[Journal]) AND (("2002/01/01"[Date - Publication] : "3000"[Date - Publication]))'
    results = pubmed.query(query, max_results=2000)
    for r in results:
        doi = r.doi if r.doi else ''
        df = df.append(
            {'doi': doi},
            ignore_index=True)
        count += 1
        print(f'Finished line {count}')

df.to_csv("negative_paper_dois.csv")  # this file can be found in the sophia-data folder
