from funocen import srednia
from funocen import drukuj
from funocen import mediana

print("Witaj w pseudo-dzienniku.")

przedmioty = set()
oceny = {}
wybor = 1
oceny['fizyka'] = [3, 4, 5, 6]
while wybor != 0:
    wybor = int(input("------------------------------------\n"
                      "Aby wyswietlic liste przedmiotow wcisnij 1\n"
                      "Aby dodac przedmiot wcisnij 2\n"
                      "Aby wyswietlic liste ocen dla danego przedmiotu wcisnij 3\n"
                      "Aby dodaj oceny dla przedmiotu wcisnij 4\n"
                      "Aby wyswietlic dane nt. ocen wcisnij 5\n"
                      "Aby wyjsc wcisnij 0\n"
                      "------------------------------------\n"))
    if wybor == 1:
        drukuj(przedmioty, "Lista dodanych przedmiotow: ")

    if wybor == 2:
        nazwaPrzedmiotu = input("Podaj nazwe przedmiotu do dodania: ")
        przedmioty.add(nazwaPrzedmiotu)
        oceny[nazwaPrzedmiotu] = []
        print("dodano przedmiot: ", nazwaPrzedmiotu)

    if wybor == 3:
        nazwaPrzedmiotu = input("Podaj nazwe przedmiotu ktorego oceny chcesz sprawdzic: ")
        drukuj(oceny[nazwaPrzedmiotu], "Oceny dla: " + nazwaPrzedmiotu)

    if wybor == 4:
        nazwaPrzedmiotu = input("Podaj nazwe przedmiotu do ktorego oceny chcesz dodac: ")
        listaOcen = str(input("Podaj oceny oddzielone spacja: "))
        listaOcen = listaOcen.split(" ")
        listaOcen = [*map(int, listaOcen)]
        print("type oceny: %s type lista ocen: %s" % (type(oceny[nazwaPrzedmiotu]), type(listaOcen )))
        print("lista ocen: ", type(listaOcen[0]) )
        oceny[nazwaPrzedmiotu] += listaOcen
        drukuj(oceny[nazwaPrzedmiotu], "Oceny z przedmiotu: " + nazwaPrzedmiotu)

    if wybor == 5:
        nazwaPrzedmiotu = input("Podaj nazwe przedmiotu ktorego dane ocen chcesz sprawdzic: ")
        print(srednia(oceny[nazwaPrzedmiotu]))
        print(mediana(oceny[nazwaPrzedmiotu]))