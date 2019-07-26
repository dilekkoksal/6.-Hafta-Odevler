"""

XOX Oyunu
		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu
		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz
		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini
		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim:
					X O _
					_ X _
					_ _ _

		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O"
		koymalidir.


		Farkli bir ihtimal:
					O X X
					O _ X
					_ _ _

		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak
		oyunu bitirmelidir.
"""
import random
print("XOX oyunununa hosgeldiniz.")
tablo=[["__","__","__"],
       ["__","__","__"],
       ["__","__","__"]]
kazanma_ihtimalleri = [[[0, 0], [1, 0], [2, 0]],
                       [[0, 1], [1, 1], [2, 1]],
                       [[0, 2], [1, 2], [2, 2]],
                       [[0, 0], [0, 1], [0, 2]],
                       [[1, 0], [1, 1], [1, 2]],
                       [[2, 0], [2, 1], [2, 2]],
                       [[0, 0], [1, 1], [2, 2]],
                       [[0, 2], [1, 1], [2, 0]]]
sira=1
y_kordinat=[]
x_kordinat=[]
x=[]
o=[]

for i in tablo:
    print("\t",i,sep="\n")
while True:


    if sira%2==0:
        simge="X"#bilgisayar
    else:
        simge="O"#Kullanici
    sira+=1
    print("Simge :{}".format(simge))
    if simge == "X":
        print("Bilgisayar Oynuyor!!")
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        print("Kordinatlar", x,y)
    if simge=="O":
        x=input("Yukaridan asagiya (1,2,3):")
        y=input("Soldan saga (1,2,3):")

    x=int(x)-1
    y=int(y)-1
    if tablo[x][y]=="__":
        tablo[x][y]=simge
        if simge=="X":
            x_kordinat.append([int(x),int(y)])
        elif simge=="O":
            y_kordinat.append([int(x),int(y)])
    else:
            print("Alan doludur. Tekrar deneyiniz.")
            sira += 1
    for i in tablo:
        print("\t", i, sep="\n")
    for i in kazanma_ihtimalleri:
        a = 0
        b=0
        for j in x_kordinat:
            if j in i:
                a += 1
                if a == 3:
                    print("Bilgisayar kazandi(x)")
                    quit()

        for j in y_kordinat:
            if j in i:
                b += 1
                if b == 3:
                    print("Kazandiniz.(o)")
                    quit()



