def palidrome(num):
	num2=num
	reverse=0
	while(num>0):
		dev=num%10
		reverse=reverse*10+dev
		num=num//10
	if num2==reverse:
		print("number is a palidrome")
	else:
		print("number is not palidrome")
if __name__=='__main__':
	palidrome(123)