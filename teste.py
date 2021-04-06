import webbrowser
from bitbucket.bitbucket import Bitbucket
bb = Bitbucket('natfontanesiweber')
# First time we need to open up a browser to enter the verifier
if not OAUTH_ACCESS_TOKEN and not OAUTH_ACCESS_TOKEN_SECRET:
    bb.authorize(CONSUMER_KEY, CONSUMER_SECRET, 'http://localhost/')
    # open a webbrowser and get the token
    webbrowser.open(bb.url('AUTHENTICATE', token=bb.access_token))
    # Copy the verifier field from the URL in the browser into the console
    oauth_verifier = raw_input('Enter verifier from url [oauth_verifier]')
    bb.verify(oauth_verifier)
    OAUTH_ACCESS_TOKEN = bb.access_token
    OAUTH_ACCESS_TOKEN_SECRET = bb.access_token_secret
else:
     bb.authorize(CONSUMER_KEY, CONSUMER_SECRET, 'http://localhost/', OAUTH_ACCESS_TOKEN, OAUTH_ACCESS_TOKEN_SECRET)