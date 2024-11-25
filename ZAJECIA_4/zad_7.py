import sys
# Funkcja odwracająca ciąg znaków
def is_finished_by_punctuation(string):
    punctuation = [".", ",", ":", ";", "?", "!"]
    if string[-1] in punctuation:
        return True
    return False

def reverse_string(string: str):
    reversed = ""
    for character in string:
        reversed= character + reversed
    return reversed

def main():
    # Lista argumentów
    files = sys.argv[1:]
    # Lista samogłosek
    vowels = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
    vowels_upper = [vowel.upper() for vowel in vowels]
    vowels.extend(vowels_upper)

    # Sprawdzanie ilości plików
    if not files:
        sys.exit("Podaj co najmniej jeden plik")
    
    # Powtarzanie procesu dla każdego argumentu
    for filename in files:
        with open(filename, encoding="utf-8") as file:
            text = file.read()
            words = text.split()

            for i in range(len(words)):
                word = words[i]
                finish = ""
                n = -1
                # Usuwanie interpunkcji z końca słowa
                while is_finished_by_punctuation(word[n]) and word[0] in vowels:
                    finish = word[n] + finish
                    word = word[:-1]
                # Owraca słowo i je kapitalizuje, jeżeli pierwsza i ostatnia litera
                # są samogłoskami
                if word[0] in vowels and word[-1] in vowels:
                    words[i] = reverse_string(word)
                    words[i] = words[i].upper()
                # Odwraca słowo, jeżeli pierwsza litera jest samogłoską
                elif word[0] in vowels:
                    words[i] = reverse_string(word)
                words[i] = words[i] + finish
        # Nadpisanie zmian do pliku
        with open(filename, "w", encoding="utf-8") as file:
            for word in words:
                file.write(word + " ")


if __name__ == '__main__':
    main()