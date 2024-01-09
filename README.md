<h1 align="center">
    <a href="https://github.com/BetaHacks-Community-IIIT-Kottayam/Cypher-text-Toolkit">
        <img src="Logo.jpeg" valign="middle" height="58" alt="Betahacks Logo" style="border-radius:58px; border: 2px solid white" />
    </a>
    <span valign="middle">
        Betahacks
    </span>
</h1>

### Indian Institute of Information Technology Kottayam


## About Us

Welcome to the Betahacks, The Cyber Security club of Betalabs(Technical CLub) of Indian Institute of Information Technology. This is a place where we share our knowledge, experience, and passion for cybersecurity. We aim to promote cybersecurity awareness and provide a platform for students to learn and grow in this field.

## Useful Links

- Project [Link]()

### Cypher-Text Toolkit Contribution Guidelines

Thank you for your interest in contributing to Cypher-Text Toolkit, our open-source project dedicated to a collection of different encryption algorithms. To ensure a smooth contribution process, please adhere to the following guidelines:

1. **Programming Language**
   - All code submissions must be in Python.

2. **Code Structure**
   - Each submission should include at least one encryption and one corresponding decryption function.
   - Functions should return strings.
   - Include thorough error handling to enhance the robustness of the code.

3. **Algorithm Diversity**
   - While submitting, please check if the algorithm you are contributing has not already been submitted by another contributor. Diverse contributions are encouraged.

4. **Submission Format**
   - Fork the repository to your GitHub account.
   - In your fork, navigate to the "submissions" folder.
   - Create a new folder with the format `"yourname_rollno"` to organize your submission.
   - Place all algorithm files, a running script, and a `requirements.txt` file within your submission folder.

5. **Running Script Template**
    - It will install all the required packages for your script. Name it as `runme.py`

```python
# import pip to install required packages
import pip

# An install function is defined to install packages
def install(library):
    pip.main(['install', library])

# List of libraries to be installed
libraries = ["requests",]
for library in libraries:
    install(library)

# If any library needs special installation like nltk needs some downloads then,
# do it here with proper error handling
try:
    import nltk
except ImportError:
    install('nltk')
import nltk
nltk.download("words")
nltk.download('punkt')
```

6. **Readme.md File**
    - Write a `readme.md` file explaining your algorithm. Including the mathematics behind it.

_All the best 👍🏻_
