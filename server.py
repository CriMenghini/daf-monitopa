import itertools
from flask_cors import CORS
from collections import defaultdict
from flask import Flask, render_template, request, jsonify

from src.classes import Tweet, TweetCollection, Hashtag,\
                        GraphHashtag, Topic,\
                        data, vocabolario_lexicon, vocabolario_index_twitter

from src.metrics import get_top_retweet, sentiment_percentage,\
                        manipulate_date, unique_cumulative_users,\
                        unique_cumulative_users, stream_tweet,\
                        get_list_hashtags, co_occurrences


app = Flask(__name__,
            static_folder='web-ui/build',
            template_folder='web-ui/build')
CORS(app)



"""Simulazione dell'arrivo dei tweet"""
list_id_tweet = []
list_hashtags = []
collection_totale = []
edges_weight = defaultdict(int)

for tweet in data:

    object_tweet = Tweet(tweet, vocabolario_lexicon,
                         vocabolario_index_twitter)
    tweet_attr = object_tweet.__dict__
    id_tweet = tweet_attr['id_tweet']
    list_hashtag = tweet_attr['list_hashtags']

    if id_tweet not in list_id_tweet:
        list_id_tweet += [id_tweet]
        collection_totale += [object_tweet]
        list_hashtags += list_hashtag
        choose_two_hashtag = list(
            itertools.combinations(list_hashtag, 2))
        for edge in choose_two_hashtag:
            edges_weight[tuple(sorted(edge))] += 1

    else:
        idx_object = list_id_tweet.index(id_tweet)
        object_to_mod = collection_totale[idx_object]
        object_to_mod._updateNumberRetweet(tweet)
        object_to_mod._updateListUserRetweet(tweet)
        collection_totale[idx_object] = object_to_mod

with open('web-ui/src/data/listaHash.js', 'w') as outfile:
    outfile.write('export default [')
    max_name = len(set(list_hashtags))
    for idx, t in enumerate(list(set(list_hashtags))):
        if idx != max_name - 1:
            outfile.write("'" + t + "'" + ',\n')
        else:
            outfile.write("'" + t + "'" + ']')


Graph = GraphHashtag(edges_weight, collection_totale, False)


@app.route("/", methods=['GET'])
def landing():
    if request.method == 'GET':
        print('SONO ANDATO IN GET')
        return render_template('index.html')

@app.route("/hashtag_api", methods=['POST'])
def hashtag_api():

    hashtag = request.get_json()["selectedHashtag"]

    # Compute the number of tweets for the hashtag
    obj_hashtag = Hashtag(hashtag, collection_totale)
    hashtag = obj_hashtag.__dict__
    lista_tweet = hashtag['lista_tweet'][0]

    num_tweet = len(lista_tweet)
    top_retweet = get_top_retweet(lista_tweet)
    list_vector_pie = sentiment_percentage(lista_tweet)
    list_unici_utenti = unique_cumulative_users(lista_tweet)
    stream_neg = stream_tweet(lista_tweet, 'negative')
    stream_pos = stream_tweet(lista_tweet, 'positive')
    lista_diz_hash = co_occurrences(get_list_hashtags(lista_tweet))

    task = {
        'numTweet': num_tweet,
        'NumRetweet': top_retweet,
        'Sentiment':list_vector_pie,
        'Unique': list_unici_utenti,
        'StreamPos': stream_pos,
        'StreamNeg': stream_neg,
        'dataSet': lista_diz_hash}
    return jsonify(task)


@app.route("/topic_api", methods=['POST'])
def topic_api():

    tag = request.get_json()["selectedHashtag"]

    topic = Topic(Graph.__dict__['tweet_clusters'], tag)

    lista_tweet = topic.__dict__['tweet_topic']
    num_tweet = len(lista_tweet)
    top_retweet = get_top_retweet(lista_tweet)
    list_vector_pie = sentiment_percentage(lista_tweet)
    list_unici_utenti = unique_cumulative_users(lista_tweet)
    stream_neg = stream_tweet(lista_tweet, 'negative')
    stream_pos = stream_tweet(lista_tweet, 'positive')
    lista_diz_hash = co_occurrences(get_list_hashtags(lista_tweet))

    task = {
        'numTweet': num_tweet,
        'NumRetweet': top_retweet,
        'Sentiment':list_vector_pie,
        'Unique': list_unici_utenti,
        'StreamPos': stream_pos,
        'StreamNeg': stream_neg,
        'dataSet': lista_diz_hash}
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
