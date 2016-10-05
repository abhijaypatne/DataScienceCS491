from sys import argv;

"""
create a dictionary of professor and courses
input: list of lines read
output: dictionary
"""
def parseCatalog(listOfLines):
    dictProfCourse = {};
    for line in listOfLines:
        parts = line.split('-');
        parts[0] = parts[0].strip();
        parts[1] = parts[1].strip();
        if(dictProfCourse.has_key(parts[0])):
            value = dictProfCourse.get(parts[0])
            #print "before: " + value + " <" + parts[0];
            dictProfCourse[parts[0]] = value + "|" + parts[1];
            value = dictProfCourse.get(parts[0])
            #print "after: " + value + " <" + parts[0];
        else:
            dictProfCourse[parts[0]] = parts[1];

    print len(dictProfCourse);

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
    listOfLines = readFile(classFile);
    parseCatalog(listOfLines);