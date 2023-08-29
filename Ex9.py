# % * //
def is_palindrome(n):
    print(f"original number {n}")
    temp = n
    reverse_ = 0
    while(n > 0):
        print(f"n_before: {n}\n")

        digit = n % 10; print(f"digit: {digit}\n")

        reverse_ = reverse_ * 10 + digit; print(f"reverse_: {reverse_}\n")

        n = n//10; print(f"n_after: {n}\n")
        print(f"------------")
    if temp == reverse_:
        result = ("Yes. "
                  "given number is palindrome number")
    else:
        result = ("No. "
                  "given number isn't palindrome number")
    print(f"{result} \n")

# is_palindrome(121)
is_palindrome(125)
