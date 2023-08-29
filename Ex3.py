s1 = "America"
s2 = "Japan"
def middle(str1):
    first_ = str1[0]
    last_ = str1[-1]

    if len(str1) == 0:
        return ""
    elif len(str1) % 2 != 0:
        middle_ = str1[ (len(str1))//2 ]
        return first_, middle_, last_
    else:
        middle_ = str1[(len(str1)-1)//2 :
                       (len(str1) + 2)//2 ]
        return first_, middle_, last_
def mix_each_first_middle_last(s1,s2):
    mix_s1 = middle(s1)  # 3
    mix_s2 = middle(s2)  # 3

    for i in range(len(mix_s1)):
        print(mix_s1[i] + mix_s2[i])

mix_each_first_middle_last(s1,s2)
