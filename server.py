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


app = Flask(__name__, static_folder='web-ui/build', template_folder='web-ui/build')
CORS(app)

#@app.route('/', defaults={'path': ''})


#@app.route('/<path:path>')
#def serve(path):
#    print (path)
#    if path != "" and os.path.exists("build" + path):
#        return flask.send_from_directory('build/', path)
#    else:
#        return flask.send_from_directory('build', 'index.html')

def tweets_hashtag(hashtags_dict):
    list_tweet_hash = copy.deepcopy(hashtags_dict)
    lista_tweet_per_hash = defaultdict(list)
    for i, j in list_tweet_hash.items():
        for k in j:
            lista_tweet_per_hash[k] += [i]

    return lista_tweet_per_hash



@app.route("/home", methods=['GET', 'POST'])
def choose_hashtag():

    data = json.load(open('data/raw/outputfile.json'))

    # Get info about tweets (@TODO salva questi risultati in file, non calcolarli ad ogni request)
    dictionary_tweet = tweet_info(data)
    list_hashtags, non_set, hashtags_dict, count_hashtags = get_list_significant_hashtag(dictionary_tweet, threshold=5)
    hashtags_dict, dict_hashtag, dict_list_hashtag = tweet_hashtags(hashtags_dict, list_hashtags)

    if request.method == 'POST':
        print (request.form)
        hashtag = request.form['hashtag']
        retweet_based_on_hashtag(hashtag, dict_hashtag, data)
        return render_template('chosen_hashtag.html', hashtag=hashtag)
	    
    return render_template('prova.html')






@app.route("/api_dati_tweet", methods=['GET', 'POST'])
def hello():
    data = json.load(open('data/raw/outputfile.json'))
    #print (request.method)

    # Get info about tweets (@TODO salva questi risultati in file, non calcolarli ad ogni request)
    dictionary_tweet = tweet_info(data)
    list_hashtags, non_set, hashtags_dict, count_hashtags = get_list_significant_hashtag(dictionary_tweet, threshold=5)
    lista_tweet_per_hash = tweets_hashtag(hashtags_dict)
    hashtags_dict, dict_hashtag, dict_list_hashtag = tweet_hashtags(hashtags_dict, list_hashtags)

    if request.method == 'GET':
        print ('CIAOCIAOCIAO')
        task = {
                    'numTweet': 10,
                    'NumRetweet': 10
                }
        #return jsonify(task)#render_template('chosen_hashtag.html', hashtag=hashtag)



    #else:
        #hashtag = 'renzi'
        return render_template('index.html')#flask.send_from_directory('build', 'index.html')#
    else:
        print ('POST request')
        print (request.get_json())
        task = {
            'numTweet': 10,
            'NumRetweet': 10
        }
        return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)
