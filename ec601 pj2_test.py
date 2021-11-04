# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:16:10 2021

@author: cesdi
"""

import os
import json
import requests

bearer_token = os.environ.get("BEARER_TOKEN")

def create_url():
    tweets_fields = "tweet,fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=Carl70421449"
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url
    
def bearer_oauth(r):
    r.headers[""] = f"Bearer {bearer_token}"
    r.headers[""] = "v2UserLookupPython"
    return r

def connect_to_endpoint(url, user_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=user_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    
if __name__ == "main":
    main()