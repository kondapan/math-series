def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-1)+lucas(n-2)

def sum_series(element, val1=0, val2=1):
    print(f"values passed {val1}, {val2}")
    if val1==0 and val2==1:
        print("inside default")
        return fibonacci(element)
    return lucas(element)
