'''
This file takes the raw ngrams files (each file corresponds to a single letter of alphabet) and groups by words. 
Therefore, it shows how many times a given word occured in general (the original ngrams files give occurences 
of a given word in a given year). Then the script produces CSV files for further analysis. The ngram files should
be in the same directory.

Todo:
- narrow the range of years, to get more modern langauge(say, starting from 1900)

Useful links:
-https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
'''

import pandas as pd
import string
from pathlib import Path

def main():

    # ===================== PARAMETERS =====================
    # language: eng, ita, or fre
    language = 'ita'
    year_min = 1950
    # ======================================================

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    for letter in alphabet_list:
        print(letter)
        fname = f'/home/piotr/Documents/Python/ngrams/{language}/googlebooks-{language}-all-1gram-20120701-{letter}'
        group_file(fname, letter, year_min, language)

def group_file(filename, letter, from_year, language):
    df = pd.read_csv(filename, delimiter='\t', names=['word', 'year', 'count', 'count books'])
    # print('before narrowing the year range: ', len(df))
    # narrow the range of years
    df = df[df['year']>=from_year]
    # print('before narrowing the year range: ', len(df))
    df.drop(['year', 'count books'], inplace=True, axis=1)
    df_grouped = df.groupby('word').sum()
    
    # Save to file
    folder = f'letters_grouped_{language}_from_'+str(from_year)
    Path(folder).mkdir(parents=True, exist_ok=True)
    df_grouped.to_csv(f'{folder}/{letter}.csv', sep='\t')
    return None

main()


