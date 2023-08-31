roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John':47, 'Emma':69,
               'Kelly':76, 'Jason':97}

list_ = []
for i in sample_dict.values():
    # print(i)
    if i in roll_number:
        list_.append(i)
print(f"After removing unwanted "
      f"elements from list {list_}")


