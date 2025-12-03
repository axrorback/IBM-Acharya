# try:
#     number = 10
#     denom = 1
#     res = number / denom
# except ZeroDivisionError:
#     print("Can not divide by zero")
# except Exception as e:
#     print(e)
#
# else:
#     print(f'Try block executed successfully. Result is {res}')
#
# finally:
#     print("This is always executed")



def repeat_sentence(sqc):
    return '->'.join([(i*j).capitalize() for i , j in enumerate(sqc , 1)])


print(repeat_sentence('abcd'))

