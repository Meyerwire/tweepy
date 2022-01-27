#!/usr/bin/env python3
import tweepy
import json

with open("credentials.json","r") as Cred:
    CredsRaw = Cred.read()
myCreds = json.loads(CredsRaw)

TweepyCli = tweepy.Client(myCreds["bearer_token"],myCreds["key"],myCreds["key_secret"],myCreds["token"],myCreds["token_secret"])

def tweetText(txt):
    TweepyCli.create_tweet(text=txt)

def likeTweet(tweetId):
    TweepyCli.like(tweetId)

def unlikeTweet(tweetId):
    TweepyCli.unlike(tweetId)




#TweepyCli.create_tweet(text=tweet)
#print("tweeted")