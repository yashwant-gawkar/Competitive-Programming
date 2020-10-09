def dyn_knapsack_rep(W):
	value=[0]
	n=len(v)
	for i in range(1,W+1):
		value.append(0)


		for j in range(n):
			if w[j]<=i:
				val=value[i-w[j]]+v[j]
				if val>value[i]:
					value[i]=val
	print(value)


v=[30,14,16,9]
w=[6,3,4,2]
dyn_knapsack_rep(10)