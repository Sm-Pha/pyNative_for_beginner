str1 = "P@#yn26at^&i5ve"

alpha_ = []
digit_ = []
symbol_ = []
for i in str1:
    if i.isalpha():
        alpha_.append(i)
        len_alpha = len(alpha_)
    elif i.isdigit():
        digit_.append(i)
        len_digit = len(digit_)
    else:
        symbol_.append(i)
        len_symbol = len(symbol_)

print(f"Total counts of chars, "
      f"digits, and symbols \n")
print(f"Chars = {len_alpha}")
print(f"Digits = {len_digit}")
print(f"Digits = {len_symbol}")




