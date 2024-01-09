# import pip to install required packages
import pip

# An install function is defined to install packages
def install(library):
    pip.main(['install', library])

# list of libraries to be installed
# this is similar to pip install library-name
libraries = ["requests",]
for library in libraries:
    install(library)

# If any library needs special installation like nltk needs some downloads then,
# do it here with proper error handling
try:
    import nltk
except:
    install('nltk')
import nltk
nltk.download("words")
nltk.download('punkt')