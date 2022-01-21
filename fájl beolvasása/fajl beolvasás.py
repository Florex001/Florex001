class dolgozo():
    pass

dolgozok = []

fajl = open("berek.txt", "r", encoding="UTF-8")

fajl.readline()

sor = fajl.readline()
while sor != "":
    sor = sor.strip()
    adatok = sor.split(";")
    seged = dolgozo()
    seged.nev = adatok[0]
    seged.neme = adatok[1]
    seged.reszleg = adatok[2]
    seged.belepesEve = int(adatok[3])
    seged.ber = int(adatok[4])
    dolgozok.append(seged)
    sor = fajl.readline()

fajl.close()

def egyfeladat():
    print("3.feladat: Dolgozók száma: %d" % len(dolgozok))

egyfeladat()

