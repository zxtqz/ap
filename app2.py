# # size = int(input("Kvadratin terefini daxil edin: "))

# # for row in range(1,size+1): # 0 1 2 3 4
# #     for j in range(row): #0 1 2 3 4
# #         print("*",end=" ")
# #     print()


# # length = int(input("Uzunluqu daxil edin: "))
# # width = int(input("bucagin enin daxil edin: "))

# # for row in range(size,0):
# #     for j in range(size-row):
# #         print("*",end=" ")
# #     print()
# # size = int(input("Kvadratin terefini daxil edin: "))
# # for row in range(1,size+1):
# #     for col in range(1,size+1):
# #         if row==col or row==size or col==1:
# #             print("*",end="")
# #         else:
# #             print(end="")
# #     print()

# # size = int(input("Kvadratin terefini daxil edin: "))
# # width = int(input("daxil ed: "))

# # for row in range(size):
# #     for col in range(width):
# #         if row==0 or row==size-1 or col==0 or col==width-1:
# #             print("*",end="")
# #         else:
# #             print(end=" ")
# #     print()

# # size = int(input("Kvadratin terefini daxil edin: "))

# # for row in range(1,size+1): # 0 1 2 3 4
# #     for col in range(row): #0 1 2 3 4
# #         if row==0 or row==size or col==0 or col==size:
# #             print("*",end=" ")
# #     print()

# # number = int(input("Eded daxil edin: "))
# # numberstr = str(number)
# # uzunluq = len(numberstr)
# # print(uzunluq)
# # print("secim edin: ")
# # print("1. Reqemin sayin tapmaq")
# # print("2. sifirlarin sayini teyin etsin")
# # print("3.Ededin oratasin tapmaq")



# # cemini= number+uzunluq
# # print(cemini)

# # size = int(input("Kvadratin terefini daxil edin: "))

# for row in range(1,size+1): # 0 1 2 3 4
#     for col in range(1,size+1):  #0 1 2 3 4
#         for i in range(size):
#             print("*",end="")
#         for j in range(size):
#             print("_",end="")
#     print()

# import random

# print("Seviyye Secin:")
# print("1.Asan")
# print("2.Normal")
# print("3. Cetin")
# randomvuruq = random.randint(1,4)
# randomvuruq2 = random.randint(4,7)
# randomvuruq3 = random.randint(1,15)
# choice = int(input("Yuxarlardan birin secin: "))



# if choice==1:
#     print(randomvuruq,"*",randomvuruq)
# elif choice==2:
#     print(randomvuruq2,"*",randomvuruq2)
# elif choice==3:
#     print(randomvuruq3,"*",randomvuruq3)
# else:
#     print("bele bir secim yoxdur")

# answer = int(input("Cavab verin: "))