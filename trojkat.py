import math

def czyTrojkat(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("zwracam True")
        return True
    return False

def czyProstokatny(a,b,c):
    if (a ** 2 + b ** 2 == c ** 2 or
            a ** 2 + c ** 2 == b ** 2 or
            b ** 2 + c ** 2 == a ** 2):
        return True
    return False

def obwod(a, b, c):
    return a + b + c

def pole(a, b, c):
    p = 0.5 * (a + b + c)  # obliczmy współczynnik wzoru Herona
    # liczymy pole ze wzoru Herona
    P = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return P


odp = ""
while odp != "n":
    user_input = input("podaj 3 boki trojkata")
    a, b, c = map(int, user_input.split(" "))

    print("Podales boki:", a, b, c, "typ: ", type(a))

    if czyTrojkat(a, b, c):
        print("Tak, z tych bokow mozna zbudowac trojkat!")
        if czyProstokatny(a, b, c):
            print("nawet prostokatny :) ")

        print("obwod: ", obwod(a, b, c))
        print("pole: ", pole(a, b, c))
        odp = input("Chcesz sprobowac jeszcze raz? t/n")
    else:
        print("z tych bokow nie da sie zbudowac trojkata. sprobuj jeszcze raz")

print("elo!")


