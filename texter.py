import string
import contractions
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

book = strip_headers(load_etext(2701)).strip()
print(book)

# load text
filename = '11-0.txt'
file = open(filename, encoding="utf8")
text = file.read()
file.close()
# expand contactions
def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)
expand = replace_contractions(text)
# split into words by white space
words = expand.split()
# remove punctuation from each word
print(string.punctuation)
table = str.maketrans('', '', '`~!@#$%^&*()-_=+[]{}\|:;"<>?/‘’“”©⌐™')
stripped = [w.translate(table) for w in words]
# convert to lower case
stripped = [word.lower() for word in stripped]
print(stripped[:100])
