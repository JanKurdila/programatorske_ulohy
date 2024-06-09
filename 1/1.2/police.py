def sort_shelves(shelves):
   '''Zoradíme poličky zostupne'''

   shelves.sort(reverse=True)
   return shelves

def assign_shelves(shelves, technical_books, beletery):
    '''Priraďujeme poličky odborným knihám a beleterii'''

    shelves = sort_shelves(shelves)
    assignment = []
    
    for i in range(len(shelves)):
        if technical_books >= shelves[i]:
            assignment.append((shelves[i], 'Odborné_knihy'))
            technical_books -= shelves[i]
        elif beletery >= shelves[i]:
            assignment.append((shelves[i], 'Beleteria_knihy'))
            beletery -= shelves[i]
    
    if technical_books == 0 and beletery == 0:
        return assignment
    else:
        return "Knihy sa nedajú prideliť podľa podmienok zadania"

# použitie
police = [6, 5, 5, 3]
odborne_knihy = 10
beleteria_knihy = 9


pridelenie = assign_shelves(police, odborne_knihy, beleteria_knihy)
if pridelenie != "Knihy sa nedajú prideliť podľa podmienok zadania":
    print("Nájdené pridelenie je:")
    for polica, druh in pridelenie:
        print(f"Polica veľkosti: {polica}, Druh knihy: {druh}")
else:
    print(pridelenie)
