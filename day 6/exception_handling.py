# BaseException - SystemExit, KeyboardInterupt, Exception
# docs.python.org <- Exceptions Hierarchy

# fruits = ['apples', 'oranges', 'grapes']

# def division(a, b) -> float:
#     # if b == 0:
#     #     raise ZeroDivisionError('Denominator cannot be Zero')
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         raise ValueError("denominator cannot be zero") from ex
    
# # result = division(1,0)
# # print(result)

# try:
#     result = division(1,0)
#     print(result)
# except Exception as e:
#     print("Cause: ", e.__cause__)
#     print("Exception: ", e)



# try:
#     result = division(1,6)
#     print(result)
# except (IndexError, ZeroDivisionError, Exception) as e:
#     result = {'success': False, 'message': e, 'output': None}
#     print(result)
# finally:
#     print("In finally")
# else:
#     print("in else")

# except IndexError as e:
#     print(e)
# except Exception as e1:
#     result = {'success': False, 'message': e1, 'output': None}
#     print(result)

from custom_ex import InvalidAgeError


def checkAge(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        return f'Age: {age} is valid for voting'
    
try:
    result = checkAge(1)
    print(result)
except InvalidAgeError as e:
    print(e)







