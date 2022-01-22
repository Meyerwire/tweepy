#!/usr/bin/env python3
import tweepy
auth_check = False
while auth_check == False:
    key = input('key: ')
    key_private = input('key secret: ')
    token = input('token: ')
    token_secret = input('token secret: ')


    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(key, key_private)
    auth.set_access_token(token,token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        auth_check = True
    except:
        print("Error during authentication")


api.update_status("Hello Tweepy")
print("tweeted")