import json

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from src.classes import Tweet, TweetCollection, Hashtag, HashtagCollection
from flask import Flask, render_template, request, jsonify
import json
from src.utils import *
from src.topic_clustering import *
from src.plot_utils import *
from flask_cors import CORS
import copy
import os
import collections
import pickle
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
import pandas as pd
import collections
from src.preprocessing import *
from src.update_page import *
from collections import defaultdict
from keras.models import model_from_json
from keras.preprocessing import sequence
import numpy as np

app = Flask(__name__, static_folder='web-ui/build', template_folder='web-ui/build')
CORS(app)

data = json.load(open('data/raw/outputfile.json'))

# Minimal computations for tweets handling
list_tweets_object = [Tweet(data[i]) for i in range(len(data))]
collection_tweets = TweetCollection(list_tweets_object)
list_total_hashtag = collection_tweets.get_list_hashtags()[1]

# Retweet occurrences are not included
count_hashtags = collection_tweets.get_clean_hashtag_occurrences(list_total_hashtag)
list_hashtags = list(count_hashtags.keys())
hashtags_dict = {tweet.get_id_tweet(): tweet.get_hashtag()
                for tweet in list_tweets_object
                }
hash_collection = HashtagCollection(hashtags_dict)
lista_tweet_per_hash = hash_collection.get_list_tweet()
dict_hashtag = lista_tweet_per_hash
dict_list_hashtag, counter_hash =hash_collection.get_co_occurent_list_tweet()
list_tweet = list(hashtags_dict.keys())









############################################################################################
####################### Topics #######################
tuples_weights = edges(dict_list_hashtag, occurrences=False, jaccard=True)
G = graph_hashtags(tuples_weights)

# Assign id
id_hash = {i: j for i, j in enumerate(list_hashtags)}
hash_id = {j: i for i, j in id_hash.items()}

dimensionality_reduct, num_components = dimensionality_reduction(G)
clusters = clustering(dimensionality_reduct)
class_hash, class_num_hash = create_cluster(G, clusters)

set_tweets_class, set_hash_class = tweet_in_class(class_hash, class_num_hash, dict_hashtag, hashtags_dict)
class_of_tweets, dict_tweet_prop_class, tweet_belongs_to = assign_tweet(list_tweet, hashtags_dict, class_num_hash,
                                                                        class_hash)

### Per prendere gli id dei tweet del topic devo matchare nome e numero topic
output = []
for cluster, list_hash in class_hash.items():
    dictionary = {}
    dictionary['topic'] = int(cluster)
    dict_ha = {i: count_hashtags[i] for i in list_hash}
    dictionary['hashtags'] = [(i, count_hashtags[i]) for i in sorted(dict_ha, key=dict_ha.get, reverse=True)]
    dictionary['number_tweets'] = len(set(class_of_tweets[cluster]))

    output += [dictionary]

dict_topic_hash = defaultdict(list)
for i in output:
    dict_topic_hash[i['topic']] += [j for j in i['hashtags']]

name_topic = {i: j[0][0] for i, j in dict_topic_hash.items()}
print (name_topic)
topic_nome = {j:i for i,j in name_topic.items()}

with open('web-ui/src/data/name_topic.js', 'w') as outfile:
    outfile.write('export default [')
    max_name = len(name_topic)
    for idx, t in enumerate(list(topic_nome.keys())):
        if idx != max_name - 1:
            outfile.write("'"+t+"'"+',\n')
        else:
            outfile.write("'"+t+"'" + ']')
    #json.dump(name_topic, outfile)


