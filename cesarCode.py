

# drukowane 65 - A, 90 - Z
# male      97 - a, 122 - z

def cesarCode(text, KEY):
    coded = ""
    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:       # czyli sa to duze litery
            if o > 90 - KEY:    # jesli wychodzimy poza zakres
                coded += chr(o + KEY - 26)
            else:
                coded += chr(o + KEY)

        elif 97 <= o <= 122: # male litery
            if o > 122 - KEY:
                coded += chr(o + KEY - 26)
            else:
                coded += chr(o + KEY)
        else:
            coded += chr(o)
    return coded

def decodeCesarCode(text, KEY):
    decoded = ""
    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:   # duze litery
            if o - KEY < 65:
                decoded += chr(o - KEY + 26)
            else:
                decoded += chr(o - KEY)
        elif 97 <= o <= 122:
            if o - KEY < 97:
                decoded += chr(o - KEY + 26)
            else:
                decoded += chr(o - KEY)
        else:
            decoded += chr(o)

    return decoded

plain = input("podaj tekst do zaszyfrowania: ")
coded = cesarCode(plain, 3)
print("zaszyfrowany: ", coded)
print("odszyfrowany: ", decodeCesarCode(coded, 3))
