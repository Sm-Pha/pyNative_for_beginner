first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersect_ = first_set.intersection(second_set)

for i in intersect_:
    first_set.remove(i)

print(f"Intersection is  "
      f"{intersect_}")
print(f"First Set after removing common element  "
      f"{first_set}")

