import pip

def install(library):
    pip.main(['install', library])

library_name = "requests"
install(library_name)
try:
    import nltk
except:
    install('nltk')
import nltk
nltk.download("words")
nltk.download('punkt')