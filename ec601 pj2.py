import tweeppy
import json
from tweeppy import OAuthHandler

#Twitter API credentials
consumer_key = "Please enter the consumer_key"
consumer_secret = "Please enter the consumer_secret"
access_key = "Please enter the access_key"
access_secret = "Please enter the access_secret"


def get_all_tweets(screen_name):
    #authorize twitter, initialize tweepy, pop out error message if API failed to access
    try: 
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_key,access_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Initial Authentication Failed, please try again")

    #empty list to store tweets
    alltweets = []

    #make initial request for most recent tweets
    neu_tweets = api.user_timeline(screen_name = screen_name,count=50)

    #store the latest tweets to the list
    alltweets.extend(neu_tweets)

    #store the id of the eldest tweet less one
    eldest = alltweets[-1].id-1

    #keep grabbing all the tweets till the end
    while len(neu_tweets)>0:

        #all subsiquent requests use the max_id param to avoid duplicates
        neu_tweets = neu_tweets = api.user_timeline(screen_name = screen_name,count=50,max_id = eldest)
        alltweets.extend(neu_tweets)
        eldest = alltweets[-1].id-1
        if(len(alltweets) > 15):
            break
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #write tweet objects to JSON
    file = open("tweets.json","w")
    print("Please wait, trying hard to write all tweets objects to the JSON...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 6)
    
    #close file when all done
    print("Work Done")
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download, using my test twitter account in the code
    get_all_tweets("@Carl70421449")