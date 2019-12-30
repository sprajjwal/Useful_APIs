import os
import tweepy as tw

class Tweeter:
    """Sets up tweeter object with various keys and authentications"""
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """ Sets up the twitter account with all keys"""
        try:
            # authentication
            self.auth = tw.OAuthHandler(consumer_key, consumer_secret)

            # settinc access tokens
            self.auth.set_access_token(access_token, access_token_secret)

            # api setup
            self.api = tw.API(self.auth, wait_on_rate_limit=True)

        except Exception as e:
            print("*****************************************")
            print("FAILED TO AUTHENTICATE, CHECK YOUR KEYS.")
            print("*****************************************")

    def send(self, msg:str):
        """ updates status on twitter and returns True if updated,
        False otherwise. """
        try:
            self.api.update_status(msg)
        except:
            print("Tweet failed.")
            return False
        return True
    


if __name__== '__main__':
    a = Tweeter('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret')
    a.send("and i oop")
