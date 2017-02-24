# ZADANIE: Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym w formacie: “mała => duża litera”.
# W jednym wierszu trzeba wydrukować po pięć takich grup.

ileLinii = int(input("Podaj co ile linii ma byc przerwa"))

counter = 0
for i in range(65, 91):
    char = chr(i)
    print("%s => %s " % (char, char.lower()))
    counter += 1
    if counter == ileLinii:
        print("")
        counter = 0


print("\nAlfabet w porządku odwróconym:")
counter = 0
for i in range(122, 96, -1):
    char = chr(i)
    print("%s => %s " % (char, char.upper()))
    counter += 1
    if counter == ileLinii:
        print("")
        counter = 0


