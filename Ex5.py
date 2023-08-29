def is_first_last(list_):

    print(f"Given list: {list_}")

    first_ = list_[0]
    last_ = list_[-1]

    if first_ == last_:
        result = True
    else:
        result = False

    print(f"result is {result}\n")

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

is_first_last(numbers_x)
is_first_last(numbers_y)

