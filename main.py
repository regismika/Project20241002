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
from operator import truth, truediv
from turtledemo.penrose import start

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

# print("Iveskite savo varda")
# vardas = input()
# for v in vardas:
#     print(f'labas {vardas}')

# Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai

# for elementas in [88, 65, 21, 26, 47, 14]:
#     if elementas % 2 == 0:
#         print(elementas)

# Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. Taip pat, kokius
# skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius)

# 15. Raskite visų skaičių nuo 1 iki 100 sumą.
# totalsum = 0
# for i in range (1, 101):
#     totalsum += i
#     print(f' Galutine suma: {totalsum}')

# 16.Raskite visų lyginių skaičių nuo 20 iki 50 sumą.
# 17.Raskite visų nelyginių skaičių nuo 30 iki 60 sumą


# 1. Išveskite visus skaičius nuo 1 iki 20.
# skaicius = 1
# while skaicius < 21:
#     print(skaicius)
#     skaicius += 1

# 2. Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".
# skaicius = 0
# while skaicius < 50:
#     skaicius += 1
#     if skaicius % 2 == 0:
#         print(skaicius, "lyginis")
#     else:
#         print(skaicius, "nelyginis")

# 3. Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# išveskite tekstą "dalinasi iš 3".

# for i in range(25, 51):
#     if i % 3 == 0:
#         print("dalinasi is 3")
#     else:
#         print(i)

# 4. Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris
# dalinasi iš 7.
# i = 1
# while i <= 100:
#     if i % 7 == 0:
#         break
#     i += 1
# print(i)

# 5. Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris dalinasi iš 3 ir iš 5.
# i = 1
# while i < 100:
#     if i % 3 == 0 and i % 5 == 0:
#         break
#     i += 1
# print(i)

# 6.Vartotojas turi suvesti rėžių pradžią ir pabaigą. Tačiau jūs turite patikrinti ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). Liepkite
# vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. Turint tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus išvedant jo kvadratą, bei ar jis lyginis/nelyginis.

# while True:
#       print("Iveskite pirmaji skaiciu")
#       skaicius1 = int(input())
#       print("Iveskite antraji skaiciu didesni uz pirmaji skaiciu")
#       skaicius2 = int(input())
#       if skaicius1 < skaicius2:
#           for skaicius in range(skaicius1, skaicius2):
#              if (skaicius * skaicius) % 2 == 0:
#                  print(f'{skaicius}  {(skaicius * skaicius)} lyginis')
#              else:
#                  print(f'{skaicius}  {(skaicius * skaicius)} nelyginis')
#           break
#       else:
#          print("Neteisingai. Skaityk salyga. Prasau")


# 7. Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir yra
# didesnis nei 20.

# print("Pirminis skaicius didesnis uz 20:")
# for sk in range(1, 30 + 1):
#      if sk > 1:
#        for i in range(2, sk):
#            if sk % i == 0:
#                break
#        else:
#            if sk > 20:
#             print(sk)
#             break

# 8. Liepkite vartotojui įvedinėti bet kokius skaičius. Vykdykite įvedinėjimą iki
# kol įvestas skaičius bus lygus 0. Raskite įvestų skaičių sumą.

# Skaiciai = []
# print("Iveskite skaiciu")
# while True:
#     Skaicius = int(input())
#     if Skaicius != 0:
#         print("Iveskite skaiciu")
#     if Skaicius == 0:
#         break
#     Skaiciai.append(Skaicius)
# suma = sum(Skaiciai)
# print(f'Skaiciu suma: {suma}')

# 9. Leiskite vartotojui atlikti norimus skaičiavimus tiek kartų kiek jis nori.
# Pavyzdžiui, leiskite vartotojui įvesti du skaičius, tuomet jam parodykite
# pačius skaičius, veiksmus (sudėtis, atimtis, daugyba, dalyba) ir
# suskaičiuotus atsakymus (5 + 3 = 8; 5 - 3 = 2; ...). Kai atsakymai bus
# parodyti, vartotojas turi turėti galimybę pakartoti skaičiavimus, todėl
# leiskite pasirinkti ar dar kartoti veiksmą, ar jau programa turėtų baigti
# savo darbą.

# This function adds two numbers
# def add(x, y):
#     return x + y
#
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#    choice = input("Enter choice(1/2/3/4): ")
#    if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break
#     else:
#         print("Invalid Input")

# 10.Vartotojui išveskite pasirinkto skaičiaus daugybos lentelę (pvz, skaičiaus 5
# daugybos lentelė būtų 5 * 1 = 5; 5 * 2 = 10; 5 * 3 = 15; ...). Leiskite
# vartotojui kartoti veiksmą (tiek kartų kiek norės) ir gauti dar vieną
# daugybos lentelę su kitu pasirinktu skaičiumi.
# while True:
#     print("Iveskite skaiciu")
#     skaicius = int(input())
#     for i in range(1, 11):
#         print(skaicius, 'x', i, '=', skaicius*i)
#     kitas_bandymas = input("Ar norite pakartoti? (taip?ne): ")
#     if kitas_bandymas == "ne":
#         break
#     elif kitas_bandymas == "taip":
#         print("Veskite kita skaiciu")
#     else:
#         print("Programos pabaiga")
#         break
#
# 12.Sukurkite studentų pažymių vidurkių skaičiuoklę (kaip pavyzdį galite
# naudoti 17-ą pavyzdį). Tačiau tokia skaičiuoklė turėtų leisti skaičiuoti
# vidurkį ne tik iš vieno studento pažymių, bet leistų pakartoti pažymių
# įvedimą ir vidurkio skaičiavimą ant tiek studentų kiek reikia.



# 13.Sukurkite skaičiaus atspėjimo užduotį. Leiskite vartotojui pasirinkti
# žaidimo sudėtingumą (atsitiktinio skaičiaus rėžiai), ar suteikiamos
# pagalbos (skaičius mažesnis/didesnis nei spėjamas), kiek spėjimų
# leidžiama (neribotai, arba pvz iki 10 ėjimų), bei kiti pasirinkti parametrai.
# Vartotojas šiuos parametrus pasirenka žaidimo pradžioje. Turite užtikrinti,
# kad vartotojas pasirinko parametrus tik iš galimų - jeigu ne, liepkite
# įvedimą pakartoti
