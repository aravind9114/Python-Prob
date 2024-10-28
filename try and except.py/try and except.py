"""def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" ) 
    else:
        print(reci)
    finally:
        print("finally demo")
reciprocal(2)"""
class CustomError(Exception):

    pass  
def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative")

try:
    age = -5
    validate_age(age)
except CustomError as e:
    print(f"Error: {e}")  


