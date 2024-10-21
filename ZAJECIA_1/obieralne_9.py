# Funkcja znajdująca dzielniki liczby
def div_sum(number):
    div = [1] 
    mid = int(number**(1/2)) + 1
    for n1 in range(2, mid):
        if number % n1 == 0:
            div.append(n1)
            n2 = number // n1
            if n2 != n1:
                div.append(n2)
    return sum(div)

seek = 10**6 # liczba do której szukamy zaprzyjaźnionych

result = []
for n1 in range(seek):
    n2 = div_sum(n1)
    if div_sum(n2) == n1 and n1 != n2:
        # print(f"{n1} i {n2}")
        result.append(f"{n1} i {n2}")

# Usuwanie powtórzeń
for i in range(len(result)):
    if i % 2 == 0:
        print(result[i])