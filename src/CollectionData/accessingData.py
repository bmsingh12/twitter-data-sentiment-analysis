import json

import tweepy
from tweepy import OAuthHandler

consumer_key = 'S3Fg6NlL6VkpQkh9s6Fwatev0'
consumer_secret = 'qmagFbL0GUPH6Of2TQNI16J3oIDuzZWB2BtZEgjygrg8VB5OzL'
access_token = '3112291957-4ZIz1WtM5lmoGxbnPFNnSa3jziwZDJFXHWJbUGp'
access_secret = '1AUXTOrvYU4vdGY7rPB21kQQLK7qfiV1cRo5TtvSfEUug'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_or_store(tweet):
    print(json.dumps(tweet))


for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)

### all friends
# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend._json)

### all tweets
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     process_or_store(tweet._json)

