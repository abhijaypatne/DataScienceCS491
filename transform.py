import csv;
from urllib2 import urlopen;
from bs4 import BeautifulSoup as BS;

# return soup obj from url
def getSoup(url):
    soup = BS(urlopen('https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions').read(),'html.parser');
    return soup;

# write header to the file
def writeHeader(outputFile, header):
    with open(outputFile, "a") as file:
        csvwriter = csv.writer(file);
        csvwriter.writerow(header);

# writes required data to the file
def writeData(outputFile, soup):
    tables = soup.find_all("table", { "class" : "wikitable sortable" });
    reqTable = tables[1];
    for row in reqTable.find_all("tr")[1:]:
        columns = row.find_all("td");
        number = columns[0].find('a').get_text().strip();
        print number



# # starting point of the program
if __name__ == '__main__':
    print "start of the program";
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions";
    outputFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\result.csv';
    header = ["Game number", "year", "winning team", "score", "losing team", "venue"];
    soup = getSoup(url);
    writeHeader(outputFile, header);
    writeData(outputFile, soup);
