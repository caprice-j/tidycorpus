from distutils.core import setup
setup(
  name = 'tidycorpus',
  packages = ['tidycorpus'], # this must be the same as the name above
  version = '0.1',
  description = 'Preprocess corpus data to be scikit-learn ready',
  author = 'Yasutaka Tanaka',
  author_email = 'tnk.yasutaka@gmail.com',
  url = 'https://github.com/caprice-j/tidycorpus', # use the URL to the github repo
  download_url = 'https://github.com/caprice-j/tidycorpus/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['scikit-learn', 'machine learning', 'corpus', 'nlp'], # arbitrary keywords
  classifiers = [],
)