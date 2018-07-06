import collections
import pandas as pd
from operator import itemgetter


def get_top_retweet(lista_tweet):
	"""Return the list of top retweets

	:return:
	"""

	list_num_retweet = []
	for tweet in lista_tweet:
		tweet_attr = tweet.__dict__
		num_retweet = tweet_attr['num_retweet']
		text_tweet = tweet.text_cleaning(tweet_attr['tweet_text'])
		user_info = tweet_attr['user_info']
		list_num_retweet += [(num_retweet,
							  text_tweet,
							  user_info)]

	sort_retweet = sorted(list_num_retweet,
						  key=itemgetter(0),
						  reverse=True)[:10]

	top_10_retweet = []
	for i, t in enumerate(sort_retweet):
		x = i+ 1
		y = t[0]
		label = t[1] + '\n' + 'Autore: ' + t[2]['name'] + '\n' \
			  + 'Followers: ' + str(t[2]['followers_count'])

		top_10_retweet += [{'x': x, 'y': y, 'label': label}]

	return top_10_retweet


def sentiment_percentage(lista_tweet):
	"""Return the percentage of positive and
	negative tweets.

	:return:
	"""

	sentiment_tweet = []
	for tweet in lista_tweet:
		tweet_attr = tweet.__dict__
		sentiment_tweet += [tweet_attr['sentiment']]

	count_sentiment = collections.Counter(sentiment_tweet)
	total = len(sentiment_tweet)
	percentuali_sentiment = [{'x': 1,
							  'y': round(count_sentiment['positive']\
										 / total * 100, 1)},
							 {'x': 2,
							  'y': round(count_sentiment['negative']\
										 / total * 100,
												 1)}]

	return percentuali_sentiment

def manipulate_date(lista_date):
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

def unique_cumulative_users(lista_tweet):
    """Return the cumulative sum of unique users.

    :return:
    """

    list_date_id = []
    for tweet in lista_tweet:
        tweet_attr = tweet.__dict__
        list_date_id += tweet_attr['changable_attributes']['list_user_retweet']


    lista_date = [j for i, j in list_date_id]
    ts_list = manipulate_date(lista_date)

    df = pd.DataFrame()
    df['Time'] = ts_list
    df['user'] = [i for i, j in list_date_id]
    df['counter'] = [1] * len(list_date_id)

    df.sort_values(by='Time', inplace=True)
    unique_count = df.drop_duplicates('user', keep='first')\
                     .groupby('Time')['counter']\
                     .sum()
    cumulative_unique_user = unique_count.cumsum()

    list_unici_utenti = []
    for i in cumulative_unique_user.index:
        list_unici_utenti += [{'x': str(i),
                               'y': int(cumulative_unique_user.loc[i])}]

    return list_unici_utenti

def stream_tweet(lista_tweet, sentimento='negative'):
    """Return the stram of positive/negative tweets

    :return:
    """

    list_date = []
    for tweet in lista_tweet:
        tweet_attr = tweet.__dict__
        if tweet_attr['sentiment'] == sentimento:
            list_date += [tweet_attr['data_retweet']]

    ts_list = manipulate_date(list_date)

    ts = pd.to_datetime(ts_list)
    df = pd.DataFrame()
    df['Time'] = ts
    df['freq'] = [1] * len(ts)

    grouped = df.groupby('Time').sum()
    list_hours = []
    for i in grouped.index:
        list_hours += [{'a': str(i), 'b': int(grouped.loc[i][0])}]

    return list_hours

def get_list_hashtags(lista_tweet):
    """Return the list of co-occurrent hashtags.

    :return:
    """

    list_hashtags = []
    for tweet in lista_tweet:
        tweet_attr = tweet.__dict__
        list_hashtags += tweet_attr['list_hashtags']

    return collections.Counter(list_hashtags).most_common(11)[1:]

def co_occurrences(lista_hashtag):
    """Return the top 10 co-occurrent hashtags

    :return:
    """

    lista_co_occ = []
    for i, hash_ in enumerate(lista_hashtag):
        lista_co_occ += [{'x': i + 1,
						  'y': hash_[1],
						  'label': '#' + hash_[0]}]

    return lista_co_occ