a1=[1,2,3,4,5]
a=[]
res=[]
for i in range(len(a1)):
	temp=[]
	for j in range(len(a1)):
		temp.append(a1[i]*a1[j])
	a.append(temp)
n=len(a1)
for i in range(2*n-1):
	if i<n:
		y=0
		x=i
		s=a[y][x]
		
		while x>0:
			y+=1
			x-=1
			s+=a[y][x]
	

	else:
		ite=i-(n-1)
		y=ite
		x=n-1
		s=a[y][x]
		while x>ite:
			y+=1
			x-=1
			s+=a[y][x]

	res.append(s)
	

print(res)


