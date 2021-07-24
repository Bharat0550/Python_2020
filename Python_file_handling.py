#file handling using python

# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.


#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist


# "x" - Create - Creates the specified file, returns an error if the file exists




#opening a file

f=open("C:\HTML Tutorials\CSS Basic tutotials\python for brginers\demo_file.txt","rt")

 print(f.read())
 print(f.read(17))

 print(f.readline())

 print(f.readline())


#read line by line
 for i in f:
     print(f)
 f.close()

#writting to an existing file

 f=open("C:\HTML Tutorials\CSS Basic tutotials\python for brginers\demo_file.txt","at")
 f.write("ggggggggggg")
 f.close()

 f=open("C:\HTML Tutorials\CSS Basic tutotials\python for brginers\demo_file.txt","rt")
 t=f.read()
 print(t)
# Overwritting the content of existing file
 f=open("C:\HTML Tutorials\CSS Basic tutotials\python for brginers\demo_file.txt","wt")
 f.write("hello this is an overwrite file")
 f.close()
 f=open("C:\HTML Tutorials\CSS Basic tutotials\python for brginers\demo_file.txt","rt")
 print(f.read())

# creating a new file

 f=open("created_by_python.txt","x")
 f.write("jalebi babay")
 f.close()

 f=open("created_by_python.txt","rt")
 print(f.read())

 g=open("zero.txt","x")
 g.write("bharat singh")
 g.close()
 g=open("zero.txt","at")
 g.write("hello bolo")
 g.close()

 g=open("zero.txt","rt")
 print(g.read())

# deleting a file
 import os
 os.remove("zero.txt")

 f=open("zero.txt","rt")

 import  os
 if os.path.exists("zero.txt"):
     os.remove("zero.txt")
 else:
     print("file nahi hai bro")    

#deleting a folder
 import os
 os.rmdir("myfolder")
