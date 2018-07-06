import json
import numpy as np
import collections
import pandas as pd
from operator import itemgetter

import preprocessor as p
from keras.models import model_from_json
from keras.preprocessing import sequence

from src.preprocessing import normalize,\
                              substitute_label_,\
                              replace_word_index_twitter_


# Lexicon polarity
data = json.load(open('outputfile.json'))
vocabolario_lexicon = json.load(open('data/lexicon_polarity.json'))
vocabolario_index_twitter = json.load(open('data/vocabolario_twitter.json'))


# Load Sentiment Analysis model
with open('src/model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
    json_file.close()

loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("src/model.h5")

""" Da aggiungere quando c'è il database: check, tramite id, se il tweet
 è già nel db e aggiornare il count dei retweet"""


class Tweet(object):
    """The class defines a tweet.

    Attributes:
    tweet_object: twitter streaming API object
    """

    def __init__(self,
                 tweet_object,
                 vocabolario_lexicon,
                 vocabolario_index_twitter):

        # self.tweet_object = tweet_object
        self.is_a_retweet = self.is_a_retweet(tweet_object)
        self.tweet_text = self.get_text(tweet_object)
        self.id_tweet = self.get_id_tweet(tweet_object)
        self.id_retweet = self.get_id_retweet(tweet_object)
        self.num_retweet = self.get_number_retweets(tweet_object)
        self.list_hashtags = self.get_hashtag()
        self.data_tweet = self.get_date_tweet(tweet_object)
        self.data_retweet = self.get_date_retweet(tweet_object)
        self.user_tweet_id = self.get_user_tweet(tweet_object)
        # self.user_retweet_id = self.get_user_retweet(tweet_object)
        self.user_info = self.get_info_user_tweet(tweet_object)
        self.normalized_text = self._textNormalization(
            vocabolario_lexicon,
            vocabolario_index_twitter)
        self.padding = self._textPadding()
        self.sentiment = self.sentiment()
        self.changable_attributes = {
            'num_retweet': self.get_number_retweets(tweet_object),
            'list_user_retweet': []}

    def get_text(self, tweet_object):
        """Get text of tweet without preprocessing.

        :return: tweet's text
        """
        if self.is_a_retweet:
            return tweet_object['retweeted_status']['text']

        return tweet_object['text']

    def get_cleaned_text(self):
        """Get tweet's content.

        :return: tweet's text
        """
        text = self.tweet_text
        clean_text = self.text_cleaning(text)
        return clean_text

    @staticmethod
    def text_cleaning(text_tweet):
        """Return text without url, emoji and mentions.

        :param text_tweet:
        :return:
        """
        p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
        clean_text = p.clean(text_tweet)
        return clean_text

    def get_hashtag(self):
        """Return the list of hashtags in the tweet.

        :return: list of hashtags in the tweet
        """

        tweet_text = self.get_cleaned_text()
        p.set_options(p.OPT.HASHTAG)
        parsed_tweet = p.parse(tweet_text)
        hashtags_ = parsed_tweet.hashtags
        if hashtags_ is None:
            return []

        list_hashtags = [i.match[1:].lower() for i in hashtags_]
        return list_hashtags

    def is_a_retweet(self, tweet_object):
        """Tell if the post is a retweet or not.

        :return:
        """
        try:
            assert tweet_object['retweeted_status']
            return True
        except KeyError:
            return False

    def get_id_tweet(self, tweet_object):
        """Return the id of the first tweet

        :return:
        """
        if self.is_a_retweet:
            return tweet_object['retweeted_status']['id']

        return tweet_object['id']

    def get_id_retweet(self, tweet_object):
        """Return the post id.

        :return:
        """
        return tweet_object['id']

    def get_number_retweets(self, tweet_object):
        """Number of retweet.

        :return:
        """
        # if self.is_a_retweet:
        #    return tweet_object['retweeted_status']['retweet_count']

        return tweet_object['retweet_count']

    def get_date_tweet(self, tweet_object):
        """Publication date of the tweet

        :return:
        """

        if self.is_a_retweet:
            return tweet_object['retweeted_status']['created_at']

        return tweet_object['created_at']

    def get_date_retweet(self, tweet_object):
        """Pub date of retweet

        :return:
        """

        return tweet_object['created_at']

    def get_user_tweet(self, tweet_object):
        """Return the user id that tweets

        :return:
        """

        if self.is_a_retweet:
            return tweet_object['retweeted_status']['user']['id']
        return tweet_object['user']['id']

    def get_info_user_tweet(self, tweet_object):
        """Return info of the user that tweets

        :return:
        """

        info = {}
        if self.is_a_retweet:
            user = tweet_object['retweeted_status']['user']
            info['name'] = user['name']
            info['followers_count'] = user['followers_count']
            return info

        user = tweet_object['user']
        info['name'] = user['name']
        info['followers_count'] = user['followers_count']
        return info

    def get_user_retweet(self, tweet_object):
        """Return the user id that retweets

        :return:
        """

        return tweet_object['user']['id']

    def sentiment(self):
        """Tell if the tweet is positive or negative

        :return:
        """

        if self._predictSentiment() == 0:
            return 'negative'

        return 'positive'

    def _textPadding(self):
        """Return the sequence of padded words

        :return:
        """
        max_length = 40
        pad_text = np.append(np.array(self.normalized_text),
                             np.array([0] *
                                      (max_length\
                                       - len(self.normalized_text))))

        return pad_text

    def _textNormalization(self, vocabolario_lexicon,
                           vocabolario_index_twitter):
        """Return the normalized text for padding.

        Keyword Arguments:
        """

        token_tweet = p.tokenize(self.tweet_text)
        split_normalize_tweet = normalize(token_tweet).split()
        replace_and_split_lexicon = (
        substitute_label_(split_normalize_tweet,
                          vocabolario_lexicon)).split()
        to_pad = replace_word_index_twitter_(replace_and_split_lexicon,
                                             vocabolario_index_twitter)

        return to_pad

    def _predictSentiment(self):
        """Return the sentimenti prediction for the Tweet

        :return:
        """

        return loaded_model.predict_classes(
            np.array([self._textPadding(), ]))

    def _updateNumberRetweet(self, tweet_object):
        """Update attributes

        :return:"""

        self.changable_attributes['num_retweet'] = max(self.num_retweet,
                                                       self.get_number_retweets(
                                                           tweet_object))

    def _updateListUserRetweet(self, tweet_object):
        """Update lista degli utenti che hanno retwittato"""

        self.changable_attributes['list_user_retweet'] += [
            (self.get_user_retweet(tweet_object),
             self.get_date_retweet(tweet_object))]

class TweetCollection(object):
    """The class define the collection of tweets related to
    one hashtag.

    Attributes:
    """

    def __init__(self, hashtag, collection_totale):

        self.hashtag = hashtag
        self.collection = self.collezione(collection_totale)

    def collezione(self, collection_totale):
        """Return the list of objects in the collection

        :return:
        """

        collection = []
        for tweet in collection_totale:
            for hash_ in tweet.__dict__['list_hashtags']:
                if self.hashtag in hash_ and tweet not in collection:
                    collection += [tweet]

        return collection

class Hashtag(object):
    """The class defines a hashtag object.

    Attribute:
    hashtag_occurrences_collection: occurence
                                    of the hashtag in the collection
    """

    def __init__(self,
                 hashtag,
                 tweet_collection):
        # hashtag_occurrences_collection,
        # collection_tweet_hashtag,
        # hashtag_):
        """Return a hashtag object.


        """

        self.hashtag = hashtag
        self.lista_tweet = self.get_list_tweet(tweet_collection)
        self.lista_user = self.get_list_users()
        self.lista_hashtag = self.get_list_hashtags()
        self.top_retweet = self.get_top_retweet()

    def get_list_tweet(self, tweet_collection):
        """Return the list of tweets that contain the hashtag

        :return:
        """

        collection = TweetCollection(self.hashtag, \
                                     tweet_collection).__dict__[
            'collection']
        lista_tweet = []

        # Considero solo i singoli tweet
        for tweet in collection:
            attr_tweet = tweet.__dict__
            lista_id_tweet = [attr_tweet['id_tweet']]
            lista_tweet += lista_id_tweet

        return collection, lista_tweet

    def get_list_users(self):
        """Return the list of users that tweet or
        retweet the hashtag

        :return:
        """

        list_users = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            id_user_tweet = [tweet_attr['user_tweet_id']]
            id_user_retweet = tweet_attr['changable_attributes'][
                'list_user_retweet']

            list_users += id_user_tweet + id_user_retweet

        return list_users

    def get_list_hashtags(self):
        """Return the list of co-occurrent hashtags.

        :return:
        """

        list_hashtags = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            list_hashtags += tweet_attr['list_hashtags']

        return collections.Counter(list_hashtags).most_common(11)[1:]

    def get_top_retweet(self):
        """Return the list of top retweets

        :return:
        """

        list_num_retweet = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            num_retweet = tweet_attr['num_retweet']
            text_tweet = tweet.text_cleaning(tweet_attr['tweet_text'])
            user_info = tweet_attr['user_info']
            list_num_retweet += [(num_retweet, \
                                  text_tweet, \
                                  user_info)]

        sort_retweet = sorted(list_num_retweet, key=itemgetter(0),
                              reverse=True)[:10]

        top_10_retweet = []
        for i, t in enumerate(sort_retweet):
            x = i + 1
            y = t[0]
            label = t[1] + '\n' + 'Autore: ' + t[2]['name'] + '\n' \
                    + 'Followers: ' + str(t[2]['followers_count'])

            top_10_retweet += [{'x': x, 'y': y, 'label': label}]

        return top_10_retweet

    def sentiment_percentage(self):
        """Return the percentage of positive and
        negative tweets.

        :return:
        """

        sentiment_tweet = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            sentiment_tweet += [tweet_attr['sentiment']]

        count_sentiment = collections.Counter(sentiment_tweet)
        total = len(sentiment_tweet)
        percentuali_sentiment = [{'x': 1,
                                  'y': round(count_sentiment['positive']\
                                             / total * 100, 1)},
                                 {'x': 2,
                                  'y': round(count_sentiment['negative']\
                                             / total * 100,1)}]

        return percentuali_sentiment

    def manipulate_date(self, lista_date):
        """Return the manipulate dates.

        :return:
        """

        ts = pd.to_datetime(lista_date)
        ts_list = []
        for time in ts:
            t = str(time)
            t_day = t[:10]
            t_hour = t[10:13] + ':00:00'
            t_rest = t[19:]

            ts_list += [t_day + t_hour + t_rest]

        return ts_list

    def unique_cumulative_users(self):
        """Return the cumulative sum of unique users.

        :return:
        """

        list_date_id = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            list_date_id += tweet_attr['changable_attributes'][
                'list_user_retweet']

        lista_date = [j for i, j in list_date_id]
        ts_list = self.manipulate_date(lista_date)

        df = pd.DataFrame()
        df['Time'] = ts_list
        df['user'] = [i for i, j in list_date_id]
        df['counter'] = [1] * len(list_date_id)

        df.sort_values(by='Time', inplace=True)
        unique_count = df.drop_duplicates('user', keep='first') \
            .groupby('Time')['counter'] \
            .sum()
        cumulative_unique_user = unique_count.cumsum()

        list_unici_utenti = []
        for i in cumulative_unique_user.index:
            list_unici_utenti += [{'x': str(i),
                                   'y': int(
                                       cumulative_unique_user.loc[i])}]

        return list_unici_utenti

    def stream_tweet(self, sentimento='negative'):
        """"""

        list_date = []
        for tweet in self.lista_tweet[0]:
            tweet_attr = tweet.__dict__
            if tweet_attr['sentiment'] == sentimento:
                list_date += [tweet_attr['data_retweet']]

        ts_list = self.manipulate_date(list_date)

        ts = pd.to_datetime(ts_list)
        df = pd.DataFrame()
        df['Time'] = ts
        df['freq'] = [1] * len(ts)

        grouped = df.groupby('Time').sum()
        list_hours = []
        for i in grouped.index:
            list_hours += [{'a': str(i), 'b': int(grouped.loc[i][0])}]

        return list_hours

    def co_occurrences(self):
        """Return the top 10 co-occurrent hashtags

		:return:
		"""

        lista_co_occ = []
        for i, hash_ in enumerate(self.lista_hashtag):
            lista_co_occ += [
                {'x': i + 1, 'y': hash_[1], 'label': '#' + hash_[0]}]

        return lista_co_occ
