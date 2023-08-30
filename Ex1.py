l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_index = l1[1::2]
even_index = l2[::2]

print(f"Element at odd-index positions "
      f"from list one \n {odd_index}")
print(f"Element at even-index positions "
      f"from list two \n {even_index} \n")
print(f"Printing Final third list \n "
      f"{odd_index + even_index}")

