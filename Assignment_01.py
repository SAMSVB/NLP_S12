# Assignment No_01
# Name:shantanu vilas borude
# Roll No_12
# Title: "Text pre-processing using NLP operations."

#import library
import spacy   

#language model loaded
nlp=spacy.load("en_core_web_sm")

#input text
in_text=(
    "Chef george crum reportedly created potato chips in 1853"
     "in New York after being fed up with a customer who continuously"
     "sent fis fried potatoes back,complaining that they were soggy"
     "and not crunchy enough!"
)

### TOKENIZATION ###
ab_doc=nlp(in_text)
print("\nTOKENIZATION :\n")
#get token and token id
for token in ab_doc:
    print (token, token.idx)


### STOP-WORD REMOVAL ###
print("\nAFTER REMOVING STOP-WORDS :\n")
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
print([token for token in ab_doc if not token.is_stop])


### LEMMATIZATION ###
print("\nLEMMATIZATION :\n")
for token in ab_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


### PART OF SPEECH ###
print("\nPART OF SPEECH TAGGING :\n")
for token in ab_doc:
    print(
        f"""
            TOKEN: {str(token)}
            =====================================
            TAG: {str(token.tag_):10} POS: {token.pos_}
            EXPLANATION: {spacy.explain(token.tag_)}"""
        )


#OUTPUT ::::======================================================================
##### TOKENIZATION :

# Chef 0
# george 5
# crum 12
# reportedly 17
# created 28
# potato 36
# chips 43
# in 49
# 1853 52
# in 56
# New 59
# York 63
# after 68
# being 74
# fed 80
# up 84
# with 87
# a 92
# customer 94
# who 103
# continuouslysent 107
# fis 124
# fried 128
# potatoes 134
# back 143
# , 147
# complaining 148
# that 160
# they 165
# were 170
# soggyand 175
# not 184
# crunchy 188
# enough 196
# ! 202

###### AFTER REMOVING STOP-WORDS :

# [Chef, george, crum, reportedly, created, potato, chips, 1853, New, York, fed, customer, continuouslysent, fis, fried, potatoes, ,, complaining, soggyand, crunchy, !]

##### LEMMATIZATION :

#              created : create
#                chips : chip
#                being : be
#                  fed : feed
#                fried : fry
#             potatoes : potato
#          complaining : complain
#                 were : be

##### PART OF SPEECH TAGGING :


#             TOKEN: Chef
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: george
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: crum
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: reportedly
#             =====================================
#             TAG: RB         POS: ADV
#             EXPLANATION: adverb

#             TOKEN: created
#             =====================================
#             TAG: VBD        POS: VERB
#             EXPLANATION: verb, past tense

#             TOKEN: potato
#             =====================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: chips
#             =====================================
#             TAG: NNS        POS: NOUN
#             EXPLANATION: noun, plural

#             TOKEN: in
#             =====================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: 1853
#             =====================================
#             TAG: CD         POS: NUM
#             EXPLANATION: cardinal number

#             TOKEN: in
#             =====================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: New
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: York
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: after
#             =====================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: being
#             =====================================
#             TAG: VBG        POS: AUX
#             EXPLANATION: verb, gerund or present participle

#             TOKEN: fed
#             =====================================
#             TAG: VBN        POS: VERB
#             EXPLANATION: verb, past participle

#             TOKEN: up
#             =====================================
#             TAG: RP         POS: ADP
#             EXPLANATION: adverb, particle

#             TOKEN: with
#             =====================================
#             TAG: IN         POS: ADP
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: a
#             =====================================
#             TAG: DT         POS: DET
#             EXPLANATION: determiner

#             TOKEN: customer
#             =====================================
#             TAG: NN         POS: NOUN
#             EXPLANATION: noun, singular or mass

#             TOKEN: who
#             =====================================
#             TAG: WP         POS: PRON
#             EXPLANATION: wh-pronoun, personal

#             TOKEN: continuouslysent
#             =====================================
#             TAG: VBD        POS: VERB
#             EXPLANATION: verb, past tense

#             TOKEN: fis
#             =====================================
#             TAG: NNP        POS: PROPN
#             EXPLANATION: noun, proper singular

#             TOKEN: fried
#             =====================================
#             TAG: VBN        POS: VERB
#             EXPLANATION: verb, past participle

#             TOKEN: potatoes
#             =====================================
#             TAG: NNS        POS: NOUN
#             EXPLANATION: noun, plural

#             TOKEN: back
#             =====================================
#             TAG: RB         POS: ADV
#             EXPLANATION: adverb

#             TOKEN: ,
#             =====================================
#             TAG: ,          POS: PUNCT
#             EXPLANATION: punctuation mark, comma

#             TOKEN: complaining
#             =====================================
#             TAG: VBG        POS: VERB
#             EXPLANATION: verb, gerund or present participle

#             TOKEN: that
#             =====================================
#             TAG: IN         POS: SCONJ
#             EXPLANATION: conjunction, subordinating or preposition

#             TOKEN: they
#             =====================================
#             TAG: PRP        POS: PRON
#             EXPLANATION: pronoun, personal

#             TOKEN: were
#             =====================================
#             TAG: VBD        POS: AUX
#             EXPLANATION: verb, past tense

#             TOKEN: soggyand
#             =====================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: not
#             =====================================
#             TAG: RB         POS: PART
#             EXPLANATION: adverb

#             TOKEN: crunchy
#             =====================================
#             TAG: JJ         POS: ADJ
#             EXPLANATION: adjective (English), other noun-modifier (Chinese)

#             TOKEN: enough
#             =====================================
#             TAG: RB         POS: ADV
#             EXPLANATION: adverb

#             TOKEN: !
#             =====================================
#             TAG: .          POS: PUNCT
#             EXPLANATION: punctuation mark, sentence closer
