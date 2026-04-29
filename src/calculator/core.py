from history import OperationHistory
class Calculator:
    """Calculator with operation history logging."""

    def __init__(self, history=None):
        self.history = history

    def add(self, a, b):
        result = a + b
        if self.history:
            self.history.log(f"{a} + {b}", result)
        return result

    def substract(self, a, b):
        result = a - b
        if self.history:
            self.history.log(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        if self.history:
            self.history.log(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        try:
            result = float(a) / float(b)
            if self.history:
                self.history.log(f"{a} / {b}", result)
            return result
        except ZeroDivisionError:
            raise ValueError("Cannot devide by 0")


# # Keep standalone functions for backwards compatibility
# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     try:
#         return float(a) / float(b)

#     except:
#         raise ValueError("Cannot devide by 0")
    

if __name__ == "__main__":


    H = OperationHistory()
    O = Calculator(history=H)
    print(O.add(1,2))
    print(O.add(1,-6))
    print(O.divide(0,5))
    #print(O.divide(3,0))
    print(H.get_last())
    print(H.entries)
    H.clear()
    print(H.entries)

    # print(add(1,2))
    # print(substract(2,5))
    # print(multiply(0,5))
    # print((divide(3,4)))
    # print(divide(1,0))


