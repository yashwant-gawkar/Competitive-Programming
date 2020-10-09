def rev_list(l):
	return list(l[len(l)-1:-1:-1])
def l_s(l):
	return "".join(str(ele) for ele in l)
      
s='123'
l=[]
for i in s:
	l.append(i)
rev=rev_list(l)
print(l,rev)
while rev!=l:
    s=rev_list(rev)
    
    print("das")
    l=[]
    for i in s:
        l.append(i)
    rev=rev_list(l)
print(l)
    
