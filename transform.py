from __future__ import unicode_literals;
import csv;
from urllib2 import urlopen;
from bs4 import BeautifulSoup as BS;

# return soup obj from url
def getSoup(url):
    soup = BS(urlopen('https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions').read(),'html.parser');
    return soup;

# write header to the file
def writeHeader(outputFile, header):
    with open(outputFile, "ab") as file:
        csvwriter = csv.writer(file);
        csvwriter.writerow(header);
        file.close();

# writes required data to the file
def writeData(outputFile, soup):
    tables = soup.find_all("table", { "class" : "wikitable sortable" });
    reqTable = tables[1];

    file = open(outputFile, "ab");
    csvwriter = csv.writer(file);

    for row in reqTable.find_all("tr")[1:51]:
        output = []
        columns = row.find_all("td");
        # find game number
        output.append(columns[0].find('a').get_text().strip().encode('ascii', 'ignore'));
        # find game year
        output.append(columns[1].findAll("span")[-1].get_text()[-4:].encode('ascii', 'ignore'));
        # find winning team
        output.append(columns[2].find('a').get_text().strip());
        # find score
        output.append(columns[3].findAll("span")[-1].get_text().encode('ascii', 'ignore'));
        # find losing team
        output.append(columns[4].find('a').get_text().strip().encode('ascii', 'ignore'));
        # find venue
        output.append(columns[5].findAll("span")[-1].get_text().strip().encode('ascii', 'ignore'));
        # write the output
        csvwriter.writerow(output);

    file.close();


# # starting point of the program
if __name__ == '__main__':
    print "start of the program";
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions";
    outputFile = 'A:\\new_Sync\\Box Sync\\academics\\sem3\\491\\assignments\\HW2\\result.csv';
    header = ["Game number", "year", "winning team", "score", "losing team", "venue"];
    soup = getSoup(url);
    writeHeader(outputFile, header);
    writeData(outputFile, soup);
