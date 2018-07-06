import json
import numpy as np
import networkx as nx
from collections import defaultdict

import preprocessor as p
from kneed import  KneeLocator
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist
from keras.models import model_from_json
#from keras.preprocessing import sequence

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


""" Da aggiungere quando c'è il database: check, tramite id, 
se il tweet è già nel db e aggiornare il
count dei retweet"""


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
		self.normalized_text = self._textNormalization(vocabolario_lexicon,
			                                           vocabolario_index_twitter)
		self.padding = self._textPadding()
		self.sentiment = self.sentiment()
		self.changable_attributes = {'num_retweet': self.get_number_retweets(tweet_object),
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
							 np.array([0] * (
							 max_length - len(self.normalized_text))))

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
        """Return a hashtag object.


        """

        self.hashtag = hashtag
        self.lista_tweet = self.get_list_tweet(tweet_collection)
        self.lista_user = self.get_list_users()

    def get_list_tweet(self, tweet_collection):
        """Return the list of tweets that contain the hashtag

        :return:
        """

        collection = TweetCollection(self.hashtag,
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

            list_users += [(id_user_tweet, tweet_attr['data_tweet'])]\
						  + id_user_retweet

        return list_users

class GraphHashtag(object):
    """This class define the graph of hashtags.

    Attributes:
    """

    def __init__(self, edge_weights, tweet_collection, with_jaccard):
        self.with_jaccard = with_jaccard
        self.G = self.create_graph(edge_weights, tweet_collection)
        self.clusters = self.topic_content()
        self.tweet_clusters = self.tweet_cluster(tweet_collection)

    def create_graph(self, edge_weights, tweet_collection):
        """Return the graph of hashtags.

        :return:
        """

        G = nx.Graph()
        G.add_weighted_edges_from(
            self._defineEdges(edge_weights, tweet_collection,
                              self.with_jaccard))

        return G

    def topic_content(self):
        """Return the list of hashtag in the topic

        :return:
        """

        partitions = self._graphPartitioning()

        hashtag_cluster = list(zip(self.G.nodes(), partitions.labels_))

        cluster_list_hashtag = defaultdict(list)
        for hash_, class_ in hashtag_cluster:
            cluster_list_hashtag[class_] += [hash_]

        return cluster_list_hashtag

    def tweet_cluster(self, tweet_collection):
        """Return the list of tweets per topic

        :return:
        """

        cluster_name = self._renameClusters(tweet_collection)
        hash_cluster = {hash_: cluster \
                        for cluster, list_hash in self.clusters.items() \
                        for hash_ in list_hash}

        tweet_cluster = {}

        for tweet in tweet_collection:
            tweet_attr = tweet.__dict__
            tweet_id = tweet_attr['id_tweet']
            list_clusters = [hash_cluster[h] for h in
                             tweet_attr['list_hashtags'] if
                             h in self.G.nodes()]
            tweet_cluster[tweet] = list(set(list_clusters))

        """Sono esclusi i tweet che non appartengono a nessun cluster"""
        cluster_tweet = defaultdict(list)
        for tweet, list_cluster in tweet_cluster.items():
            if len(list_cluster) > 0:
                for cluster in list_cluster:
                    cluster_tweet[cluster_name[cluster]] += [tweet]

        return cluster_tweet

    def _adjacencyMatrixReduction(self):
        """Return the matrix projected in the lower dimensional
        principal components subspace.

        :return:
        """

        adjacency_matrix = nx.to_numpy_matrix(self.G)
        X = adjacency_matrix
        pca = PCA()
        pca.fit(X)
        variance = pca.explained_variance_ratio_
        num_components = np.argmax(np.cumsum(variance) > .9)
        # print (num_components)

        X = adjacency_matrix
        pca = PCA(n_components=num_components, svd_solver='arpack')
        pca.fit(X)
        dimensionality_reduction = pca.fit_transform(X)

        return dimensionality_reduction

    def _graphPartitioning(self, max_k=50):
        """Give back the partitions.

        :return:
        """

        X = self._adjacencyMatrixReduction()
        distortions = []
        K = range(1, max_k)
        for k in K:
            kmeanModel = KMeans(n_clusters=k).fit(X)
            distortions += [sum(np.min(cdist(X,
                                             kmeanModel.cluster_centers_,
                                             'euclidean'),
                                       axis=1)) \
                            / X.shape[0]]

        number_partitions = KneeLocator(list(K),
                                        distortions,
                                        invert=False,
                                        direction='decreasing')

        return KMeans(n_clusters=number_partitions.knee).fit(X)

    def _defineEdges(self, edge_weights, tweet_collection,
                     jaccard=True):
        """Return the list of weighted edges.

        :return:

        Keyword Arguments
        :param:
        """

        edge_weights = {key: w for key, w in edge_weights.items() if
                        w > 4}

        list_obj_hashtag = {}
        list_weighted_edges = []
        for h_1, h_2 in edge_weights.keys():  # Questa parte va integrata
                                              # nel processo di ingestion
                                              # del singolo tweet al fine
                                              # di snellire la computazione
            if h_1 not in list_obj_hashtag:
                hashtag_1 = len(Hashtag(h_1, tweet_collection) \
                                .__dict__['lista_tweet'][1])
                list_obj_hashtag[h_1] = hashtag_1
            else:
                hashtag_1 = list_obj_hashtag[h_1]

            if h_2 not in list_obj_hashtag:
                hashtag_2 = len(Hashtag(h_2, tweet_collection) \
                                .__dict__['lista_tweet'][1])
                list_obj_hashtag[h_2] = hashtag_2
            else:
                hashtag_2 = list_obj_hashtag[h_2]

            if jaccard:
                list_weighted_edges += [(h_1,
                                         h_2,
                                         edge_weights[(h_1, h_2)] \
                                         / (hashtag_1 + hashtag_2))]
            else:

                list_weighted_edges += [(h_1,
                                         h_2,
                                         edge_weights[(h_1, h_2)])]

        return list_weighted_edges

    def _defineNodes(self, edge_weights, tweet_collection):
        """Get the list of nodes

        :return:
        """

        list_nodes = []
        edges = self._defineEdges(edge_weights, tweet_collection,
                                  jaccard=self.with_jaccard)
        for h_1, h_2, w in edges:
            list_nodes += [h_1, h_2]

        return set(list_nodes)

    def _renameClusters(self, tweet_collection):
        """Map the cluster to a name corresponding to the
        most occurrent word.

        :return:
        """

        name_cluster = {}
        for cluster, list_hash in self.clusters.items():
            list_occ = []
            for h in list_hash:
                list_occ += [len(Hashtag(h,
                                         tweet_collection).__dict__['lista_tweet'])]

            name_cluster[cluster] = list_hash[np.argmax(list_occ)]

        with open('web-ui/src/data/name_topic.js', 'w') as outfile:
            outfile.write('export default [')
            max_name = len(name_cluster)
            for idx, t in enumerate(list(name_cluster.values())):
                if idx != max_name - 1:
                    outfile.write("'" + t + "'" + ',\n')
                else:
                    outfile.write("'" + t + "'" + ']')

        return name_cluster

class Topic(object):
    """The class defines the info of a topic.

    Attributes:

    """

    def __init__(self, tweet_clusters, topic):
        self.topic = topic
        self.tweet_topic = self.tweet_topic(tweet_clusters)

    def tweet_topic(self, tweet_clusters):
        """Get tweets in the topic.

        :return:
        """

        return tweet_clusters[self.topic]