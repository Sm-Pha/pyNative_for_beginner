def outer_function(a,b):
    def inner_function(a,b):
        return a + b
    return inner_function(a,b) + 5


print(outer_function(5,10))
