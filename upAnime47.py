import requests
import os

#response = requests.get("https://anime47.com")
#print(response)
from bs4 import BeautifulSoup
#import requests
html = requests.get("https://anime47.com").text
soup = BeautifulSoup(html, 'html5lib')
divs = soup("div","movie-meta")
for i in range(5,25):
    title = divs[i].find("div", "movie-title-1").text
    eps = divs[i].find("span", "ribbon").text
#title = divs[0].find("p","movie-title-1").text
    print(title + "\t" + eps)
#import pdfkit

# Mo mot file
#fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# Ghi mot chuoi
#os.write(fd,response.content)
# Dong file da mo
#os.close( fd )
#184 - 196
#a_file = open("foo.txt", "r")
#lines = a_file.readlines()
#a_file.close()
#new_file = open("foo2.txt", "w")
#for i in range(1,277):
#        if (183<=i<=195):
#            new_file.write(lines[i])
#new_file.close()
#pdfkit.from_file('foo2.html', 'out.pdf')
#cmd = "evince out.pdf &"
#failure = os.system(cmd)
