# brojevi = [1, 10, 7, 2, 6, 3, 17, 30]

# parni=[]
# neparni = []

# # for petlja  dal je paran ili neparan, % == 0, #append


# for broj in brojevi:
#     if broj %2 == 0:
#         print("paran broj")
#         parni.append(broj)
#     else:
#         print("nepaaran broj")
#         neparni.append(broj)

# print("parni",parni)
# print("neparni", neparni)

# rec = "anavolimilovanaa"
# pocetni_indeks = 0
# krajnji_indeks = len(rec)-1
# palindrom = True
# while pocetni_indeks < krajnji_indeks:
#     if rec[pocetni_indeks] != rec[krajnji_indeks]:
#         print("nije palindrom")
#         palindrom = False
#         break
#     pocetni_indeks += 1
#     krajnji_indeks -= 1

# else:
#     print("jeste palindrom")

# print("rec", rec, ("jeste" if palindrom else "nije"), "palindrom")


kursevi = ["python", "ios", "design"]

# unos kursa input
# provera da li postoji u listi kurevi (in)
# append
# svaki put nakon unosa ili poruke ispisati listu kurseva

zeljeni_smer = input("unesite zeljeni smer")

if zeljeni_smer in kursevi:
    print("vec postoji")
else:
    kursevi.append(zeljeni_smer)
print(kursevi)