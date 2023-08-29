n = 10
previous = 0

print(f"Printing current and "
      f"previous number sum "
      f"in a range ({n})")

for i in range(n):
    print(f"Current Number {i} "
          f"Previous Number {previous}  "
          f"Sum: {previous + i}")
    previous = i


