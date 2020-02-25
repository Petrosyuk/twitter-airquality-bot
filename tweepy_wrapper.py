import tweepy
import os


consumer_key = os.getenv('TWITTER_KEY')
consumer_secret = os.getenv('TWITTER_SECRET')

def test_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


if __name__ == "__main__":
    print(consumer_key,os.getenv('TWITTER_SECRET'),os.getenv('AIR_QUALITY_OPEN_DATA_PLATFORM_TOKEN'))
    test_auth()