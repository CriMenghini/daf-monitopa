# server.py
import flask
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
import operator
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
import operator
import pandas as pd
from src.update_page import *


app = Flask(__name__, static_folder='web-ui/build', template_folder='web-ui/build')
CORS(app)


@app.route("/api_dati_tweet", methods=['GET', 'POST'])
def hello():
    data = json.load(open('data/raw/outputfile.json'))
    with open('data/raw/aa.pkl', 'rb') as f:
        id_sentiment = pickle.load(f)

    #print (request.method)

    # Get info about tweets (@TODO salva questi risultati in file, non calcolarli ad ogni request)
    dictionary_tweet = tweet_info(data)
    list_hashtags, non_set, hashtags_dict, count_hashtags = get_list_significant_hashtag(dictionary_tweet, threshold=5)
    lista_tweet_per_hash = tweets_hashtag(hashtags_dict)
    hashtags_dict, dict_hashtag, dict_list_hashtag = tweet_hashtags(hashtags_dict, list_hashtags)

    if request.method == 'GET':
        print ('SONO ANDATO IN GET')
        return render_template('index.html')#flask.send_from_directory('build', 'index.html')#


    else:

        hashtag = request.get_json()["selectedHashtag"]
        print (hashtag)

        # Compute the number of tweets for the hashtag
        lista_tweet = lista_tweet_per_hash[hashtag]
        num_tweet = len(set(lista_tweet))

        # Get the sentiment of tweets
        list_vector_pie = sentiment_tweet(lista_tweet, id_sentiment)

        # Top users
        list_user_to_plot = top_users(data, lista_tweet)

        # Stream tweet
        sent_sub_tweet = {i: id_sentiment[i] for i in lista_tweet}
        lista_tweet_pos = [i for i,j in sent_sub_tweet.items() if j=='positive']
        lista_tweet_neg = [i for i,j in sent_sub_tweet.items() if j=='negative']
        lista_tweet_neu = [i for i,j in sent_sub_tweet.items() if j=='neutral']


        # Utenti unici
        list_unici_utenti = unique_users(data, lista_tweet)

        task = {
            'numTweet': num_tweet,
            'NumRetweet':  retweet_based_on_hashtag(hashtag, dict_hashtag, data),
            'Sentiment':list_vector_pie,
            'Unique': list_unici_utenti,
            'StreamPos': stream_tweet(data,lista_tweet_pos),
            'StreamNeg': stream_tweet(data,lista_tweet_neg),
            'StreamNeu': stream_tweet(data,lista_tweet_neu),
            'dataSet': list_user_to_plot}
        return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)
