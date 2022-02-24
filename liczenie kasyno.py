import numpy
#wynik z dnia 26-01-2022
tablica_kazdej_liczby=numpy.zeros((51,), dtype=int)
ile_bylo_losowan=0
f = open("zapis_losowan.txt", "r")
#print(f.read())
zapis_pliku=f.read().replace("[","").replace("]","").replace("\n","")

for i in range(51):
    tablica_kazdej_liczby[i]=int(zapis_pliku.split(" ")[i])
print(tablica_kazdej_liczby)
ile_bylo_losowan=tablica_kazdej_liczby[50]
wynik = input("Podaj obecny wynik:")

#1 16 23 27 40 49
tablica_kazdej_liczby[int(wynik.split(" ")[0])]=tablica_kazdej_liczby[int(wynik.split(" ")[0])]+1
tablica_kazdej_liczby[int(wynik.split(" ")[1])]=tablica_kazdej_liczby[int(wynik.split(" ")[1])]+1
tablica_kazdej_liczby[int(wynik.split(" ")[2])]=tablica_kazdej_liczby[int(wynik.split(" ")[2])]+1
tablica_kazdej_liczby[int(wynik.split(" ")[3])]=tablica_kazdej_liczby[int(wynik.split(" ")[3])]+1
tablica_kazdej_liczby[int(wynik.split(" ")[4])]=tablica_kazdej_liczby[int(wynik.split(" ")[4])]+1
tablica_kazdej_liczby[int(wynik.split(" ")[5])]=tablica_kazdej_liczby[int(wynik.split(" ")[5])]+1
ile_bylo_losowan=ile_bylo_losowan+1
tablica_kazdej_liczby[50]=ile_bylo_losowan
#ile jakich liczb:
#print(tablica_kazdej_liczby[1]/tablica_kazdej_liczby[50])
for i in range(50):
    print("Szansa na liczbę"+str(i)+":"+str((tablica_kazdej_liczby[i]/tablica_kazdej_liczby[50])* 100))
f = open("zapis_losowan.txt", "w")
f.write(str(tablica_kazdej_liczby).replace("[ 0","[0").replace("  "," "))
f.close()