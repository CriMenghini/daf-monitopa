# server.py
from flask import Flask, render_template, request
import json
from src.utils import *
from src.topic_clustering import *
from src.plot_utils import *




app = Flask(__name__, static_folder='../static/src' ,template_folder='../static/public')

@app.route("/home", methods=['GET', 'POST'])
def choose_hashtag():

    data = json.load(open('data/raw/outputfile.json'))

    # Get info about tweets (@TODO salva questi risultati in file, non calcolarli ad ogni request)
    dictionary_tweet = tweet_info(data)
    list_hashtags, non_set, hashtags_dict, count_hashtags = get_list_significant_hashtag(dictionary_tweet, threshold=5)
    hashtags_dict, dict_hashtag, dict_list_hashtag = tweet_hashtags(hashtags_dict, list_hashtags)

    if request.method == 'POST':
        hashtag = request.form['hashtag']
        retweet_based_on_hashtag(hashtag, dict_hashtag, data)
        return render_template('chosen_hashtag.html', hashtag=hashtag)
	    
    return render_template('prova.html')

@app.route("/hello")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
