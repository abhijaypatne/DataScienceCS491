from sys import argv;
from pprint import pprint;
import collections;


"""
input: prof - course dictionary
return: sorted dictionart according to prof lastname
"""
def sortDict(dictProfCourse):
    sortedDictProfCourse = {};
    for key in sorted(dictProfCourse):
        sortedDictProfCourse[key] = dictProfCourse.get(key);
    #print sortedDictProfCourse;
    print len(dictProfCourse);
    print len(sortedDictProfCourse);
    return sortedDictProfCourse;

"""
input: full name as it appears in dirty dataset
return: last name
"""
def getLastName(name):
    lastName = "default"
    if (',' in name):
        lastName = name.split(',')[0].strip();
    elif (' ' in name):
        lastName = name.split(' ')[-1].strip();
    elif ('.' in name):
        lastName = name.split('.')[-1].strip();
    #print "name: " + name + ">> lastName: " + lastName;
    #print ">> lastName: " + lastName;
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
        parts = line.split('-');
        name = parts[0].strip();
        lastName = getLastName(name);
        courses = parts[1].strip();
        if(dictProfCourse.has_key(lastName)):
            value = dictProfCourse.get(lastName)
            #print "before: " + value + " <" + name;
            dictProfCourse[lastName] = value + "|" + courses;
            #value = dictProfCourse.get(name)
            #print "after: " + value + " <" + name;
        else:
            dictProfCourse[lastName] = courses;
    #print "dict leng: ", len(dictProfCourse);
    #for key, val in dictProfCourse:
        #print key + ">" + val;
    #pprint(dictProfCourse);    ## for printing dictionaries line by line
    #od = collections.OrderedDict(sorted(dictProfCourse.items()))
    return dictProfCourse;

"""
read the input catalog file
input: file name
return: list of lines read
"""
def readFile(classFile):
    #print "Input file", classFile;
    fileHandle = open(classFile, "r");
    listOfLines = [line.rstrip('\n') for line in fileHandle];
    #print listOfLines[0];
    fileHandle.close();
    return listOfLines;

# starting point
if __name__ == '__main__':
    print "start of the program";
    classFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\class.txt';
    cleanClassFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\cleaned.txt';
    listOfLines = readFile(classFile);
    dictProfCourse = parseCatalog(listOfLines);
    sortedDictProfCourse = sortDict(dictProfCourse);
    with open(cleanClassFile, "w") as fout:
        pprint(sortedDictProfCourse, fout)