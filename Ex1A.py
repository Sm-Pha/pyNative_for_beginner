str1 = "Jamess"
def middle(str1):
    first_ = str1[0]
    last_ = str1[-1]

    if len(str1) == 0:
        return ""
    elif len(str1) %2 !=0:
        middle_ = str1[ (len(str1))//2 ]
        print(first_, middle_, last_)
    else:
        middle_ = str1[(len(str1)-1)//2 :
                       (len(str1) + 2)//2 ]
        print(first_, middle_, last_)

middle(str1)

