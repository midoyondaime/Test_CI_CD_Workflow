
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return float(a)/float(b)
    
    except ZeroDivisionError as e:
        return ValueError("Cannot devide by 0")
    

if __name__ == "__main__":

    print(add(1,2))
    print(substract(2,5))
    print(multiply(0,5))
    print((divide(3,4)))
    print(divide(1,0))


