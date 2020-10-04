from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import sys 

# demo url "https://www.geeksforgeeks.org/queue-data-structure/" 

def getAllLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))

    return links

linksArray = getAllLinks(sys.argv[1])

def RemoveDuplicateLinks(linksArray): 
    final_link_Array_List = [] 
    for linkItem in linksArray: 
        if linkItem not in final_link_Array_List: 
            final_link_Array_List.append(linkItem) 
    return final_link_Array_List 

finalLinkList = RemoveDuplicateLinks(linksArray)
print('All list of links:  ',finalLinkList)
