list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

combine_ = zip(list1, list2)

result_ = [ f"{i}{j}" for i,j in combine_]
print(result_)


