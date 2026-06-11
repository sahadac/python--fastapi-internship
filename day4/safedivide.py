class CustomZeroDivisionError(Exception):
    pass
def safe_divide(a, b):
    if b == 0:
        raise CustomZeroDivisionError("Cannot divide by zero")
    return a / b
try:
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
except CustomZeroDivisionError as e:
    print("Error:", e)