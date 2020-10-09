class Prime():

    def arr_prime(self,p):
        prime=[1 for i in range(p+1)]
        prime[0:2]=[0,0]
        j=2
        for i in range(2,int(p**0.5+1)):
            j=i
            if prime[i]==1:
                while j*i<=p:
                    prime[j*i]=0
                    j+=1
        r=[i for i in range(p+1) if prime[i]==1]
        return r


a=100
p=Prime()
print(p.arr_prime(a))
                    
        
        