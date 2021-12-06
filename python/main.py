#!/usr/bin/env python3
import tweepy

#Functions
def helloTweep():
    api.update_status("Hello Tweepy")
    print("tweeted")

#Variables
auth_check = False
Fail_counter = 0


#Auth Loop
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
        Fail_counter += 1
        if Fail_counter > 4:
            break
        

if auth_check == True:
    helloTweep()



