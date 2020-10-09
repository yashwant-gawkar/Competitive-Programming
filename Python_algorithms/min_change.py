def min_change(n):
	a=[-1 for i in range(n+1)]
	a[0]=0
	m_i=1000

	for i in range(1,n+1):
		m_i=10000
		for j in [1,5,8]:
			if i-j>=0:
				if i==10:
					print(m_i,a[i-j]+1)
				m_i=min(m_i,a[i-j]+1)
			
		a[i]=m_i
	print(a)

min_change(10)





