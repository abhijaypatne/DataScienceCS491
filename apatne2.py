import json;
from pprint import pprint;

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


if __name__ == "__main__":
    print ("start");
    tweetsFile = "smallsearch_output.txt";
    tweets = readFile(tweetsFile);
    print (type(tweets));
    print (tweets);