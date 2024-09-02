# OOP = OBJECT Orineted Programming - OYP - Obyek Yonlumu Proqramlasdirma
# OYP = Object Yonumlu Proqramlasidrma
# Real heyatdaki herseye object kimi gorerek proqramimiza daxil etmeye deyilir
#Property - Ozellik - Xususiyyet
# Method - Obyektin bacariqlaridir / funksionalligidir

# Class - class keywordu vasitesi ile yaradilir Obyektlerin
# Shemasini - bildirir

# self - oldugu objecti isae edir
# __init__ - initialize - obyekt  yarandigi zaman ilk isleyen methoddur

# class Mouse:
#     def __init__(self,brand):
#         print("Mouse classindan obyekt yarandi")
#         self.brand = brand

#     def onrightClick(self):
#         print("Mousein sag duymesi klik edildi")

#     # pass # Classin bos oldugunu bildirir

# # Classdan objectin yaradilmasi bildirir
# mymouse = Mouse("HyperX")

# mymouse.brand= "Logitech"

# # s = "Salam"
# # s.replace("s","a")

# mymouse.onrightClick()

# print(mymouse.brand)

class Car:
    def __init__(self,brand,color,engine,year,price):
        print("Masiniviz yaradildi: ")
        self.color = color
        self.brand = brand
        self.engine = engine
        self.year = year
        self.price = price

    def onignition(self):
        print("Masin xodandi: ")

    def onbreak(self):
        print("Masini tormuznan diyandirdiz")

mycar = Car("M5","Dark Blue","V8 Twin-Turbo",2018,"$95,000")

mycar.brand = "BMW M5"

mycar.onignition()


print(mycar.brand)
print(mycar.color)
print(mycar.engine)
print(mycar.year)
print(mycar.price)

