#Funkcja znajdująca dzielniki liczby
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

div_sums = []
for i in range(seek):
    div_sums.append(div_sum(i))


result = []
for n1 in range(seek):
    n2 = div_sums[n1]
    if n2 > seek:
        continue
    if div_sums[n2] == n1 and n1 != n2:
        # print(f"{n1} i {n2}")
        result.append(f"{n2} i {n1}")

# Usuwanie powtórzeń
for i in range(len(result)):
    if i % 2 == 1:
        print(result[i])

# Measure-Command {py obieralne_9.py}
# Hours             : 0
# Minutes           : 0
# Seconds           : 30
# Milliseconds      : 56
# Ticks             : 300568144
# TotalDays         : 0,000347879796296296
# TotalHours        : 0,00834911511111111
# TotalMinutes      : 0,500946906666667
# TotalSeconds      : 30,0568144
# TotalMilliseconds : 30056,8144
