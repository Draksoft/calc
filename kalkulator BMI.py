# -*- coding: utf-8 -*-
wzrost=input("Witaj, podaj mi swój wzrost w cm ")
waga=input("podaj mi swoją wagę w kg ")
wzrost=float(wzrost)
waga=float(waga)
wzrost=wzrost/100
BMI=waga /(wzrost**2)
print("Twoje BMI wynosi:",BMI)

