import requests
import os

#response = requests.get("https://metruyenchu.com/truyen/thuong-nguyen-do/")
#print(response)
from bs4 import BeautifulSoup
#import requests
html = requests.get("https://metruyenchu.com/truyen/thuong-nguyen-do/").text
soup = BeautifulSoup(html, 'html5lib')
divs = soup("table","table border-bottom mb-4 mt-5")
title = divs[0].find("div", "media-body").text
time = divs[0].find("div","pl-3").text
#title = divs[0].find("p","movie-title-1").text
print(title + "\t" +  time)




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
