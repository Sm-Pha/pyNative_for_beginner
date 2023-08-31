first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

if first_set.issubset(second_set): first_set.clear()
if second_set.issubset(first_set): second_set.clear()

print(f"First set is subset of second set - {first_set.issubset(second_set)} "
      f"Second set is subset of First set -  {second_set.issubset((first_set))} "
      f"First set is Super set of second set -  {first_set.issuperset(second_set)} "
      f"Second set is Super set of First set -  {second_set.issuperset(first_set)} "
      f"First Set  {first_set} "
      f"Second Set  {second_set}")

