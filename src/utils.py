import operator
import numpy as np
from collections import defaultdict

def get_user_attr(id_, dictionary_tweet, tweet, attr, user = True):
    """the function return the attr of the tweet and put it in the dictionary related to the tweet
    @tweet_id: id 
    @dictionary_to_update: dictionary (key,value):(tweet_id, (key,value):(attr,value))
    @tweet: who tweet"""
    
    if user:
         dictionary_tweet[id_][attr] = tweet['user'][attr]
    else:
        dictionary_tweet[id_][attr] = tweet[attr]
        
    return dictionary_tweet



def FindHashHags(tweet):
    """
    This function takes the twittersearch output tweet,
    cleans up the text and the format, and returns
    the set of all hashtags in the tweet
    """
    # First get the tweet text
    tweettxt = str(tweet.encode('ascii','ignore'))
    
    # Add spacing before the hashtag symbol
    tweettxt = tweettxt.replace('#',' #')
    
    # Clean all punctuation 
    for punct in '\.!",;:%<>/~@`()[]{}?-':
        tweettxt = tweettxt.replace(punct,' ')
    
    # Split the tweet 
    tweettxt = tweettxt.split()
    
    # List of hashtags
    hashtags = []
    # Loop over the words in the tweet
    for word in tweettxt:
        # Find words beginning with hashtag
        if word[0]=='#':

            hashtag = word.lower()
            # Correct for possisives
            hashtag= hashtag.split('\'')[0]         
            
            # Get rid of the hashtag symbol
            hashtag = hashtag.replace('#','')
            # Check existence of word after #
            if len(hashtag)>0:
                hashtags.append(hashtag)
    
    return hashtags


def tweet_info(data):
    dictionary_tweet = {}
    list_attr_user = ['description','favourites_count','followers_count','friends_count','location','screen_name']
    list_attr = ['text', 'retweeted']

    for t in data:
        id_ = t['id']
        dictionary_tweet[id_] = {}

        # Extract attribute related to the tweet
        for attr in list_attr:
            dictionary_tweet = get_user_attr(id_, dictionary_tweet, t, attr, user = False)

        # Get info of the user 
        for attr in list_attr_user:
            dictionary_tweet = get_user_attr(id_, dictionary_tweet, t, attr)
            
    return dictionary_tweet



def get_list_significant_hashtag(dictionary_tweet, threshold=5):
    
    list_hashtags = []

    # Dizionari che definisce per ogni tweet la lista degli hashtag
    hashtags_dict = defaultdict(list)

    # For each tweet
    for id_ in dictionary_tweet:
        # Define the list of hashtags
        list_h = FindHashHags(dictionary_tweet[id_]['text'])
        hashtags_dict[id_] += list_h
        list_hashtags += list_h

    # List of hashtags
    non_set = list_hashtags
    # Set of hashtags
    list_hashtags = list(set(list_hashtags))
    
    ### Keep significant
    count_hashtags = defaultdict(int)
    for i in non_set:
        count_hashtags[i] += 1
    
    revome_one_hash = {i:j for i,j in count_hashtags.items() if j > threshold and len(i)>1}
    list_hashtags = list(revome_one_hash.keys())
    ######
    
    return list_hashtags, non_set, hashtags_dict, count_hashtags



def tweet_hashtags(hashtags_dict, list_hashtags):
    
    hashtags_dict = {i: [k for k in j if k in list_hashtags] for i,j in hashtags_dict.items()}
    
    dict_hashtag = defaultdict(list)
    #list_id_toscana = []
    for tag in list_hashtags:
        for i, l in hashtags_dict.items():
            if tag in l:
                dict_hashtag[tag] += [i] 
    
    dict_list_hashtag = defaultdict(list)
    #list_id_toscana = []
    for tag in list_hashtags:
        for i, l in hashtags_dict.items():
            if tag in l:
                dict_list_hashtag[tag] += [j for j in l if j!=tag and j in list_hashtags]       
    
    return hashtags_dict, dict_hashtag, dict_list_hashtag
    
    
    
def drop_duplicates(data, dict_hashtag, hashtags_dict):
    tweet_unique = defaultdict(int)

    for i in range(len(data)):
        try:
            tweet_unique[data[i]['retweeted_status']['id']] += 1
        except:
            tweet_unique[data[i]['id']] += 1
            
    list_tweet = list(tweet_unique.keys())
            
    dict_hashtag_2 = defaultdict(list)
    for i,l_t in dict_hashtag.items():
        #print (i)
        dict_hashtag_2[i] += [l for l in l_t if l in list_tweet]
    
    h_dict = {}
    for t in hashtags_dict.keys():
        if t in list_tweet:
            h_dict[t] = hashtags_dict[t]

   
            
    return list_tweet, dict_hashtag_2, h_dict