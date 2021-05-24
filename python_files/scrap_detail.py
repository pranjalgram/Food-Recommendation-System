import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrapper(item_name):
    url = 'https://en.wikipedia.org/wiki/' + item_name
    test = urlopen(url)
    souper = BeautifulSoup(test,'lxml')
    scrap_element=[]
    for para in souper.find_all('p'):
        scrap_element.append(para.text)
    result = []
    for to_be_cleaned in scrap_element[1:]:
        temp = citation_removal(to_be_cleaned)
        result.append(temp)
    return result


def citation_removal(dirt):
    flushed = ''
    i=0
    while i < len(dirt):
        #print(kk[i])
        if dirt[i]=='[':
            while True:
                if dirt[i]  == ']':
                    break
                i=i+1
        else:
            flushed = flushed + dirt[i]
        i=i+1
    a = re.sub(' +', ' ', flushed)    
    return a 
