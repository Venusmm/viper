import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre= int(input("Şifreniz kaç karakter uzunluğunda olsun?"))
7

sifreniz = ""

for i in range(sifre):
    sifreniz= sifreniz + random.choice(karakterler) 


print(sifreniz)