import os
fd = "python.txt"

print(os.getcwd())

# popen() = open
file = open(fd, 'w')
file.write("Hello Python!22222222222222222222")
file.close()
#file = open(fd,'r')
#text = file.read()
#print(text)

# popen() ket noi va truy cap file truc tiep
file = os.popen(fd, 'w')
file.write("Hello Python!")
file.close()
