def ugly_range(n):
	ugly=[1]
	curr_2,curr_3,curr_5=2,3,5;
	p1,p2,p3=0,0,0
	for i in range(1,n):    # since one is included
		ugly.append(min(curr_2,curr_3,curr_5))      #Since all values are:2x1,2x2,2x3,..or 3x1,3x2,.... or 5x1,5x2.....
		if ugly[i]==curr_2:
			p1+=1
			curr_2=ugly[p1]*2
		if ugly[i]==curr_3:
			p2+=1
			curr_3=ugly[p2]*3
		if ugly[i]==curr_5:
			p3+=1
			curr_5=ugly[p3]*5


	print(ugly[-1])

ugly_range(150)