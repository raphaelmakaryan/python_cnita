from sympy import false


def fizzBuzz():
    # 1 a 100 | Multiple de 3 = Fizz | Multiple de 5 = Buzz | Mutiple de 3 et 5 = FizzBuzz
    for i in range(1, 100):
        if i % 3 == 0 or i == 3:
            print("Fizz")
        elif i % 5 == 0 or i == 5:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
    print("Fin de la boucle")


def leapYears(n):
    # Toute les annés sont divisible par 400 sont bissextiles | Tout annés div par 4 et pas 100 sont bissextiles
    # Toute les annés divisible par 100 mais pas 400 sont pas bixesiiles |  tout annés pas difibie par 4 sont pas bissetile
    for i in range(n):
        x = int(input("Donnez une année : "))
        if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
            print("Bissextile")
        elif (x % 100 == 0 and x % 400 != 0) or x % 4 != 0:
            print("Pas bissextile")
        else:
            print("Soucis pour l'année :", x)


def diamond():
    tableAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"]
    valuePosition = 1
    for i in range(1):
        valueUser = input("Donnez une lettre : ")
        for j in range(len(tableAlphabet)):
            if tableAlphabet[j] == valueUser:
                valuePosition = j
                break
            else:
                valuePosition = 0

        if (valuePosition != 0):
            for k in range(valuePosition + 1):
                valueTextPositif = ""
                for l in range(k + 1):
                    valueTextPositif += " " + tableAlphabet[k] + " "
                print(valueTextPositif)
            for m in range(valuePosition - 1, -1, -1):
                valueTextNegative = ""
                for n in range(m + 1):
                    valueTextNegative += " " + tableAlphabet[m]
                print(valueTextNegative)
        else:
            print(
                "La valeur définit n'existe pas ou à été mal écris, veuillez écrire une lettre de l'alphabet en MAJUSCULE")


diamond()
