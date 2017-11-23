userinput=raw_input('please input a number between 1 to 100: ')
while int(userinput) not in range(1,100):
	print 'error!please input a number between 1 to 100!!!'
	userinput=raw_input('please input a number between 1 to 100 again: ')
print 'success!'


