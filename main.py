def print_params(a, b, c): #*args  **kwargs
    print(a, b, c)


dict_ = {'a':1, 'b':2 , 'c': 3}
print_params(**dict)