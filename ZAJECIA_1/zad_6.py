""" Pobrać od użytkownika 2 liczby a następnie obliczyć ich:
    sumę, różnicę, iloczyn, iloraz, kwadrat (obu liczb)
    oraz pierwiastek drugiego stopnia (obu liczb). """

# Wprowadzenie zmiennych
yay = ""
n1 = float(input("Podaj liczbę 1: "))
n2 = float(input("Podaj liczbę 2: "))

# Sprawdzenie czy OBIE liczby są mniejsze niż zero bądź czy druga liczba jest równa zeru. 
# Jeśli tak - wyłączzenie programu
if (n1 < 0 and n2 < 0) or n2 == 0:
    print("Liczby mniejsze niż zero / dzielenie przez 0")
    exit()
# Sprawdzenie, czy tylko JEDNA liczba jest mniejsza niż 0, przekształcenie ją na wartość bezwzględną
elif (n1 < 0) ^ (n2 < 0):
    if n1 < 0:
        n1 = -n1
    else:
        n2 = -n2
# DZIAŁANIA
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
# Dopisanie "Yay!", gdy iloczyn n1 i n2 jest równy 10
if n1 * n2 == 10:
    yay = "Yay!"
print(f"{n1} * {n2} = {n1*n2} " + yay)
print(f"{n1} / {n2} = {round(n1/n2,2)}")
print(f"{n1}^2 = {n1**2}")
print(f"{n2}^2 = {n2**2}")
print(f"sqrt({n1}) = {round(n1**(1/2),2)}")
print(f"sqrt({n2}) = {round(n2**(1/2),2)}")

