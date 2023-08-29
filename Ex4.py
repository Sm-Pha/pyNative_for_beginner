str1 = "PyNaTive"

lower_array = []
upper_array = []

for i in str1:
    if i.islower():
        lower_array.append(i)
    else:
        upper_array.append(i)
print(''.join(lower_array+upper_array))

