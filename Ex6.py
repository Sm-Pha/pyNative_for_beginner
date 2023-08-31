s1 = "Abc"
s2 = "Xyz"; s2_ = s2[::-1]

s3 = []; s3 += [s1]; s3 += [s2]
longest_ = max(s3, key=len)

result = ""
for i in range(len(longest_)):
    if i < len(s1):
        result += s1[i]
    if i < len(s2_):
        result += s2_[i]
print(result)

