# Top-1000-words

## Introduction

"Mille parole" project is a set of scripts to find the most frequently used words in a given language (I compared three languages: Italian, English, and French). The analysis is based on the data sets from [Google Ngrams](https://storage.googleapis.com/books/ngrams/books/datasetsv2.html). It shows how nonlinear is language (the minority of words is used most of the time), as shown in the plot below.

The list of words may be also helpful for learners (see: sec. "Further ideas" in how it can be even more helpful). This is a hobby problem, made solely for fun, so please see the disclaimer below.

![plot](https://raw.githubusercontent.com/kowalczewski/MilleParole/master/plot_annotated.png)

Some numbers:
- English: 425 words are used 40% of the time, 420513 words in total.
- French: 505 words are used 40% of the time, 186158 words in total.
- Italian: 668 words are used 40% of the time, 215171 words in total.

Or, to put it differently:
- Italian: 1000 words are used 45.7% of the time.
- English: 1000 words are used 53.5% of the time.
- French: 1000 words are used 50.0% of the time.

## How it works

This is how it works:
1. `group_words.py` takes the raw ngrams files (each file corresponds to a single letter of the alphabet) and groups them by words. Therefore, it shows how many times a given word occured in general (the original ngrams files give occurences of a given word in a given year). Then the script produces CSV files (a.csv, b.csv, c.csv, ...) for further analysis. This is the most time-consuming step and therefore we keep it seperate from step 2 (i.e., different scripts are used in step 1 and 2). It is also worth keeping csv files corresponding to letters for any further analysis.
2. `merge_words.py` takes the a.csv, b.csv, c.csv... files, puts them into PD dataframe, removes words with the occurrence below a certain threshold, and returns a CSV file with the list of words
3. `language_analysis.ipynb` is a Jupyter Notebook for analysis. It does some data cleaning and returns the plot of occurrences (%) as a function of number of words (log scale).

### Assumptions

1. Words that occurred starting from the year 1950, to get a relatively modern language.
2. Only words that appeared more than 1000 times are taken into consideration.
3. I don't distinguish between different parts of speech (different parts of speech are merged into a single word).
4. The datasets are based on books, so of course it may differ from the spoken language.
5. I remove names, i.e., words starting with capital letters. This changes the results quite significantly.

## Further ideas

1. Add example phrases for the top 1000 words, which may be helpful for learners. We will get a nice phrasebook to learn the language. Make a simple website with the list of top 1000 words and corresponding phrases. The users will be able to suggest their own phrases.
2. Compare data from intervals, say 1900-1924, 1925-1949, 1950-1974, 1975-1999 to see if the dynamics changes.
3. Focus on the names (e.g., geographical), instead of removing them. E.g., see how much more often Roma is mentioned compared to Torino (in Italian).

## Disclaimer

This is just a hobby problem. I am not doing any serious research related to language etc. It is definitely not a serious scientific analysis, it may contain flaws etc. Still, I find it interesting. My first approach to this problem is [in this repository](https://github.com/kowalczewski/MostPopWords/) (I was learning Spark at the time).
