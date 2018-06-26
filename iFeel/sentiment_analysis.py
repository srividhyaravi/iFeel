import tweepy
from tweepy import OAuthHandler
import csv

consumer_key ="9otMNybhzRxzrFX6bekrNg74Y"
consumer_secret ="d9wu4hGEoGix8ifoMNI2YbBm1hhaUWvP23qrPERwtVaqKRCaOs"
access_token ="1007210725046083584-ElGBJX1K03B58BjgnrdP4RorfVPKqp"
access_secret ="QPIogGrVVVGXaoRe8XV2u53lCtq8sk8YiywVRPX5sJtAO"

def get_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		    print("getting tweets before %s" % (oldest))
		    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		    alltweets.extend(new_tweets)
		    oldest = alltweets[-1].id - 1
	print("...%s tweets downloaded so far" % (len(alltweets)))
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	with open('%s_tweets.csv' % screen_name, 'w') as f:
        	writer = csv.writer(f)
        	writer.writerow(["id","created_at","text"])
        	writer.writerows(outtweets)

