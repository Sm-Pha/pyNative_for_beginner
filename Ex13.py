n = 10
next_ = 0

for i in range(1,n+1):
    for j in range(i,(i*10)+1,i):
        print(j, end=" ")
    print("\t\t")

