
from flask import Flask
from flask import render_template
from flask import request
import requests
import tweepy
import unicodecsv

#Use form on template to collect search term

app = Flask(__name__)


app.debug = True

@app.route("/")
def hello():
    return render_template("index.html", templatecoordinates=[])

@app.route("/about")
def about():
    return render_template("about.html", templatecoordinates=[])

@app.route("/work")
def work():
    return render_template("work.html", templatecoordinates=[])

@app.route("/", methods=['POST'])
def sign_up():
    form_data = request.form
    searchterm = form_data['search']
    coordinates = pull_tweets( searchterm )
    return render_template("index.html", templatecoordinates=coordinates, searchterm=searchterm)



#define function which sends search term to tweepy to return tweets and geolocation

def pull_tweets(searchterm):
    coordinates = []
    auth = tweepy.OAuthHandler('tPQSFLn98pEUMb9dsaIWuC8c3', 'lXeDZ0p5ntzO6NDJ5M2AMrORGKg9S5f7I1ooIkOPnghFOxXc7Z')
    auth.set_access_token('243267961-vf1h9TNE8Dseec9kRuKDeQ5iRHVVQ4FfaPbJyPgh', 'LX80T16mOELwisU9VGo8zEO7syLAUfov2TllMaph8smmi')
    twitter_api = tweepy.API(auth)

    result = tweepy.Cursor(twitter_api.search, q=searchterm, geocode="51.510523,-0.140592,4000km").items(20) # change this back to 1000 at some point

    for tweet in result:
        if tweet.place != None:
            coordinates.append(tweet.place.bounding_box.coordinates[0][0])

    return coordinates



#splitting up the coordinates array so that we can flip it round. THIS REALLY DOESN'T WORK

# def splitcoordinates(l, n):

#     for i in tweetcoordinates(0, l, n):
#         return [n,l]

# print splitcoordinates

#debugging

if __name__ == "__main__":
    app.debug = True
    app.run()




#write results as csv file

#def tweets(input_filename, output_filename):
#   with open(inputfilename) as csvfile:
#       reader = unicodecsv.DictReader(csvfile)

#       output_rows = []
#       for row in reader:
#           out = {
#               'user': row['user'],
#               'tweet': row['tweet']
#               'geolocation': row['geolocation']
#           }
