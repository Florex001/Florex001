#irassuk ki a képernyőre egy ciklussal azt hogy 1234567890 5x számláló ciklussal
# for i in range(1, 51):
#     print(i % 10, end="; ")

#egy ciklussal irassuk ki az alábbi számsorozatot:0000000001111111111122222222222
# for i in range(0,51):
#     print(i // 10, end=" ")

#állítsunk elő véletlenszerüen  öt egész számot a [0,50] intervalumban és írjuk ki egymás alá az 5 számot
# import random
#
# for i in range(5):
#     print(random.randrange(0,51))


#ugyan ez csak 40db egész szám kell a [-100, 100]intervalumbol A számok egymás mellé 5 szóközre legyen kiirva
# import random
#
# for i in range(40):
#     print(random.randrange(-100 , 100),end="     ")

# for i in range(1,16):
#     for j in range(1,16):
#         print(i*j, end=" ")
#     print()



#2

for j in range(1, 50, 1):
     print("." *j)

#1
for i in range(50):
     print("." * 50)

#3
for k in range(50, 0, -1):
    print("." *k)