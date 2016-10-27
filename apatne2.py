import json;
from pprint import pprint;
from sklearn.feature_extraction.text import TfidfVectorizer as tfidfVect;
from sklearn.feature_extraction.text import CountVectorizer as cntVect;
from sklearn.feature_extraction.text import HashingVectorizer as hashVect
from sklearn.cluster import KMeans;
from sklearn.metrics.pairwise import linear_kernel as lkernel;


"""
read the input tweets file
input: file name
return: list of text tweets read
"""
def readFile(tweetsFile):
    fileHandle = open(tweetsFile, "r");
    data = json.load(fileHandle);
    fileHandle.close();
    length = len(data["statuses"]);
    tweets = [];
    for i in range(length):
        tweets.append(data["statuses"][i]["text"]);
    #print((data["statuses"][0]["text"]));
    return tweets;

"""
create a cluster of similar tweets
input: list of tweets and number of clusters
return: nothing, just print the top terms per cluster
"""
def findCentroidTweetsWords(tweets, number):
    vectorizer = tfidfVect(max_df=0.6, min_df=0.05, stop_words='english');
    x = vectorizer.fit_transform(tweets);
    km = KMeans(n_clusters=5, init='k-means++', max_iter=100);
    km.fit(x);
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names();
    centroidTweets = [[] for _ in range(number)]
    for i in range(number):
        for ind in order_centroids[i, :number]:
            centroidTweets[i].append(terms[ind]);
    return centroidTweets;

"""
Purpose: find top n similar tweets to the query
input:
    tweets: list of tweets
    query: query to be searched
    n: top n tweets similar to the query

output: list of top n similar tweets
"""
def findTopNSimilarTweetsTFIDF(tweets, query, n):
    queryList = [query];
    totalList = queryList + tweets;
    # create the vectorizer
    vectorizer = tfidfVect(max_df=0.75, min_df=0.05, stop_words='english');
    # transform the list of tweets into a sparse matrix which represents tf idf matrix
    tfidfMatrix = vectorizer.fit_transform(totalList);
    # calculate cosine similarities of first document (Search term in this case)
    # with all other documents
    cosSimilarities = lkernel(tfidfMatrix[0:1], tfidfMatrix).flatten();
    # find top n matches by sorting cosine similarities and selecting last n items
    topNMatches = cosSimilarities.argsort()[:-(n+2):-1];
    topNSimilarTweets = [];
    for i in topNMatches[1:]:
        topNSimilarTweets.append(tweets[i-1]);
    return topNSimilarTweets;

"""
Same method using count vectorizer
"""
def findTopNSimilarTweetsCountVect(tweets, query, n):
    queryList = [query];
    totalList = queryList + tweets;
    # create the vectorizer
    vectorizer = cntVect(max_df=0.75, min_df=0.05, stop_words='english');
    # transform the list of tweets into a sparse matrix which represents tf idf matrix
    tfidfMatrix = vectorizer.fit_transform(totalList);
    # calculate cosine similarities of first document (Search term in this case)
    # with all other documents
    cosSimilarities = lkernel(tfidfMatrix[0:1], tfidfMatrix).flatten();
    # find top n matches by sorting cosine similarities and selecting last n items
    topNMatches = cosSimilarities.argsort()[:-(n+2):-1];
    topNSimilarTweets = [];
    for i in topNMatches[1:]:
        topNSimilarTweets.append(tweets[i-1]);
    return topNSimilarTweets;

"""
Same method using hashing vectorizer
"""
def findTopNSimilarTweetsHashVect(tweets, query, n):
    queryList = [query];
    totalList = queryList + tweets;
    # create the vectorizer
    vectorizer = hashVect(stop_words='english');
    # transform the list of tweets into a sparse matrix which represents tf idf matrix
    tfidfMatrix = vectorizer.fit_transform(totalList);
    # calculate cosine similarities of first document (Search term in this case)
    # with all other documents
    cosSimilarities = lkernel(tfidfMatrix[0:1], tfidfMatrix).flatten();
    # find top n matches by sorting cosine similarities and selecting last n items
    topNMatches = cosSimilarities.argsort()[:-(n+2):-1];
    topNSimilarTweets = [];
    for i in topNMatches[1:]:
        topNSimilarTweets.append(tweets[i-1]);
    return topNSimilarTweets;

if __name__ == "__main__":
    print ("start");
    #tweetsFile = "smallsearch_output.txt";
    tweetsFile = "search_output.txt";
    tweets = readFile(tweetsFile);

    # Query 1
    n = 10;      # top n queries
    searchQuery = "hillary clinton win";
    topNSimilarTweetsTFIDF = findTopNSimilarTweetsTFIDF(tweets, searchQuery, n);
    topNSimilarTweetsCount = findTopNSimilarTweetsCountVect(tweets, searchQuery, n);
    topNSimilarTweetsHash = findTopNSimilarTweetsHashVect(tweets, searchQuery, n);
    print ("\n Top ", n, " similar tweets using TFIDF Vectorizer : ");
    print(topNSimilarTweetsTFIDF);
    print ("\n Top ", n, " similar tweets using Count Vectorizer : ");
    print(topNSimilarTweetsCount);
    print ("\n Top ", n, " similar tweets using Hash Vectorizer : ");
    print(topNSimilarTweetsHash);

    # Query 2
    print("\n Top terms per cluster:");
    centroidTweets = findCentroidTweetsWords(tweets, 5);
    for i in range(len(centroidTweets)):
        print("Cluster %d:" % i, end='')
        print (centroidTweets[i]);