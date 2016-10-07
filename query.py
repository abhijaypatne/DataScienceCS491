from pprint import pprint
import clean;

"""
input: two courses list
returns: jaccard coeff
calculate jaccard similarity and return Jaccard coeff.
"""
def jaccardSimilarity(a,b):
    a = a.split();
    b = b.split();
    union = list(set(a + b));
    intersection = list(set(a) - (set(a) - set(b)));
    jaccard_coeff = float(len(intersection))/len(union);
    return jaccard_coeff;

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
    busyProfessors = {};
    for key, value in dictProfCourse.iteritems():
        if (len(value.split("|")) >= 5):
            busyProfessors[key] = value;
    #pprint(busyProfessors);
    return findSimilarInterestProfessors(busyProfessors);

"""
input: dictionary of professors and courses
returns two professors with highest similarity
"""
def findSimilarInterestProfessors(busyProfessors):
    length = len(busyProfessors);
    maxSimilarity = 0;
    #profA = ""; profB = "";
    indexA = -1; indexB = -1;
    courseList = busyProfessors.values();

    # very obvious two nested for loops to find all the combinations
    for i in range(0, length-1):
        for j in range(i+1, length):
            if ((jaccardSimilarity(courseList[i], courseList[j])) > maxSimilarity):
                indexA = i;
                indexB = j;

    if (indexA != -1):
        return (busyProfessors.keys()[indexA] + " and " + busyProfessors.keys()[indexB] );

    return "Every professor has their own interests.";

# start of the program
if __name__ == "__main__":
    cleanClassFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\cleaned.txt';
    listOfLines = clean.readFile(cleanClassFile);
    dictProfCourse = {};
    dictProfCourse = clean.parseCatalog(listOfLines);
    print "Total number of courses: ", query1(dictProfCourse);
    print ("Course taught by Professor Mitchell Theys: " + query2(dictProfCourse));
    print ("Professors with most aligned interests: " + query3(dictProfCourse));

