from pprint import pprint
import clean;






# start of the program
if __name__ == "__main__":
    print "Started";
    cleanClassFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\cleaned.txt';
    listOfLines = clean.readFile(cleanClassFile);
    dictProfCourse = {};
    dictProfCourse = clean.parseCatalog(listOfLines);
    pprint(dictProfCourse);

