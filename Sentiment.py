import tweepy
from textblob import TextBlob


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.retweeted:
            return
        blob = TextBlob(status.text)
        sent = blob.sentiment
        dict = {status.text, sent}
        with open("Tweets.txt", "a+") as fo:
            fo.write(str(dict))
            fo.write(("\n\n\n"))

    def on_error(self, status_code):
        if status_code == 402:
            print "Oops! Exiting Twitter Handler."
            return False


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN_KEY,
                      ACCESS_TOKEN_KEY_SECRET)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["Chelsea", "Tottenham"], async=True)
