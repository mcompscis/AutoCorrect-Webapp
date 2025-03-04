from collections import Counter
import correction
from show_db import getDbPairs
import sys

# print("Running auto_correct.py")

words_dict = getDbPairs()
common_wiki = set(words_dict.keys())

def common_filter(word):
    all_words = correction.correction(word)
    return common_wiki & all_words

def common_values(word):
    list_words = common_filter(word)
    list_dict = {}
    for key, value in words_dict.items():
        if key in list_words:
            list_dict[key] = value
    return list_dict

def most_common_words(word):
    dict_words = common_values(word)
    return list(dict(Counter(dict_words).most_common(5)).keys())

def best_words(word):
    list_words = most_common_words(word)
    for x in list_words:
        print(x)

best_words(sys.argv[1])
sys.stdout.flush()
