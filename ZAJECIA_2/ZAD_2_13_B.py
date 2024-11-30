import random

def make_dict(keys,values): # Tworzenie słownika z dwóch list
    return dict(zip(keys,values))
    
def make_rand_dict(list1,list2): # Tworzenie słownika losowego 
    dictionary = {}
    for i in range(len(list1)):
        if random.choice([True,False]):
            dictionary[keys[i]] = values[i]
        else:
            dictionary[values[i]] = keys[i]
    return dictionary

def dict_to_lists(dict): # Tworzenie list na podstawie dziennika
    keys = list(dict.keys())
    values = list(dict.values())
    return keys, values


keys = ["a", "b" ,"c", "d"]
values = ["apple", "banana", "cherry", "dinosaur"]

if len(keys) != len(values):
    print("Błąd: Listy powinny mieć taką samą długość")
else:
    mode = int(input(" 1 - Tryb scalania list\n 2 - Tryb losowego scalania list\nWybierz tryb: "))
    if mode == 1:
        dictionary = make_dict(keys, values)
    elif mode == 2:
        dictionary = make_rand_dict(keys, values)
        
    print(f"Słownik: {dictionary}\n")
    list1, list2 = dict_to_lists(dictionary)

    print("Klucze: ", list1)
    print("Watości: ", list2)

