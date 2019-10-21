#!/usr/bin/env python3

num=int(input("students total number: "))
data={}
subject=["phy","math","hist"]
for x in range(num):
	name=input("pls input students' name {} ".format(x+1))
	marks=[]
	for y in subject:
		marks.append(int(input("your {} score: ".format(y))) )
	data[name]=marks
for x,y in data.items():
	total=sum(y)
	print("{} total score is {}".format(x,total))
	if total<120:
		print("{} failed".format(x))
	else:
		print("{} passed".format(x))
