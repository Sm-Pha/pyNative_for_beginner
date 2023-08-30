sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(f"Original list \n {sample_list} \n")

count_dict = dict()
for i in sample_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

    # print(f"{i} : {count_dict[i]}") #11: 1, 11: 2

print(f"Printing count of each item  \n{count_dict}")

