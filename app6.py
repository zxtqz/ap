# def esl_reqemler(x):
#     return False

# bolme = []

# for i in range(x):
#     if x % i ==0:
#         divide.append(i)


# import random

# def card_selection(x):
#     cards = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
#     card_type = ["Hearts","Diamonds"]

#     if 1 <= x <= 36:
#         card = cards

# 4. # def xosbext_number(x):
#     if len(x)==6 and x.isdigit():
#         ilk_3 = int(x[0]) + int(x[1]) + int(x[2])
#         son_3 = int(x[3]) + int(x[4]) + int(x[5])

#         if ilk_3 == son_3:
#             return "Xosbext reqemdir"
#         else:
#             return "Xosbext reqem deyil..."
    
# print(xosbext_number("111111"))

# 5. # import datetime

# x = datetime.datetime(2020, 5, 17)

# x2 = datetime.datetime(2021,6,18)

# if x>x2:
#     print("First date is longer than the second date",x)
#     print("first date: ",x)
#     print("second date: ",x2)
# if x2>x:
#     print("Second date is longer than the first date",x2)
#     print("first date: ",x)
#     print("second date: ",x2)
# else:
#     print("no date")

# 7.# import random

# numbers = []

# kicik_number = 20
# boyuk_number = -20
# sifirlarin_sayi = 0

# menfi_sayi = 0
# musbet_sayi = 0

# for i in range(10):
#     ran_number = random.randint(-20,20)
#     numbers.append(ran_number)

# for i in numbers:
#     if i < kicik_number:
#         kicik_number=i
#     if i > boyuk_number:
#         boyuk_number = i
#     if i>0:
#         musbet_sayi +=1
#     elif i<0:
#         menfi_sayi +=1
#     else:
#         sifirlarin_sayi +=1      
    
# print(numbers)

# print(sifirlarin_sayi)
# print(boyuk_number)
# print(kicik_number)
# print("musbetlerin sayi: ",musbet_sayi)
# print("menfilerin sayi: ", menfi_sayi)

# 8.# def max_numbers(numbers):
#     return max(numbers)

# def minimum_numbers(numbers):
#     return min(numbers)

# print(max_numbers(1,2,5,7,9,10))
# print(minimum_numbers(1,2,5,7,9,10))

# def reverse(number):
#     number.reverse()
#     return number
# reqemler = [1,4,15,30,37,677]
# print(reverse(reqemler))