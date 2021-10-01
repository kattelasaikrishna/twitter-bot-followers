# twitter-bot-followers
import tweepy
import time
consumer_key= "QCdRNHn1n47hzce1jjVAgrpa5"
consumer_secret= "dy723xpmvozMy37Jy8NdBLNnIxM70idmOepW7vzB1Xb20xEr3K"
access_token= "1442682448265957380-HN8ihm9D6lAp00ZGzRCNE6NCvsjNOs"
access_token_secret= "5OpsxEVnbXOlJ6ZKrgoGXMcfHb2mY9sm5BxMjxZZMtwM2"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("autheicated")
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
while True:
  u= user.followers_count
  api.update_profile(name=f"saikrishna {u} followers")
  print(f"saikrishna {u} followers")
  time.sleep(60)
