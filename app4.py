# import random

# numbers= []

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

samsung = ["Samsung S5", "Samsung S6","Samsung S7","Samsung S8"]

print(len(samsung))
print(samsung[0]),print(samsung[-1])
samsungs5 = samsung.index("Samsung S5") 
samsung[samsungs5] = "Samsung S9"
print(samsung)
if "Samsung S6" in samsung:
  print("Yes Samsung S6 is in the list")

print(samsung[0:2])

samsung[-1] = "Samsung S9"
samsung[-2] = "Samsung S10"
print(samsung)

iphones = ["Iphone X","Iphone XR"]
samsung.extend(iphones)

print(samsung)

samsung.pop()

print(samsung)

samsung.reverse()

print(samsung)