"""Utility functions and variables to process Brown Corpus in nltk."""
import nltk
from sklearn.model_selection import train_test_split
import random

brown_genre2sym = {
           'news': 'a',  'editorial': 'b',         'reviews': 'c',
       'religion': 'd',    'hobbies': 'e',            'lore': 'f',
 'belles_lettres': 'g', 'government': 'h',         'learned': 'j',
        'fiction': 'k',    'mystery': 'l', 'science_fiction': 'm',
      'adventure': 'n',    'romance': 'p',           'humor': 'r'
}

brown_sym2genre = {brown_genre_symbol: genre for brown_genre_symbol, genre
                   in zip(brown_genre2sym.values(), brown_genre2sym.keys())}

def genre_sym2doc_list(genre="mystery"):
    random.seed(1234)
    genre_sym = brown_genre2sym[genre]
    # FIXME for other genres
    #mystery_filenames = ["cl" + str("%02d" % i) for i in range(1, 25)]
    fnames = [f for f in nltk.corpus.brown.fileids() if f.find('c' + genre_sym) != -1]
    files_tr, files_te = train_test_split(fnames  , train_size = .8)
    files_tr, files_va = train_test_split(files_tr, train_size = .8)

    print("%13s -> selected filenames: %s" % (genre , str(", ".join(fnames))))

    def get_docs(doc_files, nWords=100000): # far larger than # words in each text
        docs = []
        for name in doc_files:
            text = " ".join(nltk.corpus.brown.words(fileids=name)[0:nWords])
            docs.append(text)
        return docs

    genre = [genre] # for ["news"] * 3 => ["news", "news", "news"]
    return (get_docs(files_tr),  get_docs(files_va),  get_docs(files_te),
            genre*len(files_tr), genre*len(files_va), genre*len(files_te))

def get_corpus_text_list(genres = ['news', 'mystery']):
    docs_tr, docs_va, docs_te = [], [], []
    y_tr   ,    y_va,    y_te = [], [], []
    for g in genres:
        dtr, dva, dte, ytr, yva, yte = genre_sym2doc_list(g)
        docs_tr.append(dtr);  y_tr.append(ytr)
        docs_va.append(dva);  y_va.append(yva)
        docs_te.append(dte);  y_te.append(yte)

    def flatten(nested_list):
        flattened = []
        for inner_list in nested_list:
            flattened.extend(inner_list) # [1].extend([3,4]) => [1,3,4]
        return flattened

    return (flatten(docs_tr), flatten(docs_va), flatten(docs_te),
            flatten(y_tr)   , flatten(y_va)   , flatten(y_te))
