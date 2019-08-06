""" 
Setence Similarity

Sentence similarity is a common task in NLP.
This module is being developed to compute sentence similarity using different formulations.

"""

from wordnet import WordNet

def mihalcea_sentence_similarity(self, sentence1, sentence2):
    """
    Computes the sentence similarity using word to word similarity.
    This formulation was proposed by Mihalcea et al.
    Paper: https://pdfs.semanticscholar.org/1374/617e135eaa772e52c9a2e8253f49483676d6.pdf

    Parameters
    ----------
    sentence1 : str
                
    sentence2 : str
    """

    wordNet = WordNet()
    return (wordNet.sentence_similarity(sentence1, sentence2) + wordNet.sentence_similarity(sentence2, sentence1)) / 2 
 

    


