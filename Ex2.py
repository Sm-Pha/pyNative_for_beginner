s1 = "Ault"
s2 = "Kelly"
def append_middle(s1, s2):
    if len(s1) == 0:
        print(s2)
    else:
        middle_ = len(s1)//2
        print(s1[:middle_],s2,s1[middle_:])

append_middle(s1, s2)

