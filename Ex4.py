user_input = "pynative"
n = 4

def remove_chars(user_input, n):
    print(f"Original string: {user_input}\n")
    # for i in range(n,len(user_input)):
    #     print(user_input[i])

    print(user_input[n:])

remove_chars(user_input, n)

