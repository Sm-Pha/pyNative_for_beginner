source = "*"
n = 5

for i in range(n, 0, -1):
    for j in range(0, i-1):
        print(source, end=" ")

    print(" ")
