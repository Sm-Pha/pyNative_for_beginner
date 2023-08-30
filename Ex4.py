list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

for i in list1:
    for j in list2:
        print(f"{i}{j}")

result_ = [f"{i + j}" for i in list1
           for j in list2]
print(result_)

