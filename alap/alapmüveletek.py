#1. feladat
    # számoljuk ki a kerités 45m hosszú és 35m szélességü téglalap alaku keritésy körbekeritéséhez ha 5m ert ki hagyunk?

print('2*(45+35)-5=')
print( 2*(45+35)-5)

#2 feladat:
#irassuk ki a 35 35 egyeseinek a helyén mely a 10 esek helyén található
print('az egyesek helyén lévő szám', 35 % 10)
print('a tizesek helyén lévő szám', (35-(35%10))//10)

#3 feladat
#1 feladat másképpen
hossz = 45
szel = 35
kap = 5
#print("A telek körbekerítéséhez szükséges anyag mérete", 2 * (hossz + szel) - kap, "Méter")
print("A telek körbekerítéséher szükséges anyag mérete %d méter anyag kell!" % (2 * (hossz + szel) - kap))

#értékadások
szam = 14
szam += 5;
print(szam)

#be felh0asználó név üdv felhaszn
felhasz = input('adja meg a felhasználónevet')
print("Felhasználónév", felhasz, "fasza")

#4 feladat egy program ami bekéri a kör sugarát

sugar = float(input("kérem a kör sugarát"))
kerulet = 2 * sugar * 3.14
terulet = sugar * sugar * 3.14
#print("A kör kerülete=", kerulet)
#print("A kör területe=", terulet)
print("A kör területe %.2f \n A kör kerülete %.2f"% (terulet, kerulet))

# 5 feladat


