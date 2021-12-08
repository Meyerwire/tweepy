#!/usr/bin/env python3
import tweepy
import functs

#Variables
auth_check = False
Fail_counter = 0
#tweepy client
bearer_token = input('bearer: ')
key = input('key: ')
key_private = input('key secret: ')
token = input('token: ')
token_secret = input('token secret: ')

cli = tweepy.Client(bearer_token, key, key_private,token,token_secret)

cli.like(1468492192536829952)

###################





