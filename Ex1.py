input1 = int(input("number 1 = "))
input2 = int(input("number 2 = "))

mul_ = input1 * input2
sum_ = input1 + input2

if mul_ <= 1000:
    result = (f"The result is {mul_}")
else:
    result = (f"The result is {sum_}")

print(result)

