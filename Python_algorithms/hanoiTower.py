def move(a,b):
    print("Move {} to {}".format(a,b))


def hanoi(n,from_t,helper,to):
    if n==0:
        pass
    else:
        hanoi(n-1,from_t,to,helper)
        move(from_t,to)
        hanoi(n-1,helper,from_t,to)
        
hanoi(3,"A","B","C")
    
