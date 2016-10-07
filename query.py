from pprint import pprint
import clean;

"""
"""
def jaccardSimilarity(a,b):
    a=a.split()
    b=b.split()
    union = list(set(a+b))
    intersection = list(set(a) - (set(a)-set(b)))
    print "Union - %s" % union
    print "Intersection - %s" % intersection
    jaccard_coeff = float(len(intersection))/len(union)
    print "Jaccard Coefficient is = %f " % jaccard_coeff

"""
Query for question 1.1
"""
def query1(dictProfCourse):
    courseList = [];
    for key,value in dictProfCourse.iteritems():
        courses = value.split("|");
        for course in courses:
            courseList.append(course);
    return len(set(courseList));

"""
Query for question 1.2
"""
def query2(dictProfCourse):
    courses = dictProfCourse.get("Theys");
    courseList = courses.split("|");
    # separating by ';' because course names also contain commas ','
    return ";".join(courseList);

"""
Query for question 1.3
"""
def query3(dictProfCourse):
    print "Hello";


# start of the program
if __name__ == "__main__":
    print "Started";
    cleanClassFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\cleaned.txt';
    listOfLines = clean.readFile(cleanClassFile);
    dictProfCourse = {};
    dictProfCourse = clean.parseCatalog(listOfLines);
    print ("Total number of courses: ", query1(dictProfCourse));
    print ("Course taught by Professor Mitchell Theys: " + query2(dictProfCourse));
    query3(dictProfCourse);

