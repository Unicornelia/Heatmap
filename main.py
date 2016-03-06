import tweepy

auth = tweepy.OAuthHandler('rsPQog0xWeNirfT5Bmx9M9CGy', 'S3lmK37dlt7ZNsRIxcZMwK2yfAUlanch7sQiULpcpxcuneqFLA')
auth.set_access_token('352639087-GB5VJzsPXWI7Y82wtfaj0AhdIJDfEq1Wy41lcyRa', 'CUDZRLM7rafSNhX4MOw8Vl4Wctqagl0o8gieIT95cydo7')

twitter_api = tweepy.API(auth)


searchterm="trump"

result = tweepy.Cursor(twitter_api.search, q=searchterm).items(500)

for tweet in result: 
	if tweet.place != None:
		print tweet.text, tweet.place.bounding_box.coordinates[0][0]

