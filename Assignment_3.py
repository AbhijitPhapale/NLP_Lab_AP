#import library
import spacy
raw_text="""choosing to become an engineer can be driven by a passion for problem-solving, a desire to make a positive impact, and an interest in technical fields. It is a career path that offers opportunities for 
personal growth, professional development, and contributing to the betterment of society """
NER = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
text= NER(raw_text)
for w in text.ents:
    print(w.text,w.label_)
spacy.displacy.render(text, style="ent",jupyter=True)
spacy.explain(u"NORP")

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('treebank')

sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent[0]))
nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
raw_words= word_tokenize(raw_text)
tags=pos_tag(raw_words)
nltk.download('maxent_ne_chunker')

nltk.download('words')
ne = nltk.ne_chunk(tags,binary=True)
print(ne)

from nltk.chunk import tree2conlltags
iob = tree2conlltags(ne)
iob

#OUTPUT

# (S
#   choosing/VBG
#   to/TO
#   become/VB
#   an/DT
#   engineer/NN
#   can/MD
#   be/VB
#   driven/VBN
#   by/IN
#   a/DT
#   passion/NN
#   for/IN
#   problem-solving/NN
#   ,/,
#   a/DT
#   desire/NN
#   to/TO
#   make/VB
#   a/DT
#   positive/JJ
#   impact/NN
#   ,/,
#   and/CC
#   an/DT
#   interest/NN
#   in/IN
#   technical/JJ
#   fields/NNS
#   ./.
#   It/PRP
#   is/VBZ
#   a/DT
#   career/NN
#   path/NN
#   that/IN
#   offers/VBZ
#   opportunities/NNS
#   for/IN
#   personal/JJ
#   growth/NN
#   ,/,
#   professional/JJ
#   development/NN
#   ,/,
#   and/CC
#   contributing/VBG
#   to/TO
#   the/DT
#   betterment/NN
#   of/IN
#   society/NN)

# [('choosing', 'VBG', 'O'),
#  ('to', 'TO', 'O'),
#  ('become', 'VB', 'O'),
#  ('an', 'DT', 'O'),
#  ('engineer', 'NN', 'O'),
#  ('can', 'MD', 'O'),
#  ('be', 'VB', 'O'),
#  ('driven', 'VBN', 'O'),
#  ('by', 'IN', 'O'),
#  ('a', 'DT', 'O'),
#  ('passion', 'NN', 'O'),
#  ('for', 'IN', 'O'),
#  ('problem-solving', 'NN', 'O'),
#  (',', ',', 'O'),
#  ('a', 'DT', 'O'),
#  ('desire', 'NN', 'O'),
#  ('to', 'TO', 'O'),
#  ('make', 'VB', 'O'),
#  ('a', 'DT', 'O'),
#  ('positive', 'JJ', 'O'),
#  ('impact', 'NN', 'O'),
#  (',', ',', 'O'),
#  ('and', 'CC', 'O'),
#  ('an', 'DT', 'O'),
#  ('interest', 'NN', 'O'),
#  ('in', 'IN', 'O'),
#  ('technical', 'JJ', 'O'),
#  ('fields', 'NNS', 'O'),
#  ('.', '.', 'O'),
#  ('It', 'PRP', 'O'),
#  ('is', 'VBZ', 'O'),
#  ('a', 'DT', 'O'),
#  ('career', 'NN', 'O'),
#  ('path', 'NN', 'O'),
#  ('that', 'IN', 'O'),
#  ('offers', 'VBZ', 'O'),
#  ('opportunities', 'NNS', 'O'),
#  ('for', 'IN', 'O'),
#  ('personal', 'JJ', 'O'),
#  ('growth', 'NN', 'O'),
#  (',', ',', 'O'),
#  ('professional', 'JJ', 'O'),
#  ('development', 'NN', 'O'),
#  (',', ',', 'O'),
#  ('and', 'CC', 'O'),
#  ('contributing', 'VBG', 'O'),
#  ('to', 'TO', 'O'),
#  ('the', 'DT', 'O'),
#  ('betterment', 'NN', 'O'),
#  ('of', 'IN', 'O'),
#  ('society', 'NN', 'O')]
