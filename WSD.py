class WSD:
    '''
    Word Sense Disambiguation

    In this class we define some classes to implement different kinds os disambiguation.

    Methods
    --------------

    disambiguation(synsets):
        returns the appropriate synset after disambiguation process
    '''

    def disambiguation(self, synsets):
        raise NotImplementedError("Subclass must implement abstract method")
    
class FirstSynset(WSD):

    '''
    This class returns the first synset of a list of synsets for a word on wordnet.
    The first synset is the most common sense of the word in a list of synsets.

    Methods
    --------------

    disambiguation(synsets):
        returns the appropriate synset after disambiguation process    
    '''

    def disambiguation(self, synsets):
        '''
        Returns the appropriate synset after disambiguation process.

        parameteres
        -----------
        synsets: list
            a list of synsets
        '''  
        return synsets[0]