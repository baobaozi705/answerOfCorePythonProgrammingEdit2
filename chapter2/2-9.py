arr=[1,2,3,4,5]

def avg(alist):
	num=0
	for i in range(len(alist)):
		num+=alist[i]
	print (float(num)/len(alist))

avg(arr)
