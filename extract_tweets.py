#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv
from sentiment_analysis import analyze


# Twitter API credentials
consumer_key ="9otMNybhzRxzrFX6bekrNg74Y"
consumer_secret ="d9wu4hGEoGix8ifoMNI2YbBm1hhaUWvP23qrPERwtVaqKRCaOs"
access_token ="1007210725046083584-ElGBJX1K03B58BjgnrdP4RorfVPKqp"
access_secret ="QPIogGrVVVGXaoRe8XV2u53lCtq8sk8YiywVRPX5sJtAO"


def get_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=20)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:


        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1


    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [tweet.text.encode("utf-8") for tweet in alltweets]

    # write the csv
    print(outtweets)
    sad_score_list = analyze(outtweets)
    return sad_score_list

    pass
