import random

def make_dict(list1,list2): # Tworzenie słownika z dwóch list
    dict = {}
    for element in list1:
            value = list1.index(element)
            dict.update({element : list2[value]})
    return dict
    
def make_rand_dict(list1,list2): # Tworzenie słownika losowego oraz listy umożliwiającej złozenie słownika z powrotem w listę
    dict = {}
    revert_list = []
    for element in list1:
        value = list1.index(element)
        if random.choice([True,False]):
            dict.update({element : list2[value]})
            revert_list.append(1)
        else:
            dict.update({list2[value] : element})
            revert_list.append(2)
    return dict, revert_list

def dict_to_lists(dict,revert_list=None): # Tworzenie list na podstawie dziennika
    list1 = []
    list2 = []
    keys = list(dict.keys())
    values = list(dict.values())
    if revert_list == None:
        revert_list = [1] * len(dict)
    for i in range(len(revert_list)):
        if revert_list[i] == 1:
            list1.append(keys[i])
            list2.append(values[i])
        else:
            list1.append(values[i])
            list2.append(keys[i])
    return list1, list2

a = ["a", "b" ,"c"]
b = ["apple", "banana", "candy"]

if len(a) != len(b):
    print("Błąd: Listy powinny mieć taką samą długość")
else:
    mode = int(input(" 1 - Tryb scalania list\n 2 - Tryb losowego scalania list\n Wybierz tryb: "))
    if mode == 1:
        dict = make_dict(a,b)
        print(f"Słownik:\n {dict}")
        list1, list2 = dict_to_lists(dict)
        print(f"Listy złożone z powrotem:\n{list1}\n{list2}")
    elif mode == 2:
        dictionary, revert = make_rand_dict(a,b)
        print(f"Słownik:\n{dictionary}")
        list1, list2 = dict_to_lists(dictionary,revert)
        print(f"Listy złożone z powrotem:\n{list1}\n{list2}")