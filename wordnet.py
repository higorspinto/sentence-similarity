from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag

from WSD import WSD
from WSD import FirstSynset

class WordNet:

    """
    This class contains all methods that call wordnet routines.

    Attributes
    ----------

    Methods
    -------

    penn_to_wn(tag)
        Convert between a Penn Treebank tag to a simplified Wordnet tag. 


    """

    def penn_to_wn(self, tag):
        """ 
        Convert between a Penn Treebank tag to a simplified Wordnet tag. 

        Parameters
        ----------

        tag : str
            The tag that will be converted for WordNet tag format.

        """

        #nltk.pos_tag function returns tags on notation of Penn Treebank.
        #https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

        if tag.startswith('N'):
            return 'n'
 
        if tag.startswith('V'):
            return 'v'
 
        if tag.startswith('J'):
            return 'a'
 
        if tag.startswith('R'):
            return 'r'
 
        return None

    def tagged_to_synset(self, word, tag):

        """ 
        Returns the synset of the word that matches the tag.
        
        Parameters
        ----------
        
        word : str
        tag : str

        """

        wsd = FirstSynset()

        wn_tag = self.penn_to_wn(tag)
        if wn_tag is None:
            return None

        try:
            synsets = wn.synsets(word, wn_tag)
            wsd_synset = wsd.disambiguation(synsets)
            return wsd_synset
        except:
            return None
    
    def sentence_similarity(self, sentence1, sentence2):
        
        """
        Calculate the similarity betwenn two sentences using wordnet.

        This algorithm was proposed by Mihalcea et al.
        Paper: https://pdfs.semanticscholar.org/1374/617e135eaa772e52c9a2e8253f49483676d6.pdf

        Parameters
        ----------

        sentence1 : str
            sentence1 to be compared to sentence2
                
        sentence2 : str
            sentence2 to be compared to sentence1

        """

        #Implementation based on this post:
        #https://nlpforhackers.io/wordnet-sentence-similarity/


        # Tokenize and tag
        sentence1 = pos_tag(word_tokenize(sentence1))
        sentence2 = pos_tag(word_tokenize(sentence2))
 
        # Get the synsets for the tagged words
        synsets1 = [self.tagged_to_synset(*tagged_word) for tagged_word in sentence1]
        synsets2 = [self.tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
        # Filter out the Nones
        synsets1 = [ss for ss in synsets1 if ss]
        synsets2 = [ss for ss in synsets2 if ss]
 
        score, count = 0.0, 0
 
        # For each word in the first sentence
        for synset in synsets1:
            # Get the similarity value of the most similar word in the other sentence
            best_score = max([synset.path_similarity(ss) for ss in synsets2])
 
            # Check that the similarity could have been computed
            if best_score is not None:
                score += best_score
                count += 1
 
        # Average the values
        score /= count
        return score