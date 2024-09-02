

# while True:
#     try:
#         number1 = float(input("Ededi daxil edin: "))
#         number2 = float(input("Ededi daxil edin: "))
#         result = number1/number2
#         print(result)
#     except ValueError:
#         print("Siz eded daxil etmelisiniz")
#     except ZeroDivisionError:
#         print("Bolen 0 a beraber ola bilmez")
#     except:
#         print("Gozlenilmeyen xeta bas verdi")
#     else:
#         print(result)

# raise ArithmeticError 
# assert 4>5

while True:
    try:
        number1 = float(input("Ededi daxil edin: "))
        number2 = float(input("Ededi daxil edin: "))
        print("1.Toplama")
        print("2.Cixma")
        print("3.Bolme")
        print("4.Vurma")
        choice = float(input("Secim eliyin: "))
        if choice==1:
            print(number1+number2)
        elif choice==2:
            print(number1-number2)
        elif choice==3:
            print(number1/number2)
        elif choice==4:
            print(number1*number2)
        else:
            raise ArithmeticError("Bele bir secim yoxdur")
        try_again = input("Tezden elemek istiyirsiz?: ")

        if try_again == "yes":
            continue
        elif try_again == "no":
            print("goodbye!")
            break
    except ValueError:
        print("Siz eded daxil etmelisiniz..")
    except ZeroDivisionError:
        print("Bolen 0 a beraber ola bilmez! ")
    except ArithmeticError:
        print("Bele bir secim yoxdur")
        break
    
    
    
    
        
    