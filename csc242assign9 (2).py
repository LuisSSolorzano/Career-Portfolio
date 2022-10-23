
import os

def TextExtractor(root):
    'recursively crawl through a directory structure comibining all the text contents into one string with path'
    text = ''
    for item in os.listdir(root):
        n = os.path.join(root, item)
        if os.path.isdir(n):
            text += TextExtractor(n)
        else:
            text += 'PATH: ' + n + '\n' + open(n, 'r').read() + '\n'
    return text            
        

def findAllDirectoriesWithFiles(root):
    'return a list of all directories that contain files'
    n = ''
    lst = []
    contain_file = False

    for item in os.listdir(root):
        n = os.path.join(root, item)
        if os.path.isdir(n):
            lst = lst + findAllDirectoriesWithFiles(n)
        else:
            contain_file = True
            
    if contain_file:
        lst.append(root)

    return lst


def fileStartsWithCount(folder,chars):
    'Count of files that start with specific characters'
    count = 0

    for item in os.listdir(folder):
        n = os.path.join(folder, item)

        if os.path.isdir(n):
            count += fileStartsWithCount(n, chars)
        elif item.startswith(chars):
            count += 1

    return count
    


from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testLParser(url):
    content = urlopen(url).read().decode()
    parser = ListParser()
    parser.feed(content)
    return parser.getListItems()

class ListParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = []
        self.foundTag = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' or tag == 'ol' or tag == 'li':
            self.foundTag = True

    def handle_endtag(self, tag):
        if tag == 'ul' or tag == 'ol' or tag == 'li':
            self.foundTag = False
            
    def handle_data(self, data):
        if self.foundTag == True:
            self.list.append(data.strip())
        
    def getListItems(self):
        for elem in self.list:
            if elem == '':
                self.list.remove(elem)
        return self.list

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

#https://www.cdm.depaul.edu/Faculty-and-Staff/Pages/faculty-info.aspx?fid=193

def testTeachingParser(url):
    content = urlopen(url).read().decode()
    parser = CourseParser()
    parser.feed(content)
    return parser.getCourses()

class CourseParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = []
        self.foundSection = False
        self.foundCourse = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'section' and attrs and attrs[0] and attrs[0][1] == 'Faculty--Courses':
            self.foundSection = True

        elif tag == 'span' and self.foundSection:
            if attrs and attrs[0] and attrs[0][1] == 'col1':
                self.foundCourse = True

    def handle_endtag(self, tag):
        if tag == 'section':
            self.foundSection = False

    def handle_data(self, data):
        if self.foundSection == True and self.foundCourse == True:
            self.list.append(data.strip())
            self.foundCourse = False
        
    def getCourses(self):
        for elem in self.list:
            if elem == '':
                self.list.remove(elem)
        return self.list


txt=TextExtractor('Test')
#print(txt)
#print(findAllDirectoriesWithFiles('Test'))
#print(fileStartsWithCount('Test','f'))
#print(testLParser('http://zoko.cdm.depaul.edu/csc242/lists.html'))
print(testTeachingParser('https://www.cdm.depaul.edu/Faculty-and-Staff/Pages/faculty-info.aspx?fid=193'))

