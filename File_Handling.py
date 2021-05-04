"""
# open File read Mode
f = open("try.txt", "r")

# We also give the length of character
# print(f.read(10))

# print all the file
# print(f.read())

# read only one line if we want read next time then print it again
# print(f.readline())

# open file using For loop

for x in f:
    print(x)

f.close()"""

"""
# open File for Append something
f = open("try.txt", "a")

f.write("i am a new Line now")

f.close()
f = open("try.txt", "r")

print(f.read())
"""
"""
# create a new file
k = open("New_file.txt", "x")"""

"""
# delete File
import os

os.remove("New_file.txt")
"""
