#read a fileline

# Open a file
fo = open("python.txt",'r')
print ("Name of the file: ", fo.name)
line = fo.readline()
print( "Read Line: ",line)
line = fo.readline(5)
print ("Read Line: ",line)


fo.close()
