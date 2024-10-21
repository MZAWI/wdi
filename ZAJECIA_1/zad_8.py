# Rysunek choinki

height = int(input("Podaj wysokość: "))
bombka = "*o"

# Główna pętla
for i in range(0,height):
    # Obliczanie ile wypisać spacji i bombek/igieł
    space = height - (i+1)
    print(" " * space, end = "")
    width = (height - space + i)

    # Wpisywanie igieł/bombek na choince
    while width > 0:
        if width % 4 == 3:
            print("o", end="")
        else:
            print("*", end="")
        width -= 1
    # Rozpoczęcie kolejnego etapu pętli nową linią
    print()

# Pień
print(" " * (height-1) + "U")
