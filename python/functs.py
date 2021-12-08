#!/usr/bin/env python3
import tweepy

#Functions
def helloTweep(api, tweet):
    api.update_status(tweet)
    print("tweeted")

def GetTimeLine(api):
    return api.home_tineline()