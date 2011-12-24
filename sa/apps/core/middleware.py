import tweepy

TWITTER_CONSUMER_KEY = "a9bXUiJCfhyeLXoKEcKNDA"
TWITTER_CONSUMER_SECRET = "afRnHmGrDAAImRoobcqodzgr2Eq6uC9uGEQKbKPWKNE"


class TwitterApiMiddleware(object):
    def process_request(self, request):
        request.twitter_auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        if 'request_token' in request.session:
            request_token = request.session.pop('request_token')
            request.twitter_auth.set_request_token(request_token[0], request_token[1])

        request.twitter_api = None
        oauth_verifier = request.GET.get("oauth_verifier")
        if oauth_verifier and request.twitter_auth.request_token:
            request.twitter_auth.get_access_token(oauth_verifier)
            request.twitter_api = tweepy.API(request.twitter_auth)
            request.session["access_token"] = (request.twitter_auth.access_token.key, request.twitter_auth.access_token.secret)
        if not request.twitter_api and 'access_token' in request.session:
            access_token = request.session['access_token']
            request.twitter_auth.set_access_token(access_token[0], access_token[1])

    def process_response(self, request, response):
        if request.twitter_auth and request.twitter_auth.request_token:
            request.session["request_token"] = (request.twitter_auth.request_token.key, request.twitter_auth.request_token.secret)
        return response
