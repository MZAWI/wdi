import random

def make_dict(list1,list2): # Tworzenie słownika z dwóch list
    dict = {}
    for element in list1:
            value = list1.index(element)
            dict.update({element : list2[value]})
    return dict
    
def make_rand_dict(list1,list2): # Tworzenie słownika losowego oraz listy umożliwiającej złozenie słownika z powrotem w listę
    dict = {}
    for element in list1:
        index = list1.index(element)
        if random.choice([True,False]):
            dict.update({element : list2[index]})
        else:
            dict.update({list2[index] : element})
    return dict

def dict_to_lists(dict): # Tworzenie list na podstawie dziennika
    list1 = list(dict.keys())
    list2 = list(dict.values())
    return list1, list2


a = ["a", "b" ,"c"]
b = ["apple", "banana", "cherry"]

if len(a) != len(b):
    print("Błąd: Listy powinny mieć taką samą długość")
else:
    mode = int(input(" 1 - Tryb scalania list\n 2 - Tryb losowego scalania list\n Wybierz tryb: "))
    if mode == 1:
        dictionary = make_dict(a,b)
    elif mode == 2:
        dictionary = make_rand_dict(a,b)
        print(dictionary)
        
    print(f"Słownik:\n{dictionary}\n")
    list1, list2 = dict_to_lists(dictionary)
    print("Listy:")
    print(list1)
    print(list2)

