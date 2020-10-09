def number_of_paths(m,n):#In a rectangle
    if m==1:
        return 1
    if n==1:
        return 1
    return number_of_paths(m,n-1)+number_of_paths(m-1,n)

print(number_of_paths(2,2))