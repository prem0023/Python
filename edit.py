# this program is under file handling

f = open('Mydata', 'r')         #to read data writtrn in MyData file


f1 = open('New', 'w')           #to write data in 'New' file if not exist then it will created automatecly, but it is temporary not save
f1.write("My name.., ")         #it will write the data which inside " " 
f1.write("My name is prem")     #it will write the data which inside " "
f1.write("\n")                  #it will write the data which inside " " (here it will change line)

for data in f:                  # it mean to MyData file
    f1.write(data)              #write all data which is in 'MyData' to f1(i.e New)
