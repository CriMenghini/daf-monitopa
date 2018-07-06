import json
import string


def normalize(x):
    """This function normalizes the review's text. In particular,
    1. remove the punctuation
    2. lower case"""
    
    # Dictionary of punctuation
    punct_table = {ord(char):' ' for char in string.punctuation}
        
    # Remove punctuation
    s = x.translate(punct_table)
    s = ' '.join(w.lower() for w in s.split() if len(w)>1)
    return s


vocabolario = json.load(open('data/lexicon_polarity.json'))
valid_string = [w for w in list(vocabolario.keys()) if type(w)==str]
lista_parole_uniche = [w for w in list(valid_string) if len(w.split('_'))<=1]
lista_espressioni = [w for w in list(valid_string) if len(w.split('_'))>1]

vocabolario_index_twitter = json.load(open('data/vocabolario_twitter.json'))

def substitute_label_(x, voc_lexicon):
    """Substitute words with tag pos, neg, neu.
    ------------------------------------------------------------

    This operation requires some times especially when the
    length of the text increases.
    """

    l = set(lista_parole_uniche).intersection(set(x))
    return ' '.join([voc_lexicon[i] if i in l else i for i in x])


def replace_word_index_twitter_(x, vocabolario_index_twitter):
    """Given a list of words it returns the list of indeces"""
    
    return [vocabolario_index_twitter[w] for w in x if w in vocabolario_index_twitter.keys()]
