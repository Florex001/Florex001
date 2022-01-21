import math
bea = float(input("adja meg a-t"))
bem = float(input("adja meg m t"))
mo = math.sqrt(math.pow(bem, 2) + math.pow((bea//2), 2))
a = math.pow(bea, 2) + 4 * ((bea-mo)//2)
v = math.pow(bea, 2) * mo // 3
print("felszín: %d térfogat: %d " % (a, v))



