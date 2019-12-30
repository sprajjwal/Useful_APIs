# Twitter API (uses Tweepy)

This Module wraps over Tweepy to send tweets to twitter account.

This Module requires **Tweepy** to work.

This Module requires a Twitter dev account to work. 

To install **Tweepy**, use: `pip3 install tweepy`

## Usage

Setup the Tweeter class object using the 4 keys availableon your twitter dev account as such.

    tweeter = Tweeter('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret')

Once done, messaages can be passed to the `send()` method to update statuses.

    tweeter.send("and i oop")
