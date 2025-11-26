# Armstrong rule
# 153 = 1^3  + 5^3 + 3^3

# def is_armstrong(num):
#     digits = str(num)
#
#     power = len(digits)
#
#     total = 0
#     for digit in digits:
#         total += int(digit) ** power
#
#     return total == num
#
#
# number = 153
# if is_armstrong(number):
#     print(f"{number} Armstrong!")
# else:
#     print(f"{number} Not Armstrong")



# text = 'Ahrorjon Ibrohimjonov'
#
# f = open('axrorback.txt','w')
# f.write(text)
# f.close()


read = open('axrorback.txt', 'r')

print(read.read())