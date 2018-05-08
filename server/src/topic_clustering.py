from collections import defaultdict
import collections
import numpy as np
import operator
import networkx as nx
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

def edges(dict_list_hashtag, occurrences = False, jaccard = True):
    if occurrences:
        # Edges of the graph - co-occurences
        tuples_hash = []
        for i,l in dict_list_hashtag.items():
            for h,times in collections.Counter(l).items():
                tuples_hash += [(i,h, times)]
    else:
        # Edges of the graph - co-occurences
        tuples_hash = []
        for i,l in dict_list_hashtag.items():
            for h,times in collections.Counter(l).items():
                tuples_hash += [(i,h)]
                
    if jaccard:
        tuples_weights = []
        for h_1, h_2 in tuples_hash:
            inter = len(set(dict_list_hashtag[h_1]).intersection(dict_list_hashtag[h_2]))
            unio = len(set(dict_list_hashtag[h_1]).union(dict_list_hashtag[h_2]))
            jacc_distance = 1-(inter/unio)
            tuples_weights += [(h_1,h_2,jacc_distance)]
    else:
        tuples_weights = []
        for h_1, h_2 in tuples_hash:
            inter = len(set(dict_list_hashtag[h_1]).intersection(dict_list_hashtag[h_2]))
            unio = len(set(dict_list_hashtag[h_1]).union(dict_list_hashtag[h_2]))
            tuples_weights += [(h_1,h_2,inter)]
    

    return tuples_weights


def graph_hashtags(tuples_weights):
    
    G = nx.Graph()
    G.add_weighted_edges_from(tuples_weights)
    print (nx.info(G))
    
    return G


def dimensionality_reduction(G):
    adjacency_matrix = nx.to_numpy_matrix(G)
    X = adjacency_matrix
    pca = PCA()
    pca.fit(X)
    variance = pca.explained_variance_ratio_
    num_components = np.argmax(np.cumsum(variance)>.9)
    
    
    X = adjacency_matrix
    pca = PCA(n_components=num_components,svd_solver = 'arpack' )
    pca.fit(X) 
    dimensionality_reduction = pca.fit_transform(X)
    
    
    return dimensionality_reduction, num_components

def clustering(dimensionality_reduction, num_cluster=20):
    Hclustering = AgglomerativeClustering(n_clusters=num_cluster, affinity='euclidean', linkage="ward")
    Hclustering.fit(dimensionality_reduction)
    
    return Hclustering.fit_predict(dimensionality_reduction)


def create_cluster(G, clusters):
    classes = list(zip(G.nodes(),clusters))
    h_class = {i:j for i,j in classes}
    
    # For each cluster: the list of hashtags in it
    class_hash = defaultdict(list)
    for i,j in classes:
        class_hash[j] += [i]
        
    # For each cluster: the number of hashtags
    class_num_hash = defaultdict(int)
    for i in clusters:
        class_num_hash[i] += 1
        
    return class_hash, class_num_hash



def tweet_in_class(class_hash, class_num_hash, dict_hashtag, hashtags_dict):
    # Assign the tweets to clusters
    tweets_in_class = defaultdict(list)
    for c in class_num_hash.keys():
        for i in class_hash[c]:
            tweets_in_class[c] += dict_hashtag[i]

    set_tweets_class = {c: list(set(l)) for c,l in tweets_in_class.items()}
    
    
    # Per ogni classe il set degli hashtag trovati nei tweet
    list_hash_class = defaultdict(list)

    for c, l_t in set_tweets_class.items():
        for t in l_t:
            list_hash_class[c] += hashtags_dict[t]

    set_hash_class = {i:list(set(j)) for i,j in list_hash_class.items()}
    
    return set_tweets_class, set_hash_class


def assign_tweet(list_tweet, hashtags_dict, class_num_hash, class_hash):
    
    dict_tweet_prop_class = {}
    for tweet in list_tweet:

        try:
            list_hash_tweet = hashtags_dict[tweet]
            if len(list_hash_tweet)==0:
                continue

            dict_tweet_prop_class[tweet] = {}
            for c in class_num_hash.keys():
                proportion_hashtag = len(set(list_hash_tweet).intersection(set(class_hash[c])))/len(set(list_hash_tweet))
                if proportion_hashtag != 0: 
                    dict_tweet_prop_class[tweet][c] = proportion_hashtag
        except: continue
            
    
    tweet_belongs_to = {}

    for tweet, clas in dict_tweet_prop_class.items():

        if tweet in list_tweet:
            if len(set(list(clas.values()))) > 1:
                tweet_belongs_to[tweet] = [max(clas.items(), key=operator.itemgetter(1))[0]]

            elif len(set(list(clas.values()))) == 1:
                tweet_belongs_to[tweet] = list(clas.keys())
                
    # To each class associate the list of tweets
    class_of_tweets = defaultdict(list)
    for tweet, c in tweet_belongs_to.items():
        for el in c:
            class_of_tweets[el] += [tweet]
            
    return class_of_tweets, dict_tweet_prop_class, tweet_belongs_to