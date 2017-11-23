a=[1,2,3,4,5]
summ=0
flag=0
while flag<len(a):
	summ+=a[flag]
	flag+=1
print summ

sequence=raw_input('please input a series of num split use comma: ')
handleseq=sequence.strip().split(',')
summm=0
for i in range(len(handleseq)):
	summm+=handleseq[i]
print summm