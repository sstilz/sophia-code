import pandas as pd

df = pd.read_csv('../sophia-data/raw_press_release_paper_info.csv', index_col=0)

# clean abstract column
remove_words = ['ABSTRACT', 'Abstract', 'SUMMARY', 'Summary', 'BACKGROUND', 'INTRODUCTION', 'PURPOSE', 'OBJECTIVE']
pat = r'\b(?:{})\b'.format('|'.join(remove_words))
df['abstract'] = df['abstract'].str.replace(pat, '', regex=True)
df['abstract'] = df['abstract'].str.strip()
df = df[df['abstract'].str.contains('\[This corrects the article DOI: ') == False]

df = df.drop_duplicates()
df.to_csv('../sophia-data/cleaned_press_release_paper_info.csv')

# TODO - manually add journal_name to some empty columns
