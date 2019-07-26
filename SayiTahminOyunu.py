"""
Sayi Tahmin
		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi
		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin
		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
"""
import random
print ("Lutfen Bilgisayarin tahmin etmesini istediginiz sayiyi giriniz.(0-100 arasi)")
deneme=0
tahmin = random.randint(0, 100)
buyuk_tahmin=[100]
kucuk_tahmin=[0]

while True:
    deneme = deneme + 1
    print("tahmin:", tahmin)
    print("buyuk tahmin", buyuk_tahmin, "kucuk tahmin:", kucuk_tahmin)
    yonerge=input("""Lutfen Sayinin konumunu belirten yonerge giriniz:
                     (-):Tahmin, sayidan  buyuk
                     (+):Tahmin, Sayidan Kucuk
                     (=):Tahmin dogru\n""")

    if yonerge=="=":
        print("{}.denemede Bilgisayar Sayiyi Dogru tahmin etti.".format(deneme))
        break
    elif yonerge=="-":
        buyuk_tahmin.append(tahmin)
        tahmin=random.randint(max(kucuk_tahmin)+1,min(buyuk_tahmin)-1)

    elif yonerge=="+":
        kucuk_tahmin.append(tahmin)
        tahmin = random.randint(max(kucuk_tahmin)+1,min(buyuk_tahmin)-1 )

    else:
        print("Yanlis bir secip yaptiniz.Oyun Sonlandirildi !!")
        break



