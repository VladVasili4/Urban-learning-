# from random import random


right_stone = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
left_stone = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password_ = []
print('Какое число на левом камне?')
left_number = int(input())
for i in right_stone:
    for j in right_stone:
        if left_number % (i + j) == 0:
            print('---------')
            para = [i, j]
            parasort = sorted(para)
            password_.append(parasort)
            # num1 = right_stone[i] - 1
            # print('num1 : ', num1)
            # num2 = right_stone[j] - 1
            # print('num2 : ', num2)
            print('password_ :', password_)





            # para = {num1, num2}
            # print('password_ :', password_)
            # pass_num = pass_num + {num1, num2}
# print('pass_num :', pass_num )
password_tuple = tuple(password_)
print('password_tuple :', password_tuple)
def convert(password_tuple):
    return set(password_tuple)
convert
print(convert)
# password_set = set(password_tuple)








print(password_)