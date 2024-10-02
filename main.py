# text = "labas"
# number = 46
# #          0 1 2
# numbers = [1,5,10]
# print(numbers)
# print(numbers[0])
# numbers[0] = 7
# print(numbers[0])
# print(numbers)
# print(len(text)) #labas
# print(len(numbers)) # skaiciu masyvo ilgis
# numbers.append(20)
# print(numbers)
# numbers.insert(0,40)
# print(numbers)
# numbers.extend([5,6,7])
# print(numbers)
#
# names = [
#     "Jonas",
#     "Petras",
#     "Antanas"
# ]
# print(names)
# names.pop()
# print(names)
# # names.clear()
# # print(names)
# print(names.index("Jonas"))
# print("Antanas" in names)
# print("Jonas" in names)
# print(numbers.count(5))
#
# print(sorted(numbers))
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers[:5])
# print(numbers[5:])
# print(numbers[1:5])
# print(numbers[:-1])
# print(numbers[0:8:2])#viskas kas antra elementa
# print(numbers[::2])#viskas kas antra elementa
#
# mixedList = ["miau", 20, True, "bugatti", "70", 4]
# print(mixedList)
#
# Joana = ["Joana", "Marceliute", 29, False, "jm@gmail.com", 1.65]
# Virgis = ["Virgis", "Noreika", 48, True, "vn@yahoo.com", 1.75]
#
# zmones = [
#     Joana,
#     Virgis,
#     ["Virgis1", "Noreika", 48, True, "vn@yahoo.com", 1.75],
#     ["Virgis2", "Noreika", 48, True, "vn@yahoo.com", 1.75],
#     ["Virgis3", "Noreika", 48, True, "vn@yahoo.com", 1.75]
# ]
#
# print(zmones[4][0])
# zmones.pop(4)
# print(zmones)
# print(list(range(0,2)))
# print(list(range(0,100,7)))
# print(len(list(range(0,100,7))))
from itertools import count

# Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.
# vardai = ["Mantas", "Petras", "Maryte", "Pranyte"]
# print(vardai)
# vardai[0] = "Tadas"
# vardai[3] = "Rasa"
# # pridedu varda
# vardai.append("Matas")
# print(vardai)
# print(vardai[3])
# print(len(vardai))

# Susikurkite list žmonių ūgiams saugoti ir užpildykite jį informacija. Išveskite viso šio list duomenis bei kiek ūgių turite.

# ugiai = [172, 185, 200, 169, 170]
# print(ugiai)
# ugiai.append(188)
# print(ugiai)
# print(len(ugiai))
# print(ugiai [0 : -2])

# Susikurkite list pažymiams saugoti.
# Pamėginkite sukurti programą, kur vartotojas galėtų suvesti norimą kiekį naujų duomenų.
# Galiausiai išveskite visus pažymius ir jų kiekį.

# pazymiai = []
# 1 variantas
# print("Iveskite pazymi")
# nauji_pazimiai = int(input())
# pazymiai.append(nauji_pazimiai)
# print("Iveskite pazymi")
# nauji_pazimiai = int(input())
# pazymiai.append(nauji_pazimiai)
# print("Iveskite pazymi")
# nauji_pazimiai = int(input())
# pazymiai.append(nauji_pazimiai)
# print(f'Visi pazymiai: {pazymiai}'
# print("Iveskite pazymi")
# 2 variantas
# print("Iveskite pazymius")
# nauji_pazimiai = input().split(",")
# print(nauji_pazimiai)
# print(len(nauji_pazimiai))

# Susikurkite miestų sąrašą.
# Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list.
# Išveskite tiek pradinį list, tiek papildytą duomenimis.
# Pamėginkite papildyti programą, kad vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas

# miestai = ["Joniskis", "Naujoji Akmene", "Kazlu Ruda", "Rokiskis"]
# print(miestai)
# print("Iveskite miesta:")
# naujas_miestas = input().split(",")
# print("Pasirinkite miesto vieta sarase")
# mieto_vieta_sarase = int(input())
# miestai.append(naujas_miestas, [reikia iterpti naujo miesto vieta sarase])
# print(f'Atnaujintas miestu sarasas: {miestai}')

# Su for pagalba penkis kartus išveskite savo vardą
# for sk in range(5):
#  print("Regis")

# Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.
# for i in range(11):
#  print(i)

# Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15
# for i in range(0, 16, 2):
#     print(i)

# Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
# for i in range(1, 20, 3):
#     print(i)

# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7].
# for el in [7, 4, 5, 32, 14, 78]:
#  print([el])

# Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.
# for i in range(1, 21):
#         if i % 4 ==0:
#             print(f'skaicius {i} dalinasi is 4')

# Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis ar nelyginis skaičius. Pvz:
# 1 nelyginis
# 2 lyginis
# 3 nelyginis
# for i in range(1, 16):
#     if i % 2 == 0:
#         print(f'skaicius {i} lyginis')
#     elif i % 2 != 0:
#             print(f'skaicius {i} nelyginis')

# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite, kad tai būtų validu (pradžia
# turi būti mažesnė nei pabaiga). Jei rėžiai tinkami, tuomet vykdyti for, kuris atskirose eilutėse
# išvestų kiekvieną skaičių iš tų rėžių, bei atskiriant tarpu - tų skaičių kvadratus
# start = 1
# end = 15
# if start < end:
#     for skaicius in range(start, end):
#         print(str(skaicius) + " " + str(skaicius * skaicius))
# else:
#     print("Belekas")

# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius
# skaičius arba tuos, kurie dalinasi iš 8

# start = 1
# end = 15
# if start < end:
#     for skaicius in range(start, end):
#        if skaicius % 2 != 0 or skaicius % 8 == 0:
#         print(skaicius)

# Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).

print("Iveskite savo varda")
vardas = input()
for v in vardas:
    print(f'labas {vardas}')

# Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai
# KLAUSTI
for elementas in [88, 65, 21, 26, 47]:
    if elementas % 2 == 0:
        print(elementas)

# Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. Taip pat, kokius
# skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius)

