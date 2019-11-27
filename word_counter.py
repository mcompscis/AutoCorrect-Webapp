
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from collections import Counter
from wikipedia_url_getter import url_getter
import string
import time

print("Running word_counter.py")

start_time = time.process_time()

# link = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# word_list = ['name', 'hello', 'my', 'hello', 'my']
# word_freq = [word_list.count(w) for w in word_list]
# word_pair = dict(zip(word_list, word_freq))


def remove_punc(word):
    new_word = []
    for c in word:
        if c in string.punctuation or c in string.digits:
            new_word.append('')
        else:
            new_word.append(c.lower())
    return ''.join(new_word)


def sentence_word(sentence):
    word_list = []
    for word in sentence.split():
        word_list.append(remove_punc(word))
    # print(word_list)
    return word_list


def big_text(url):
    f = urlopen(url)
    page = f.read()
    f.close()
    parsed_text = soup(page, "html.parser")
    paragraphs_create = parsed_text.findAll("p")
    big_sentence = [paragraph.text for paragraph in paragraphs_create]
    return remove_punc(big_sentence)


def combine_big_text():
    link_list = url_getter()
    link_list = link_list[1:2]
    print(link_list)
    large_text = ''
    for link in link_list:
        large_text = large_text + big_text(link)
    return dict(Counter(sentence_word(large_text)))


word_count_25 = combine_big_text()
# print(word_count_25)
# print(len(word_count_25)) --> 19549 pairs
# over 4000 links

# print(word_count_25.keys())
print("--- %s seconds ---" % (time.process_time() - start_time))

