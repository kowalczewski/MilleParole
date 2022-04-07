# Top-1000-words

## Introduction

"Mille parole" project is a set of scripts to find the most frequently used words in a given language (I comparted three languages: Italian, English, and French). The analysis is based on the data sets from [Google Ngrams](https://storage.googleapis.com/books/ngrams/books/datasetsv2.html). It shows how nonlinear is language (the minority of words is used most of the time), as shown in the plot below.

The list of words may be also helpful for learners (see: sec. "Furhter ideas" in how it can be even more helfpul). This is a hobby problem, made solely for fun, so please see the disclaimer below.

![plot](https://raw.githubusercontent.com/kowalczewski/Top-1000-words/main/plot.png)

Some numbers:
- English: **688** words are used 40% of time, **1089392** words in total.
- French: **691** words are used 40% of time, **348189** words in total.
- Italian: **960** words are used 40% of time, **338283** words in total.

## How it works

This is how it works:
1. `group_words.py` takes the raw ngrams files (each file corresponds to a single letter of alphabet) and groups by words. Therefore, it shows how many times a given word occured in general (the original ngrams files give occurences of a given word in a given year). Then the script produces CSV files (a.csv, b.csv, c.csv, ...) for further analysis. This is the most time-consuming step and therefore we keep it seperate from step 2 (i.e., different scripts are used in step 1 and 2). It is also worth keeping csv files corresponding to letters for any further analysis.
2. `merge_words.py` takes the a.csv, b.csv, c.csv... files, puts them into PD dataframe, removes words with the occurence below a certain threshold, and returns a CSV file with the list of words
3. `language_analysis.ipynb` is a Jupyter Notebook for analysis. It does some data cleaning and returns the plot of occurences (%) as a function of number of words (log scale).

### Assumptions

1. Words that occured starting from year 1950, to get a relatively modern language.
2. Only words that appeared more than 1000 times are taken into consideration.
3. I don't distinguish between different parts of speech (different parts of speech are merged into a single word).
4. The datasets are based on books, so of course it may differ from the spoken language. 

## Further ideas

1. Add example phrases for the top 1000 words, which may be helpful for learners. We will get a nice phrasebook to learn the language. Make a simple website with the list of top 1000 words and corresponding phrases. The users will be able to suggest their features.
2. Compare data from intervals, say 1900-1924, 1925-1949, 1950-1974, 1975-1999 to see if the dynamics changes.

## Disclaimer

This is just a hobby problem. I am not doing any serious research related to language etc. It is definitely not a serious scientific analysis, it may contain flaws etc. Still, I find it interesting. My first approach to this problem is [in this repository](https://github.com/kowalczewski/MostPopWords/) (I was learning Spark at the time).