############################## Sentiment model ######################################
# load json and create model
json_file = open('src/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("src/model.h5")
print("Loaded model from disk")

#################################### Pre-process Tweets ################################
index_vocabolario = {idx:w for w, idx in vocabolario_index_twitter.items()}

id_text_pad_list = []
for i in range(len(data)):
    try:
        id_text_pad_list += [(data[i]['id'], replace_word_index_twitter((substitute_label((normalize(p.tokenize(data[i]['retweeted_status']['text']))).split())).split()))]
    except:
        id_text_pad_list += [(data[i]['id'], replace_word_index_twitter((substitute_label((normalize(p.tokenize(data[i]['text']))).split())).split()))]


array_pad = np.array([j for i,j in id_text_pad_list])
padding = sequence.pad_sequences(array_pad, maxlen=40, padding='post')
prediction = loaded_model.predict_classes(padding)
pred = ['negative' if i==0 else 'positive' for i in prediction ]
dict_id_sentiment = {}
for i,j in enumerate(array_pad):
    dict_id_sentiment[id_text_pad_list[i][0]] = pred[i]

@app.route("/", methods=['GET'])
def landing():
    if request.method == 'GET':
        print('SONO ANDATO IN GET')
        return render_template('index.html')

@app.route("/hashtag_api", methods=['POST'])
def hashtag_api():
    #if request.method == 'GET':
    #    print ('SONO ANDATO IN GET')
    #    return render_template('index.html')


    #else:

    hashtag = request.get_json()["selectedHashtag"]
    print (hashtag)

    # Compute the number of tweets for the hashtag
    lista_tweet = lista_tweet_per_hash[hashtag]
    num_tweet = len(set(lista_tweet))

    # Get the sentiment of tweets
    list_vector_pie = sentiment_tweet(lista_tweet, dict_id_sentiment)#id_sentiment)
    print (list_vector_pie)
    # Top users
    #list_user_to_plot = top_users(data, lista_tweet)
    lista_diz_hash = []
    for i, j in enumerate(counter_hash[hashtag][:10]):
        lista_diz_hash += [{'x': i + 1, 'y': j[1], 'label': '#' + j[0]}]

    print (lista_diz_hash)

    # Stream tweet
    sent_sub_tweet = {i: dict_id_sentiment[i] for i in lista_tweet}
    lista_tweet_pos = [i for i,j in sent_sub_tweet.items() if j=='positive']
    lista_tweet_neg = [i for i,j in sent_sub_tweet.items() if j=='negative']
    #lista_tweet_neu = [i for i,j in sent_sub_tweet.items() if j=='neutral']


    # Utenti unici
    list_unici_utenti = unique_users(data, lista_tweet)


    task = {
        'numTweet': num_tweet,
        'NumRetweet': retweet_based_on_hashtag(hashtag, dict_hashtag, data),
        'Sentiment':list_vector_pie,
        'Unique': list_unici_utenti,
        'StreamPos': stream_tweet(data,lista_tweet_pos),
        'StreamNeg': stream_tweet(data,lista_tweet_neg),
        #'StreamNeu': stream_tweet(data,lista_tweet_neu),
        'dataSet': lista_diz_hash}
    return jsonify(task)


@app.route("/topic_api", methods=['POST'])
def topic_api():
    #if request.method == 'GET':
    #    print ('SONO ANDATO IN GET')
    #    return render_template('index.html')


    #else:

    hashtag = request.get_json()["selectedHashtag"]
    print (hashtag)

    # Compute the number of tweets for the hashtag
    lista_tweet = class_of_tweets[topic_nome[hashtag]]
    num_tweet = len(set(lista_tweet))

    # Get the sentiment of tweets
    list_vector_pie = sentiment_tweet(lista_tweet, dict_id_sentiment)

    # Top users
    #list_user_to_plot = top_users(data, lista_tweet)
    lista_diz_hash = []
    for i, j in enumerate(dict_topic_hash[topic_nome[hashtag]][:10]):
        lista_diz_hash += [{'x': i +1, 'y': j[1], 'label': '#' + j[0]}]

    print (lista_diz_hash)

    # Stream tweet
    sent_sub_tweet = {i: dict_id_sentiment[i] for i in lista_tweet}
    lista_tweet_pos = [i for i,j in sent_sub_tweet.items() if j=='positive']
    lista_tweet_neg = [i for i,j in sent_sub_tweet.items() if j=='negative']
    #lista_tweet_neu = [i for i,j in sent_sub_tweet.items() if j=='neutral']


    # Utenti unici
    list_unici_utenti = unique_users(data, lista_tweet)
    print (retweet_based_on_topic(topic_nome[hashtag], class_of_tweets, data))

    task = {
        'numTweet': num_tweet,
        'NumRetweet': retweet_based_on_topic(topic_nome[hashtag], class_of_tweets, data),
        'Sentiment':list_vector_pie,
        'Unique': list_unici_utenti,
        'StreamPos': stream_tweet(data,lista_tweet_pos),
        'StreamNeg': stream_tweet(data,lista_tweet_neg),
        #'StreamNeu': stream_tweet(data,lista_tweet_neu),
        'dataSet': lista_diz_hash}
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
