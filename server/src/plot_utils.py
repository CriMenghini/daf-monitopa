from collections import defaultdict, OrderedDict
import json 


def top_10_rt(data, name):

    data_small = []
    dictionary_retweet = {}
    for t in range(len(data)):
        n_retweet = data[t]['retweet_count']

        if n_retweet > 0:
            try:
                dictionary_retweet[data[t]['retweeted_status']['id']] = n_retweet
            except:
                dictionary_retweet[data[t]['id']] = n_retweet

            data_small += [data[t]]
            
    top_10 = [w for w in sorted(dictionary_retweet, key=dictionary_retweet.get, reverse=True)[:10]]
    
    find_id = []
    tweets = []

    for i in range(len(data_small)):
        if len(set(find_id)) < 10:
            try:
                if data_small[i]['retweeted_status']['id'] in top_10:

                    if data_small[i]['retweeted_status']['id'] not in find_id:
                        find_id += [data_small[i]['retweeted_status']['id']]
                        tweets += [(data_small[i]['text'], data_small[i]['retweet_count'], data_small[i]['retweeted_status']['user']['name'], data_small[i]['retweeted_status']['user']['id'], data_small[i]['retweeted_status']['user']['followers_count'], data_small[i]['retweeted_status']['user']['friends_count'])]
            except:
                if data_small[i]['id'] in top_10:
                    if data_small[i]['id'] not in find_id:
                        find_id += [data_small[i]['id']]
                        tweets += [(data_small[i]['text'], data_small[i]['retweet_count'], data_small[i]['user']['name'], data_small[i]['user']['id'], data_small[i]['user']['followers_count'], data_small[i]['user']['friends_count'])]
        else: break
            
    
    tweets = sorted(tweets, key=lambda x: x[1], reverse = True)
    # Get info
    retweet_output_dict = OrderedDict()
    for t, rt, u, uid, fol, frien in tweets:
        retweet_output_dict[t] = {}
        retweet_output_dict[t]['num_RT'] = rt
        retweet_output_dict[t]['user'] = u
        retweet_output_dict[t]['user_id'] = uid
        retweet_output_dict[t]['user_followers'] = fol
        retweet_output_dict[t]['user_friends'] = frien
    
    f = open( 'data/out/top_retweet_'+ name +'.js', 'w' )
    f.write( 'var dataset = ' + repr(retweet_output_dict))
    f.close()
    
    
def retweet_based_on_hashtag(hashtag, dict_hashtag, data):
    
    id_tweets = dict_hashtag[hashtag]
    print (id_tweets)
    data_hashtag = []
    for i in range(len(data)):
        if data[i]['id'] in id_tweets:
            data_hashtag += [data[i]]
        else:
            try:
                if data[i]['retweeted_status']['id'] in id_tweets:
                    data_hashtag += [data[i]]
            except: continue
    
    top_10_rt(data_hashtag, hashtag)
    
    
def retweet_based_on_topic(topic, class_tweet, data):
    
    id_tweets = class_tweet[topic]
    print (id_tweets)
    data_hashtag = []
    for i in range(len(data)):
        if data[i]['id'] in id_tweets:
            data_hashtag += [data[i]]
        else:
            try:
                if data[i]['retweeted_status']['id'] in id_tweets:
                    data_hashtag += [data[i]]
            except: continue
    
    top_10_rt(data_hashtag, topic)