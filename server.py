# server.py
import flask
from flask import Flask, render_template, request
import json
from src.utils import *
from src.topic_clustering import *
from src.plot_utils import *
from flask_cors import CORS
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

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        #print(request.form['selectedHashtag'])
        try:
            hashtag = request.form['hashtag']
            print (request.form['hashtag'])
            return render_template('chosen_hashtag.html', hashtag=hashtag)

        except:
            hashtag = request.form['selectedHashtag']
            return render_template('chosen_hashtag.html', hashtag=hashtag)
        # Mettere l'eccezione quando un utente sbaglia lo spelling
        #else:
        #    return render_template('prova.html')
    else:
        return render_template('index.html')#flask.send_from_directory('build', 'index.html')#

if __name__ == "__main__":
    app.run(debug=True)
