n=[2,3,5,7,8,4,6,7]
for sub in n:
    for even in str(n):
        if even %2==0:
            print("even")
        else:
            print("odd")