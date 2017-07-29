def comb(n,r):
	c=1
	for i in range(r,n):
		c*=((i+1)/(n-i))
	return int(round(c,2))

while 1:
    n=int(input("n: "))
    r=int(input("r: "))
    print(comb(n,r),'\n')
