import json
import sys

list_sys = [i[:-1] for i in sys.stdin]
nice_list = []
argentina_dict = {}
chile_dict = {}
qwerty = {"argentina": argentina_dict,
          "chile": chile_dict}

for i in list_sys:
    nice_list.append(i.split('#'))

for i in nice_list:
    print(i)
    if i[0] == 'A':
        argentina_dict.setdefault(i[1])
    elif i[0] == 'Ch':
        chile_dict.setdefault(i[1])

plants_Ch = []
animals_Ch = []

plants_A = []
animals_A = []

a = qwerty["chile"].keys()

for i in a:
    for j in nice_list:
        if j[0] == 'Ch':
            if j[1] == i:
                if j[2] == 'animal':
                    animals_Ch.append(j[3])
                else:
                    plants_Ch.append(j[3])
    chile_dict.update({i: sorted(animals_Ch) + sorted(plants_Ch)})
    animals_Ch = []
    plants_Ch = []


a = qwerty["argentina"].keys()
for i in a:
    for j in nice_list:
        if j[0] == 'A':
            if j[1] == i:
                if j[2] == 'animal':
                    animals_A.append(j[3])
                else:
                    plants_A.append(j[3])
    argentina_dict.update({i: sorted(animals_A) + sorted(plants_A)})
    animals_A = []
    plants_A = []



with open("patagonia.json", "w", encoding="utf-8") as file:
    json.dump(qwerty, file)