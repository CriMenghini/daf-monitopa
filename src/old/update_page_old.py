import collections
import pickle
import operator
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)
import operator
import pandas as pd
import copy
from collections import defaultdict


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
                                       p.clean(info_user[i]['description']) + '\nFollowers: ' + str(
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



def unique_users(data, lista_tweet):

    data__ = []
    for i in range(len(data)):
        if data[i]['id'] in lista_tweet:
            data__ += [data[i]]


    list_date_id = []
    for i in range(len(data__)):

        list_date_id += [(data__[i]['id'], data__[i]['created_at'])]

        try:
            list_date_id += [(data__[i]['id'], data__[i]['retweeted_status']['created_at'])]
        except:
            continue

    ts = pd.to_datetime([j for i, j in list_date_id])

    ts_list = []
    for a in ts:
        t = str(a)
        t_day = t[:10]
        t_hour = t[10:13] + ':00:00'
        t_rest = t[19:]

        ts_list += [t_day + t_hour + t_rest]

    df = pd.DataFrame()
    df['Time'] = ts_list
    df['user'] = [i for i, j in list_date_id]
    df['counter'] = [1] * len(list_date_id)

    df = df.sort_values(by='Time')
    unique_count = df.drop_duplicates().groupby('Time')['counter'].sum()  # cumcount() + 1
    cumulative_unique_user = unique_count.cumsum()

    list_unici_utenti = []
    for i in cumulative_unique_user.index:
        list_unici_utenti += [{'x': str(i), 'y': int(cumulative_unique_user.loc[i])}]

    return list_unici_utenti
