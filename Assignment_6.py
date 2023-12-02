"""
Name : Abhijit Phapale
Roll No :45
Batch:B3
Pract no 6: Implement and visualize 
dependancy parsing of textual input using standfor and spacy library
"""
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy
text = "My name is Abhijit I am from Sanjivani College of Engineering"
doc = nlp(text)
for token in doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
displacy.serve(doc,style="dep")    

'''
Output
TOKEN: My
=====
token.tag_ = 'PRP$'
token.head.text = 'name'
token.dep_ = 'poss'

TOKEN: name
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: Abhijit
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: I
=====
token.tag_ = 'PRP'
token.head.text = 'am'
token.dep_ = 'nsubj'

TOKEN: am
=====
token.tag_ = 'VBP'
token.head.text = 'is'
token.dep_ = 'ccomp'

TOKEN: from
=====
token.tag_ = 'IN'
token.head.text = 'am'
token.dep_ = 'prep'

TOKEN: Sanjivani
=====
token.tag_ = 'NNP'
token.head.text = 'College'
token.dep_ = 'compound'

TOKEN: College
=====
token.tag_ = 'NNP'
token.head.text = 'from'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'College'
token.dep_ = 'prep'

TOKEN: Engineering
=====
token.tag_ = 'NNP'
token.head.text = 'of'
token.dep_ = 'pobj'
PS C:\Users\AJay\Desktop\NLP_lab_MP> & C:/Users/AJay/AppData/Local/Programs/Python/Python311/python.exe c:/Users/AJay/Desktop/NLP_lab_MP/nlp6.py

TOKEN: My
=====
token.tag_ = 'PRP$'
token.head.text = 'name'
token.dep_ = 'poss'

TOKEN: name
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: Abhijit
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: I
=====
token.tag_ = 'PRP'
token.head.text = 'am'
token.dep_ = 'nsubj'

TOKEN: am
=====
token.tag_ = 'VBP'
token.head.text = 'is'
token.dep_ = 'ccomp'

TOKEN: from
=====
token.tag_ = 'IN'
token.head.text = 'am'
token.dep_ = 'prep'

TOKEN: Sanjivani
=====
token.tag_ = 'NNP'
token.head.text = 'College'
token.dep_ = 'compound'

TOKEN: College
=====
token.tag_ = 'NNP'
token.head.text = 'from'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'College'
token.dep_ = 'prep'

TOKEN: Engineering
=====
token.tag_ = 'NNP'
token.head.text = 'of'
token.dep_ = 'pobj'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...



'''