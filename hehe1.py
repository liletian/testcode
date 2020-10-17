#!/usr/bin/python
import os
date_string = os.popen("ls -l").read()
#print(date_string)
# test pull

i=0
y=""
lst=[]
for x in date_string:
    if (x!="\n"):
        y=y+x
    else:
#        print(y)
        if(i>0):
            y=y.split()
            lst.append(y)
            print("kill -9 " + y[1])
        y=""
        i=i+1
print(i)

ii=0

for ii in range(len(lst)):
    print("kill -9 " + lst[ii][1])
    ii=ii+1
