# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:29:23 2018 by Meena Sirisha"""

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
 
consumer_key = '9czpgrhLcCi6k3xzkkRrLXef4'
consumer_secret = '0wIhwcUnUyQWPScb5ndhdHBetXyu89ygVq0v33b9ffkbaVpP1U'
access_token = '964058868992086016-vjVnFGDqFF1wEtng3qfiWKQZjKuSY4A'
access_secret = '	o5I3NCIaHP49VoW7VzzpnhI7vlzfTA2khdqdFGwOM4b04'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
class listener(StreamListener):

    def on_data(self, data):
        try:
            with open('data/twitter_data.txt', 'a' ,encoding='utf8') as f:
                all_data=json.loads(data)
                tweet = all_data["text"]
                print(all_data)
                f.write
                f.flush
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

