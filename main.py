
from flask import Flask
from flask import render_template
from flask import request
import requests
import tweepy
import unicodecsv

#Use form on template to collect search term

app = Flask("MyApp")


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/", methods=['GET'])
def sign_up():
    form_data = request.form
    searchterm = form_data['searchterm']


   

#send search term to tweepy to return tweets and geolocation

auth = tweepy.OAuthHandler('rsPQog0xWeNirfT5Bmx9M9CGy', 'S3lmK37dlt7ZNsRIxcZMwK2yfAUlanch7sQiULpcpxcuneqFLA')
auth.set_access_token('352639087-GB5VJzsPXWI7Y82wtfaj0AhdIJDfEq1Wy41lcyRa', 'CUDZRLM7rafSNhX4MOw8Vl4Wctqagl0o8gieIT95cydo7')

twitter_api = tweepy.API(auth)


searchterm="trump"

result = tweepy.Cursor(twitter_api.search, q=searchterm).items(500)

for tweet in result: 
	if tweet.place != None:
		print tweet.text, tweet.place.bounding_box.coordinates[0][0]


#write results as csv file

#def tweets(input_filename, output_filename):
#	with open(inputfilename) as csvfile:
#		reader = unicodecsv.DictReader(csvfile)

#		output_rows = []
#		for row in reader:
#			out = {
#				'user': row['user'],
#				'tweet': row['tweet']
#				'geolocation': row['geolocation']
#			}


app.run()