#   BEZ ZMIENNYCH
# Wypisać swoje imię, nazwisko, wiek, ulubioną potrawę, ulubione zwierzę, wynik dzielenia 5 przez 7.
# Używając funkcji służącej do wysyłania danych na standardowe wyjście (kilka wywołań).
print("Imię: Mateusz")
print("Nazwisko: Zawieracz")
print("Wiek: 20")
print("Ulubiona potrawa: zupka chińska")
print("Ulubione zwierzę: kot")
print("5/7 =", round(5/7,2))
print("")

# Używając funkcji służącej do wysyłania danych na standardowe wyjście (jedno wywołanie).
print("Imię: Mateusz \nNazwisko: Zawieracz\nWiek: 20\nUlubiona potrawa: zupka chińska\nUlubione zwierzę: kot\n5/7 =", round(5/7,2))

# Wynik dzielenia należy wypisać z dokładnością do 1, 3, 5 i 10 cyfr po przecinku.
print("5/7 =", round(5/7,1))
print("5/7 =", round(5/7,3))
print("5/7 =", round(5/7,5))
print("5/7 =", round(5/7,10))

#   TO SAMO ZE ZMIENNYMI
name = "Mateusz"
sname = "Zawieracz"
age = 20
food = "zupka chińska"
pet = "cat"
wynik_dziel = 5/7
print("Imię", name)
print("Naziwsko", sname)
print("Wiek:", age)
print("Ulubiona potrawa:", food)
print("Ulubione zwierzę:", pet)
print("5/7 =", wynik_dziel)

print("5,7 =", round(wynik_dziel,1))
print("5,7 =", round(wynik_dziel,3))
print("5,7 =", round(wynik_dziel,5))
print("5,7 =", round(wynik_dziel,7))