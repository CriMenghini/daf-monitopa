from collections import defaultdict, OrderedDict
import json
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
import collections
import operator


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
                        tweets += [(p.clean(data_small[i]['text']), data_small[i]['retweet_count'],
                                    data_small[i]['retweeted_status']['user']['name'],
                                    data_small[i]['retweeted_status']['user']['id'],
                                    data_small[i]['retweeted_status']['user']['followers_count'],
                                    data_small[i]['retweeted_status']['user']['friends_count'])]
            except:
                if data_small[i]['id'] in top_10:
                    if data_small[i]['id'] not in find_id:
                        find_id += [data_small[i]['id']]
                        tweets += [(p.clean(data_small[i]['text']), data_small[i]['retweet_count'], data_small[i]['user']['name'],
                                   data_small[i]['user']['id'], data_small[i]['user']['followers_count'],
                                   data_small[i]['user']['friends_count'])]
        else:
            break

    tweets = sorted(tweets, key=lambda x: x[1], reverse=True)

    # List top
    list_retweet = []
    # Get info

    # for ind, t, rt, u, uid, fol, frien in enumerate(tweets):
    for ind, (t, rt, u, uid, fol, frien) in enumerate(tweets):
        retweet_output_dict = {}
        # retweet_output_dict[t] = {}
        retweet_output_dict['x'] = ind + 1
        retweet_output_dict['y'] = rt
        retweet_output_dict['label'] = t + "\nAutore: " + str(u) + "\nFollowers: " + str(fol)
        list_retweet += [retweet_output_dict]

    #f = open('web-ui/src/data/TopRetweet.js', 'w')
    #f.write('var Retweet = ' + repr(list_retweet))
    #f.write('\n')
    #f.write('export default Retweet')
    #f.close()
    return list_retweet


    
    
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

    list_retweet = top_10_rt(data_hashtag, hashtag)
    return list_retweet
    
    
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

    list_retweet = top_10_rt(data_hashtag, topic)
    return list_retweet

def co_occurrences_tweet(hashtags_dict):
    co_hash_occ = defaultdict(list)
    for i, j in hashtags_dict.items():
        for el in j:
            j.remove(el)
            co_hash_occ[el] += j

    counter_hash = {}
    for i, j in co_hash_occ.items():
        counter_hash[i] = sorted(collections.Counter(j).items(), key=operator.itemgetter(1), reverse=True)

    return counter_hash