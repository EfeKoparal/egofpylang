import random
import time

print("""

sayi tahmin oyunu

1 ile 40 arasinda sayi tahmin edin...

""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:
    tahmin = int(input("Tahmininiz: "))

    if tahmin < rastgele_sayi :
        print("Bilgiler sorgulaniyor...")
        time.sleep(1)
        print("Daha yuksek bir sayi soyleyin...")
        tahmin_hakki -=1
    elif tahmin > rastgele_sayi:
        print("Bilgiler sorgulaniyor...")
        time.sleep(1)
        print("Daha dusuk bir sayi soyleyin...")
        tahmin_hakki -= 1
    else:
        print("Bilgiler sorgulaniyor...")
        time.sleep(1)
        print("bildiniz tebrikler aminyum...", rastgele_sayi)
    if tahmin_hakki == 0:
        print("bundan sonra bilmenin anlami yok zaten siktir git")
        break
