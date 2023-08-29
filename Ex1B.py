str1 = "JhonDipPeta"
print(len(str1)) #11

def get_middle_three_chars(str1):
    if len(str1) == 0:
        return ""
    elif len(str1) %2 !=0:
        middle_ = len(str1)//2

        range_middle = str1[middle_-1: middle_+2]
        print(range_middle)
    else:
        middle_ = len(str1)//2

        range_middle = str1[middle_-2: middle_+2]
        print(range_middle)

get_middle_three_chars(str1)