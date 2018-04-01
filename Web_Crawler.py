import requests
import math
from bs4 import BeautifulSoup

visited_links = []
unique_links = []
f = open("List of URL's.txt", "w")
f1 = open("Tokens.txt", "w")
f2 = open("Dictionary.txt", "w")
f3 = open("Bigrams.txt", "w")
f4 = open("matrix.txt", "w")
num = 0
unique_words = []
dic = {}
list = []
total_words = []
freq1 = {}
element = {}
out_d = {}
in_d = {}
# w, h = 519,2
# mat = [[0 for x in range(w)] for y in range(h)]
'''
def matrix(i,j,freq):
    global mat
    try:
        mat[i][j] = freq
    except UnicodeEncodeError:
        pass
    try:
        f4.write(str(mat[i][j]) + " ")
    except:
        pass
        '''
def out():
    ff = open("List of URL's.txt", "r")
    i = 0
    while (i < 10):
        count = 0
        s = ff.readline()
        source_code = requests.get(s)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a'):
            try:
                p = (link.get('href'))
                count = count + 1
            except:
                pass
        try:
            out_d[i] = [{s: count}]
        except:
            pass
        print(out_d[i])
        i = i + 1
    print("\n"+"\n")
def ind():
    with open("List of URL's.txt") as p:
        content = p.readlines()
        content = [x.strip() for x in content]
        w, h = 10, 10
        Matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(0,10):
            for j in range(0,10):
                Matrix[i][j] = 0
        #print(Matrix)
    i = 0
    while (i < 10):
        count = 0
        s = content[i]
        for j in range(0,10):
            if (j!=i):
                source_code = requests.get(content[j])
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                for link in soup.findAll('a'):
                    try:
                        if (link.get('href')[:6] == 'https:' or link.get('href')[:5] == 'http:'):
                            p = link.get('href')
                        else:
                            p = "http://www.cricbuzz.com/" + (link.get('href'))
                        #print(p)
                        if(p == s):
                            count = count+1
                            Matrix[i][j] = 1
                            break
                        elif(p.__contains__("http://www.cricbuzz.com/")):
                            Matrix[i][j] = 0
                    except:
                        pass
                try:
                    in_d[i] = [{s: count}]
                except:
                    pass
        for i in range(0, 10):
            print(Matrix[i])
        #print(in_d[i])
        i = i + 1
#def adj():
def trade_spider(url):
    href = ""
    temp_unique_words = []
    temp_total_words = []
    global dic
    global element
    global freq1
    global visited_links
    global num
    #print(num)
    num += 1
    l1 = len(unique_links)
    #print("l1=" + str(l1))
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a'):
        try:
            if (link.get('href')[:6] == 'https:' or link.get('href')[:5] == 'http:'):
                href = link.get('href')
            else:
                href = url + (link.get('href'))
            visited_links.append(href)
        except:
            pass
    for link in soup.findAll(['a', 'hr', 'div', 'p', 'h2', 'ul', 'li', 'strong', 'span', 'b', 'i', 'label']):
        title = link.string
        if title == None:
            pass
        else:
            words = title.split()
            for word in words:
                try:
                    if word not in unique_words:
                        total_words.append(word)
                        unique_words.append(word)
                        temp_unique_words.append(word)
                        temp_total_words.append(word)
                        f1.write(word + "\n")
                    else:
                        total_words.append(word)
                        temp_total_words.append(word)
                except:
                    pass
    i = 0
    for unique in unique_words:
        freq = 0
        j = 0
        for word in temp_total_words:
            if word == unique:
                freq += 1
        if not freq == 0:
            if unique not in dic.keys():
                dic[unique] = [{url: "TF is: " + str(freq)}]
            else:
                dic[unique] += [{url: "TF is: " + str(freq)}]
        # matrix(i,j,freq)
        i + 1
        j + 1

    for i in visited_links:
        if i not in unique_links:
            unique_links.append(i)
    visited_links = []
    print("unique=" + str(len(unique_links)))

trade_spider('http://www.cricbuzz.com/')
'''
for i in range(0, 10):
    # if '#' not in unique_links[i] and not unique_links[i].endswith('//'):
    trade_spider(unique_links[i])
'''
for link in unique_links:
    f.write(str(link) + "\n")
for x in dic:
    try:
        ratio = len(dic[x]) / 5
        idf = (math.log(ratio, 10))
        f2.write(str(x) + " " + str(dic[x]) + " IDF is: " + str(idf * -1) + "\n")
    except UnicodeEncodeError:
        pass
f.close()
f1.close()
f2.close()

def bigram():
    bigrams = []
    for i in range(97, 123):
        for j in range(97, 123):
            bigrams.append(chr(i) + chr(j))
    f = open("Tokens.txt", "r")
    text = f.readlines()
    for list_element in bigrams:
        for word in text:
            if list_element in word:
                if list_element not in element.keys():
                    element[list_element] = [{str(word).replace('\n', '')}]
                else:
                    element[list_element] += [{str(word).replace('\n', '')}]
    for x in element:
        f3.write(str(x) + " " + str(element[x]) + "\n")
bigram()
#out()
ind()
f.close()
f3.close()
