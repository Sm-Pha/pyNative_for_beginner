def list_condition(list1, list2):
    result = []
    for i in list1:
        if i %2 != 0:
            result.append(i)

    for j in list2:
        if j %2 == 0:
            result.append(j)

    print(f"result list: {result}")

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list_condition(list1, list2)
