a_file = open("python.txt", "r") #Get list of lines
lines = a_file.readlines()
a_file.close()

del lines[5]

new_file = open("sample.txt", "w+")
for line in lines:
    new_file.write(line)

new_file.close()

