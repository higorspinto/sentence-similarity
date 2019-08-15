""" 
Sentence Similarity

Sentence similarity is a common task in NLP.
This module is being developed to compute sentence similarity using different formulations.

Methods
------------

mihalcea_sentence_similarity(sentence1, sentence2)

"""

from wordnet import WordNet

def mihalcea_sentence_similarity(sentence1, sentence2):
    """
    Computes the sentence similarity propesed by Mihalcea using word to word similarity.

    Parameters
    ----------
    sentence1 : str
        sentence1 to be compared to sentence2
                
    sentence2 : str
        sentence2 to be compared to sentence1
    """

    wordNet = WordNet()
    return (wordNet.sentence_similarity(sentence1, sentence2) + wordNet.sentence_similarity(sentence2, sentence1)) / 2 
 

    


