pin = 1234
bal = 1000

while True:
    # Lista operacji
    print("Witaj! Wybierz operację!") 
    print("[1] Wpłać pieniądze")
    print("[2] Wypłać pieniądze")
    print("[3] Sprawdź balans konta")
    print("[4] Wyjdź")
    try: # Sprawdzenie czy podana liczba spełnia kryteria
        operation = int(input("Podaj typ operacji (1-4): ")) # Wybór operacji
        if operation < 1 or operation > 4:
            print("Nieprawidłowa operacja")
            continue
    except:
        print("Nieprawidłowa operacja")
        continue

    pin_in = int(input("Wprowadź pin: ")) # Sprawdzenie pinu
    if pin_in != pin:
        print("Nieprawidłowy pin!")
        continue
    
    if operation == 1: # Wpłata pieniędzy
        deposit = int(input("Wybierz kwotę, jaką chcesz wpłacić: "))
        bal += deposit
        print(f"Wpłacono {deposit}zł")
    elif operation == 2: # Wypłata pieniędzy
        withdraw = int(input("Wybierz kwotę, jaką chcesz wpłacić: "))
        if withdraw > bal: # Sprawdzenie, czy na koncie jest wystarczająca kwota
            print("Niewystarczająco środków na koncie!")
        else:
            bal -= withdraw
            print(f"Wypłacono {withdraw}zł.")
    elif operation == 3: # Wyświetlenie balansu konta
        print(f"Twój balans wynosi: {bal}")
    else: break
    print("Co chcesz zrobić w kolejnym kroku?") # Pytanie o kontynuację
    print("[1] Kontynuacja")
    print("[2] Wyjście")
    cont = input("Wybór: ")
    if cont == "1":
        continue
    else: break