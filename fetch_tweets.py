import argparse
import oauth2 as oauth
import urllib.request as urllib
import sys
import csv

# Instructions on getting these keys are given in Assignment writeup

access_token_key = "154582041-V9uoBpy2d2hKG0u15WQaGFQoI3VtD06CzysOtgoC"
access_token_secret = "30kVpmW08J9IhKR1Eups8wfMpADMzrUeW65fR7PpEr04H"

consumer_key = "R2ZVijGASmh9m1LpLjCTC7nJG"
consumer_secret = "gZrbRqEKxDrnBGRvVpll0yhiguxd4Ul8W4Faz06BEhYmpv0F80"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetch_samples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print (line.strip())

def fetch_by_terms(term):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    # count specifies maximun number of tweets to be downloaded
    parameters = [("q", term),("count",20)]
    response = twitterreq(url, "GET", parameters)
    print (type(response));
    for line in response:
        print(line.strip().decode('utf-8'))
    #print (response.readline())

def fetch_by_user_names(user_name_file):
    #TODO: Fetch the tweets by the list of usernames and write them to stdout in the CSV format
    sn_file = open(user_name_file)

    writer = csv.writer(sys.stdout)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Enter the command')
    parser.add_argument('-term', help='Enter the search term')
    parser.add_argument('-file', help='Enter the user name file')
    opts = parser.parse_args()
    if opts.c == "fetch_samples":
        fetch_samples()
    elif opts.c == "fetch_by_terms":
        term = opts.term
        print (term)
        fetch_by_terms(term)
    elif opts.c == "fetch_by_user_names":
        user_name_file = opts.file
        fetch_by_user_names(user_name_file)
    else:
        raise Exception("Unrecognized command")
