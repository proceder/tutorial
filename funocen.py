import math
def srednia(oceny):
    for i in oceny:
        print("typ: ", type(i))
    suma = sum(oceny)
    return suma / float(len(oceny))


def drukuj(type, description):
    print(description)
    if len(type) > 0:
        for i in type:
            print(i)
    else:
        print("Brak elementow")


def mediana(oceny):
    oceny = sorted(oceny)
    dlugosc = len(oceny)
    half = int(len(oceny)/2)
    print("dlugosc: ", dlugosc)
    if dlugosc%2 != 0:  #nieparzyste
        return oceny[half]
    else:   #parzysta
        return (oceny[half-1] + oceny[half]) / 2

