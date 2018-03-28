import string
import contractions
import io
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

#book = strip_headers(load_etext(2701)).strip()
#print(book)

# load text
filename = 'songs-input.txt'
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
print(stripped[:200])

#write to file
thefile = open('lyrics-cleaned.txt','w',encoding="utf8")
for item in stripped:
  thefile.write(" " + item)
