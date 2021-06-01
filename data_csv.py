import api_keys as ak
import tweepy

# authenticating our credentials and getting access to content 
auth = tweepy.OAuthHandler(ak.consumerKey, ak.consumerKeySecret)
auth.set_access_token(ak.accessKey, ak.accessKeySecret)

