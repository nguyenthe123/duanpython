a_file = open("out1.tex", "r")
lines = a_file.readlines()
a_file.close()
# it start from line 35
print('Nhap stt tiep can dien: ')
p = input()
y = int(p)
print('Nhap so sinh vien ban muon nhap vao bang diem: ')
ssv = input()
total = int(ssv)
i = y
k = 32 + 2*y
for u in range(0,total):
    stt = str(i)
# Data
    print('Nhap ma so sinh vien: ')
    mssv = input()
    print('Ho va ten :') 
    name = input()
    print('Ngay thang nam sinh: ') 
    birth = input()
    print('Lop :') 
    cla = input()
    print('Chuyen can: ') 
    often = input()
    p = r"\\"
# Creat new line stt1 & ms & birth & class & often & sign & mid & note
    d = '\t\t' + stt + ' & ' + mssv + ' & ' + name + ' & ' + birth + ' & ' + cla + ' & ' + often + ' & & & ' + p + '\n'

    lines[k] = d
# Write into new file
    new_file = open("out1.tex", "w+")

    for line in lines:
        new_file.write(line)
    new_file.close()
    i = i + 1
    k = k + 2
import os
cmd = "pdflatex out1.tex"
failure = os.system(cmd)
if failure:
    print("Sai cmd")
#viewing .pdf
cmd = "evince out1.pdf &"
failure = os.system(cmd)
if failure:
    print("Xem pdf sai")

