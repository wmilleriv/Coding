for i in range(0,10000):
	line=''
	if(i%3==0):
		line+="Fizz"
	if(i%5==0):
		line+="Buzz"
	if(i%7==0):
		line+="pop"
	if(i%3!=0 and i%5!=0 and i%7!==0):
		line=str(i)
	print(line)
