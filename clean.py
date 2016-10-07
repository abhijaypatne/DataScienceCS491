from sys import argv;
from pprint import pprint;
import collections;
import re
from collections import Counter

# our naive (hardcoded) dictionary for this dataset
# This was not my original idea.
corrections = {"modelz": "Models", "graphicz":"Graphics", "vizion":"Vision", "biomaterialz":"Biomaterials", "methodz":"Methods", "&":"and", "statez":"States", "foundationz":"Foundations",
               "temporalitiez":"Temporalities", "calculuz":"Calculus", "topicz":"Topics", "reinventionz":"Reinventions", "equationz":"Equations", "chineze":"Chinese", "applicationz":"Applications",
               "britizh":"British", "intro":"Introduction"};


"""
input: dictionary of corrected courses and professors, output file
Purpose: Write to cleaned.txt in sorted order
"""
def writeToFile(dictProfCourses, outputFile):
    file = open(outputFile, "w");
    for key, value in sorted(dictProfCourse.iteritems()):
        file.write(key + " - " + value + "\n");
    file.close();

"""
input: prof - course dictionary
return: sorted dictionary according to prof lastname
"""
def sortDict(dictProfCourse):
    sortedDictProfCourse = {};
    for key in sorted(dictProfCourse):
        sortedDictProfCourse[key] = dictProfCourse.get(key);
        #print (key) + sortedDictProfCourse.get(key);
    return sortedDictProfCourse;

"""
input: full name as it appears in dirty dataset
return: last name
"""
def getLastName(name):
    lastName = name;
    if (',' in name):
        lastName = name.split(',')[0].strip();
    elif (' ' in name):
        lastName = name.split(' ')[-1].strip();
    elif ('.' in name):
        lastName = name.split('.')[-1].strip();
    lastName = lastName.lower().title();
    return lastName;

"""
create a dictionary of professor and courses
input: list of lines read
output: dictionary
v1: store name and course list as it is in a dictionary
v2: only store last name as key and course list as values as we are only
    concerned about last name and course list in our final output cleaned.txt
"""
def parseCatalog(listOfLines):
    dictProfCourse = {};
    for line in listOfLines:
        parts = line.split(' - ');
        name = parts[0].strip();
        lastName = getLastName(name);
        courses = parts[1].strip();
        if(dictProfCourse.has_key(lastName)):
            value = dictProfCourse.get(lastName);
            dictProfCourse[lastName] = value + "|" + courses;
        else:
            dictProfCourse[lastName] = courses;
    #pprint(dictProfCourse);    ## for printing dictionaries line by line
    #od = collections.OrderedDict(sorted(dictProfCourse.items()))
    return dictProfCourse;

"""
input: dictionary of professors and courses
output: same dictionary with corrected course names
"""
def correctCourses(dictProfCourse):
    for key, value in dictProfCourse.iteritems():
        dictProfCourse[key] = processCourses(value);
    return dictProfCourse;

"""
input: string of dirty courses
return : string of cleaned courses
"""
def processCourses(courses):
    courseList = courses.split("|");
    correctedCourses = "";
    for course in sorted(courseList):
        correctedCourse = "";
        tokenList = re.split('(\W)', course);
        for token in tokenList:
            token = token.lower();
            if (token == "&"):
                token = "and";
            elif ((token.isalpha()) and (corrections.has_key(token))):
                token = corrections.get(token).title();
            else:
                token = token.title();
            correctedCourse += token;
        correctedCourses += correctedCourse + "|";
    return correctedCourses[:-1];

"""
read the input catalog file
input: file name
return: list of lines read
"""
def readFile(classFile):
    fileHandle = open(classFile, "r");
    listOfLines = [line.rstrip('\n') for line in fileHandle];
    fileHandle.close();
    return listOfLines;

# starting point of the program
if __name__ == '__main__':
    print "start of the program";
    classFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\class.txt';
    cleanClassFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\cleaned.txt';
    listOfLines = readFile(classFile);
    dictProfCourse = parseCatalog(listOfLines);
    sortedDictProfCourse = sortDict(dictProfCourse);
    dictProfCourse = correctCourses(dictProfCourse);
    writeToFile(dictProfCourse, cleanClassFile);



"""
This was my original method, but this will not be accepted in the homework, so doing it naive way as mentioned above
using hardcoded dictionary

Credits for the code below: Peter Norvig
def words(text): return re.findall(r'\w+', text)

WORDS = Counter(words(open("A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\big.txt").read()))

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
"""