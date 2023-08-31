n = 10
def recursive(n):
    if n:
        return n + recursive(n - 1)
    else:
        return 0

print(recursive(n))
