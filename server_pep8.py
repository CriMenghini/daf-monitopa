import json

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from classes import Tweet, TweetCollection, Hashtag, HashtagCollection


app = Flask(__name__, static_folder='web-ui/build',
            template_folder='web-ui/build')
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
                for tweet in list_tweets_object}
hash_collection = HashtagCollection(hashtags_dict)
lista_tweet_per_hash = hash_collection.get_list_tweet()
dict_hashtag = lista_tweet_per_hash
dict_list_hashtag, counter_hash = hash_collection.get_co_occurent_list_tweet()
list_tweet = list(hashtags_dict.keys())

