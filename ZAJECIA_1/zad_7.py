# Należy wypisać liczby z zakresu przedstawionego przez użytkownika.
print("Podaj dwie liczby całkowite")
n1 = int(input("Liczba 1: "))
n2 = int(input("Liczba 2: "))

# Znalezienie większej i mniejszej liczby
maxi = max(n1,n2)
mini = min(n1,n2)

# Wypisanie liczb z zakresu (z wykorzystaniem różnych pętli)
if maxi-mini+1 > 20:
    avg = int((mini+maxi)/2)
    for i in range(avg-2,avg+4):
        print(i)
else:
    i = mini
    while i <= maxi:
        print(i)
        i += 1