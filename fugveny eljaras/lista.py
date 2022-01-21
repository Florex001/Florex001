# A lista névvel és sorszámmal elátott összetett típus
# A lista elemeire  a lista nevével és sorszámmal együtt hivatkozunk sorszám = index
#Lista a hónap nevei (január, február, március, április, május, június, július,augusztus, szeptember, október, november, december)
# ha honap[10] akkor novembert kapunk
# a lista mindíg 0 indexel kezdődik
# olyan adatszerkezet amely végrehajthatunk műveleteket pl.: hozzáfűzés, törlés, rendezés...stb

#lista definiálása
# lista = [] <--- üres lista
###################################################
#lista létrehozása
honap = ["január", "február", "március", "április", "május", "június", "július","augusztus", "szeptember", "október", "november", "december"]
print(honap[2]) #a lista 3. elemét írja ki

print(honap) #teljes lista
###################################################
#üres lista létrehozása ( nincsen benne elem)
nev = []
###################################################
#nev[0] = "Levente" <= listába nem lehet így elemet rakni
nev.append("Levente")
print(nev)
nev[0] = "Dávid"
print(nev)
nev.append("Levente")
print(nev)
###################################################

#40 elemű üres lista létrehozása
lista = [0] * 40
print(lista)
###################################################
# az elemek típusa eltérő lehet
lista2 = [10,   "tíz"]
print(lista2)
###################################################
#listaműveletek
tippek= [3, 12, 1, 8, 5, 8, 1, 2, 1, 4]

#nézzük meg, hogy hanyadiknak érkezett a 2 es tipp
print(tippek.index(2))

#töröljük ki a listábol a 4. és 5. tippet
del tippek[3:5]
print(tippek)

# rendezzük a tippoeket növekvő sorrendbe
tippek.sort()
print(tippek)

# lista elemsorrendjének megfordítása
tippek.reverse()
print(tippek)

# töröljük a lista 12. es értékü elemét elemét
tippek.remove(12)
print(tippek)

# lista bejárása
#amikor nem kell az index, azaz az elem értékével foglalkozunk csak
for elem in tippek:
    print(elem)



#amikor kell az index
print(len(tippek))

for i in range(7):
    print("%d. %d" % (i, tippek[i]))
