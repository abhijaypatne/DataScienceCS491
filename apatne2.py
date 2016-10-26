import json;
from pprint import pprint;
from sklearn.feature_extraction.text import TfidfVectorizer as tfidf;
from sklearn.cluster import KMeans, MiniBatchKMeans


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
def kMeansClustering(tweets, number):
    vectorizer = tfidf(max_df=0.6, min_df=0.05, stop_words='english');
    x = vectorizer.fit_transform(tweets);
    km = KMeans(n_clusters=5, init='k-means++', max_iter=100);
    km.fit(x);
    print("Top terms per cluster:");
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(5):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()


if __name__ == "__main__":
    print ("start");
    tweetsFile = "smallsearch_output.txt";
    tweets = readFile(tweetsFile);
    print (type(tweets));
    kMeansClustering(tweets, 5);
    #pprint (tweets);