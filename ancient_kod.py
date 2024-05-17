from random import random


right_stone = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
left_stone = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('Какое число на левом камне?')
left_number = int(input())
for i in right_stone:
    for j in right_stone:
        if left_number % (i + j) == 0:
            print('WOW !')
            password_ = {[], []}
            password_.append(i) 





print(password_)