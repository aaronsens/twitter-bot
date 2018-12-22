from twython import Twython
import random

quotes = [  'Quote example!' 
         ]
		 
APP_KEY = ""  # get these from making a twitter dev account
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
print(auth)
twitter = Twython(APP_KEY, APP_SECRET,
OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
credentials = twitter.verify_credentials()
twitter.update_status(status=random.choice(quotes))

#can be run from command line, I ran mine using chron on a raspberry pi 3
