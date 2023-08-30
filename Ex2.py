list1 = [34, 54, 67, 89, 11, 43, 94]
add_element = 11

remove_at = 4
add_at = 2

list1.pop(remove_at)
print(f"List After removing "
      f"element at index {remove_at} {list1}")

list1.insert(add_at, add_element)
print(f"List after Adding "
      f"element at index {add_at}  {list1}")

list1.append(add_element)
print(f"List after Adding "
      f"element at last  {list1}")

