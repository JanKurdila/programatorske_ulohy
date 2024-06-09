def sort_shelves(police):
    '''Zoradíme poličky zostupne'''
    police.sort(reverse=True)
    return police

def backtrack(police, zostavajuce_odborne_knihy, zostavajuce_knihy_beleterie, polica_index, pouzite_police, assignment):
    # Základný prípad: ak už nezostali žiadne knihy na priradenie
    if zostavajuce_odborne_knihy == 0 and zostavajuce_knihy_beleterie == 0:
        return True, assignment

    # Ak sme už prešli všetky poličky a stále sú zostávajúce knihy, zlyháme
    if polica_index == len(police):
        return False, None

    aktualna_polica = police[polica_index]

    # Skúsme priradiť aktuálnu poličku technickým knihám
    if zostavajuce_odborne_knihy >= aktualna_polica:
        assignment.append((aktualna_polica, 'Odborné_knihy'))
        uspech, vysledok = backtrack(police, zostavajuce_odborne_knihy - aktualna_polica, zostavajuce_knihy_beleterie, polica_index + 1, pouzite_police + 1, assignment)
        if uspech:
            return uspech, vysledok
        assignment.pop()

    # Skúsme priradiť aktuálnu poličku beleterii
    if zostavajuce_knihy_beleterie >= aktualna_polica:
        assignment.append((aktualna_polica, 'Beleteria_knihy'))
        uspech, vysledok = backtrack(police, zostavajuce_odborne_knihy, zostavajuce_knihy_beleterie - aktualna_polica, polica_index + 1, pouzite_police + 1, assignment)
        if uspech:
            return uspech, vysledok
        assignment.pop()

    # Skúsme nevyužiť aktuálnu poličku (ak ešte nie je rozhodnuté)
    uspech, vysledok = backtrack(police, zostavajuce_odborne_knihy, zostavajuce_knihy_beleterie, polica_index + 1, pouzite_police, assignment)
    if uspech:
        return uspech, vysledok

    return False, None

def assign_shelves(police, odborne_knihy, knihy_beleteria):
    police = sort_shelves(police)
    success, final_assignment = backtrack(police, odborne_knihy, knihy_beleteria, 0, 0, [])
    if success:
        return final_assignment
    else:
        return "Knihy sa nedajú prideliť podľa podmienok zadania"


# Použitie
shelves = [2, 4, 2, 2, 5, 3, 2, 3, 6]
technical_books = 9
beletery_books = 7


pridelenie = assign_shelves(shelves, technical_books, beletery_books)
if pridelenie != "Knihy sa nedajú prideliť podľa podmienok zadania":
    print("Nájdené pridelenie je:")
    for polica, druh in pridelenie:
        print(f"Polica veľkosti: {polica}, Druh knihy: {druh}")
else:
    print(pridelenie)
