from context import tidycorpus as tc
import nltk
from collections import Counter

if __name__ == "__main__":
    assert Counter(nltk.corpus.brown.categories()) == Counter(tc.brown.genre2sym.keys())
    assert Counter(nltk.corpus.brown.categories()) == Counter(tc.brown.sym2genre.values())
    # MAYBE-LATER How can I check symbols are correct?
