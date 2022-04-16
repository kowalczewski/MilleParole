'''
This file takes the a.csv, b.csv, c.csv... files, puts them into PD dataframe, removes words with the occurence below a certain threshold, 
and returns a CSV file with the list of words.
'''

import pandas as pd
import string

def main():

    # ===================== PARAMETERS =====================
    # take only words than occure more than n_min times
    n_min = 1000
    # year from (here only for filename)
    year_min = 1950
    # language: eng, ita, fre, ger
    language = 'ger'
    # ======================================================

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)

    df = pd.DataFrame(columns = ['word', 'count'])

    for letter in alphabet_list:
        print(letter)
        fname = f'./letters_grouped_{language}_from_{year_min}/{letter}.csv'
        df_new = pd.read_csv(fname, delimiter='\t')
        df = pd.concat([df, df_new], ignore_index=True)

    # Take only words than occure more than n_min times.
    df = df[df['count']>n_min]

    # df.sort_values(by=['count'], ascending=False, inplace=True, ignore_index=True)

    # Save all
    df.to_csv(f'{language}_from_{year_min}.csv', sep='\t', index=False)

main()
