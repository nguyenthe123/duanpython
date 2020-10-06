import requests
import os

response = requests.get("https://metruyenchu.com/truyen/thuong-nguyen-do/")
print(response)

# Mo mot file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Ghi mot chuoi
os.write(fd,response.content)

# Dong file da mo
os.close( fd )
# 184 - 195
a_file = open("foo.txt", "r")
#get list of lines
lines = a_file.readlines()
a_file.close()
new_file = open("foo.txt", "w")
for line in lines:
    if  ("line183" < line < "line196"):
        new_file.write(line)
new_file.close()
