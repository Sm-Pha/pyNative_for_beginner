from statistics import mean

str1 = "PYnative29@#8496"

digit_ = []
for i in str1:
    if i.isdigit():
        digit_.append(int(i))

print(f"Sum is: {sum(digit_)} "
      f"Average is  {mean(digit_)}")

