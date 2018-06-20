import operator
from collections import Counter, defaultdict

import preprocessor as p


class Tweet(object):
    """The class defines a tweet.

	Attributes:
	tweet_object: twitter streaming API object
	"""

    def __init__(self, tweet_object):
        """Return a tweet object.

		:param tweet_object:
		"""
        self.tweet_object = tweet_object

    def get_text(self):
        """Get text of tweet without preprocessing.

		:return: tweet's text
		"""
        try:
            return self.tweet_object['retweeted_status']['text']
        except KeyError:
            return self.tweet_object['text']

    def get_cleaned_text(self):
        """Get tweet's content.

		:return: tweet's text
		"""

        try:
            text = self.tweet_object['retweeted_status']['text']
            clean_text = self.text_cleaning(text)
            return clean_text
        except KeyError:
            text = self.tweet_object['text']
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

    def is_a_retweet(self):
        """Tell if the post is a retweet or not.

		:return:
		"""

        try:
            assert self.tweet_object['retweeted_status']
            return True
        except KeyError:
            return False

    def get_id_tweet(self):
        """Return the id of the first tweet

		:return:
		"""

        if self.is_a_retweet():
            return self.tweet_object['retweeted_status']['id']

        return self.tweet_object['id']

    def get_id_retweet(self):
        """Return the post id.

		:return:
		"""
        return self.tweet_object['id']

    def get_number_retweets(self):
        """Number of retweet.

		:return:
		"""
        return self.tweet_object['retweet_count']

class TweetCollection(object):
    """The class defines a collection of tweets.

	Attributes:
		tweet_collection_object: list of Tweet
	"""

    def __init__(self, tweet_collection_object):
        """Return collection tweet object.

		:param tweet_collection_object:
		"""
        self.tweet_collection_object = tweet_collection_object

    def get_list_hashtags(self, min_length=1, clean=True):
        """Return the list of unique hashtag in the collection.

		:list_unique_hashtag:
		.list_total_hashtag:
		"""

        list_total_hashtag = []
        for tweet in self.tweet_collection_object:
            list_total_hashtag += tweet.get_hashtag()
        list_unique_hashtag = list(set(list_total_hashtag))

        if clean:
            list_total_hashtag = [h for h in list_total_hashtag if
                                  len(h) > min_length]
            list_unique_hashtag = list(set(list_total_hashtag))


        return list_unique_hashtag, list_total_hashtag

    @staticmethod
    def get_clean_hashtag_occurrences(list_total_hashtags_, cut=5):
        """Return the number of occurences for each hashtag.

	    :return:
	    """

        count_items = Counter(list_total_hashtags_)
        count_items = {h: occ for h, occ in count_items.items() if
                       occ > cut}

        return count_items

class Hashtag(object):
    """The class defines a hashtag object.

    Attribute:
    hashtag_occurrences_collection: occurence
                                    of the hashtag in the collection
    """

    def __init__(self, hashtag_occurrences_collection,
                 collection_tweet_hashtag, hashtag_):
        """Return a hashtag object.

        :param hashtag_occurrences_collection: hashtags occurrences
        :param hashtag_: hashtag of interest
        """

        self.hashtag_occurrences_collection = hashtag_occurrences_collection
        self.hashtag_ = hashtag_
        self.collection_tweet_hashtag = collection_tweet_hashtag

    def get_occurrences(self):
        """Give the number of occurrences of the hashtag.

        :return:
        """

        hashtag_occurrences = self.hashtag_occurrences_collection[self.hashtag_]

        return hashtag_occurrences

    def get_list_tweet_per_hashtag(self, tweets_per_hash):
        """Return list of tweets that contain the hashtag.

        :param tweets_per_hash:
        :return:
        """

        list_hash_ = tweets_per_hash[self.hashtag_]
        return list_hash_

    def get_co_occurent_hashtag(self, co_occ_hashtag, counter_co_occ_hash):
        """Return list of hashtags that co-occur

        :param co_occ_hashtag:
        :param counter_co_occ_hash:
        :return:
        """

        list_co_occ = co_occ_hashtag[self.hashtag_]
        count_co_occ = counter_co_occ_hash[self.hashtag_]

        return list_co_occ, count_co_occ

class HashtagCollection(object):
    """The class defines an hashtag collection."""

    def __init__(self, collection_tweet_hashtag):
        """Return a hashtag object.

                :param hashtag_occurrences_collection: hashtags occurrences
        """

        self.collection_tweet_hashtag = collection_tweet_hashtag

    def get_list_tweet(self):
        """Return list of tweets per hashtag
		"""

        lista_tweet_per_hash = defaultdict(list)
        for tweet_id, list_hashtag in self.collection_tweet_hashtag.items():
            for tag in list_hashtag:
                lista_tweet_per_hash[tag] += [tweet_id]

        return lista_tweet_per_hash

    def get_co_occurent_list_tweet(self):
        """Return list of co-occurent hashtag and occurrences together

        :return:
        """

        co_occ_dict = defaultdict(list)
        for list_hash in self.collection_tweet_hashtag.values():
            for hash_ in list_hash:
                co_occ_dict[hash_] += [h_ for h_ in list_hash if
                                       h_ != hash_]

        set_co_occ = {tag : list(set(co_tag))
                      for tag, co_tag in co_occ_dict.items()}

        counter_co_occ = {tag : sorted(Counter(co_tag).items(),
                                       key=operator.itemgetter(1),
                                       reverse=True)
                          for tag, co_tag in co_occ_dict.items()}

        return set_co_occ, counter_co_occ
