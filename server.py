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
#import preprocessor as p
#p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
import operator
import pandas as pd


app = Flask(__name__, static_folder='web-ui/build', template_folder='web-ui/build')
CORS(app)


def tweets_hashtag(hashtags_dict):
    list_tweet_hash = copy.deepcopy(hashtags_dict)
    lista_tweet_per_hash = defaultdict(list)
    for i, j in list_tweet_hash.items():
        for k in j:
            lista_tweet_per_hash[k] += [i]

    return lista_tweet_per_hash


def sentiment_tweet(lista_esempio_tweet, id_sentiment):
    counter = collections.Counter({i: j for i, j in id_sentiment.items() if i in lista_esempio_tweet}.values())

    list_vector_pie = []
    tot = sum(list(counter.values()))
    for k,v in counter.items():
        if k == 'negative':
            list_vector_pie += [{'x': 2, 'y': round(v/tot*100,1)}]
        elif k == 'positive':
            list_vector_pie += [{'x': 1, 'y': round(v/tot*100,1)}]
        elif k == 'neutral':
            list_vector_pie += [{'x': 3, 'y': round(v/tot*100,1)}]

    return list_vector_pie


def top_users(data, lista_tweet):
    data__ = []
    for i in range(len(data)):
        if data[i]['id'] in lista_tweet:
            data__ += [data[i]]

    count_user_tweet = defaultdict(int)
    for i in range(len(data__)):
        count_user_tweet[data__[i]['user']['id']] += 1
    top_10 = [w for w in sorted(count_user_tweet, key=count_user_tweet.get, reverse=True)[:10]]

    find_id = []
    info_user = {}

    for i in range(len(data)):

        if data[i]['user']['id'] in top_10:
            if len(set(find_id)) < 11:
                info_user[data[i]['user']['id']] = {}
                info_user[data[i]['user']['id']]['followers_count'] = data[i]['user']['followers_count']
                #info_user[data[i]['user']['id']]['favourites_count'] = data[i]['user']['favourites_count']
                info_user[data[i]['user']['id']]['description'] = data[i]['user']['description']
                #info_user[data[i]['user']['id']]['location'] = data[i]['user']['location']
                info_user[data[i]['user']['id']]['name'] = data[i]['user']['name']
                #info_user[data[i]['user']['id']]['lang'] = data[i]['user']['lang']

            find_id += [data[i]['user']['id']]
    sorted_x = sorted(count_user_tweet.items(), key=operator.itemgetter(1), reverse=True)

    list_user_to_plot = []
    counter_ = 0
    for i, count in sorted_x:
        try:
            list_user_to_plot += [{'x': counter_ + 1, 'y': count,
                                   'label': 'User: ' + info_user[i]['name'] + '\nDescription: ' +
                                       info_user[i]['description'] + '\nFollowers: ' + str(
                                       info_user[i]['followers_count'])}]
            counter_ += 1
        except:
            continue

    return list_user_to_plot


def stream_tweet(data,lista_esempio_tweet):
    data__ = []
    for i in range(len(data)):
        if data[i]['id'] in lista_esempio_tweet:
            data__ += [data[i]]

    list_date = []
    for i in range(len(data__)):

        list_date += [data__[i]['created_at']]

        try:
            list_date += [data__[i]['retweeted_status']['created_at']]
        except:
            continue

    ts = pd.to_datetime(list_date)
    ts_list = []
    for a in ts:
        t = str(a)
        t_day = t[:10]
        t_hour = t[10:13] + ':00:00'
        t_rest = t[19:]

        ts_list += [t_day + t_hour + t_rest]

    ts = pd.to_datetime(ts_list)
    df = pd.DataFrame()
    df['Time'] = ts
    df['freq'] = [1] * len(ts)

    grouped = df.groupby('Time').sum()
    list_hours = []
    for i in grouped.index:
        list_hours += [{'a': str(i), 'b': int(grouped.loc[i][0])}]
        # ['freq']

    return list_hours

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


        print (stream_tweet(data,lista_tweet_pos))
        print (stream_tweet(data,lista_tweet_neg))
        print (stream_tweet(data,lista_tweet_neu))

        task = {
            'numTweet': num_tweet,
            'NumRetweet':  retweet_based_on_hashtag(hashtag, dict_hashtag, data),
            'Sentiment':list_vector_pie,
            'Unique': [{ 'x': 11, 'y': 14 },{ 'x': 2, 'y': 10},{ 'x': 3, 'y': 9 },{ 'x': 4, 'y': 3 },{ 'x': 5, 'y': 7 }],
            'StreamPos': stream_tweet(data,lista_tweet_pos),
            'StreamNeg': stream_tweet(data,lista_tweet_neg),
            'StreamNeu': stream_tweet(data,lista_tweet_neu),
            'dataSet': list_user_to_plot}
        return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)
