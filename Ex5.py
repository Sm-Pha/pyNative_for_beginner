from itertools import cycle
import itertools


def student(*arg1):
    key_ = ["ID", "Name"]
    student_array = list(arg1)

    result = [x + ' : ' + y
              for x, y in zip(itertools.cycle(key_), student_array)]
    print(result)

    zip_list = list(zip(key_, cycle(student_array))
                    if len(key_) > len(student_array)
                    else zip(cycle(key_), student_array))
    print(zip_list)  # zip object/ tuple => list: [(,), (,)]


student("1", "Anna", "2", "Papa", "3", "Papa")

