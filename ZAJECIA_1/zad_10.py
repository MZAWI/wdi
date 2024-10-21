# Kalkulator prosty
import random

while True:
    n1 = float(input("Wprowadź liczbę 1: "))
    oper = input("Wprowadź operację: ")
    n2 = float(input("Wprowadź liczbę 2: "))
    if oper == "+":
        print("Wynik: ", end = "")
        print(n1 + n2)
    elif oper == "-":
        print("Wynik: ", end = "")
        print(n1 - n2)
    elif oper == "*":
        print("Wynik: ", end = "")
        print(n1 * n2)
    elif oper == "/" and n2 != 0:
        print("Wynik: ", end = "")
        print(n1 / n2)
    elif oper == "^":
        print("Wynik: ", end = "")
        print(n1 ** n2)
    elif oper == "#" and n1 >= 0 and n2 != 0:
        print("Wynik: ", end = "")
        print(n1 ** (1/n2))
    elif oper == "x":
        mini = min(n1,n2)
        maxi = max(n1,n2)
        print("Wynik: ", end = "")
        print(random.randrange(mini,maxi))
    else:
        print("Error")
    cont = input("Czy chcesz wprowadzić nowe dane? [t/n] ")
    if cont == "t":
        continue
    else:
        break