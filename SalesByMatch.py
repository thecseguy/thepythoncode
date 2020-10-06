#Solution to https://www.hackerrank.com/challenges/sock-merchant/problem


ar=[10,20, 20, 10, 10, 30, 50, 10, 20]
c=0
i=0
while i<(len(ar)-1):
	print(ar[i])
	print(i)
	if ar[i] == ar[i+1]:
		c=c+1
		i=i+2
	else:
		i=i+1


print(c)
