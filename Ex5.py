list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.reverse()
new_list2 = list2

new_list = zip(list1, new_list2)
print(list(new_list))
