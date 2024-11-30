# Funkcja generująca macierz o wymiarach 2n-1 x 2n-1
def make_zero_matrix(n: int):
    if n < 1:
        raise ValueError("Size n must be greater than 0")
    size = 2 * n - 1
    matrix = []
    row = size * [0] # Tworzy rząd macierzy
    for _ in range(size):
        matrix.append(row.copy())
    return matrix 

# Funkcja wyświetlająca macierz
def print_matrix(matrix):
    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()

# Funkcja tworząca obramowanie w macierzy
def frame_matrix(matrix: list, integer: int = 1):
    size = len(matrix)
    for row in matrix:
        row[0] = integer
        row[-1] = integer
    for number in range(size):
        matrix[0][number] = integer
        matrix[-1][number] = integer
    return matrix

# Funkcja tworząca naprzemienne obramowanie w macierzy
def changing_frame_matrix(matrix: list, integer1: int = 1, integer2: int = 2):
    size = len(matrix)
    for i in range(size):
        # Zmiana wartości dla górnej i dolnej ramki
        matrix[0][i] = integer1 if i % 2 == 0 else integer2
        matrix[size-1][i] = integer1 if i % 2 == 0 else integer2

        # Zmiana wartości dla ramek bocznych
        matrix[i][0] = integer1 if i % 2 == 0 else integer2
        matrix[i][-1] = integer1 if i % 2 == 1 else integer2
    return matrix

# Funkcja tworząca przekątną na macierzy
def diagonal_matrix(matrix: list, mode: int = 0, diagonal: int = 1):
    if mode < 0 or mode > 2:
        raise ValueError("You must specify mode of either 0 or 2")
    size = len(matrix)
    if mode == 0:
        for number in range(size):
            matrix[number][number] = diagonal
    elif mode == 1:
        for number in range(size):
            matrix[number][size-(number+1)] = diagonal
    else:
        for number in range(size):
            matrix[number][number] = diagonal
            matrix[number][size-(number+1)] = diagonal
    return matrix


zero_matrix = make_zero_matrix(3)
# print_matrix(zero_matrix)
# print_matrix(frame_matrix(zero_matrix))
# print_matrix(diagonal_matrix(zero_matrix,2))
# print_matrix(changing_frame_matrix(zero_matrix))
    
