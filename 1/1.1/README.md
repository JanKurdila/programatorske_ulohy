# <b>ALGORITMY/1</b>

![alt text](obr.jpg)

Mestská knižnica sa pripravuje na príchod veľkej zásielky kníh. V knižnici sú rôzne poličky.
Väčšie i menšie (na 2 knihy, na 3 knihy, ..., na 10 kníh, ...). Správca knižnice stojí pred neľahkou úlohou. K dispozícii má z oznam voľných políc (o každej, samozrejme, vie, koľko
kníh sa do nej zmestí) a vie, koľko odborných kníh a koľko beletrie prišlo v rámci zásielky.
Jeho cieľom je umiestniť knihy do políc tak, aby:

    a) Žiadna polička nebola „zmiešaná“ (polica je obsadená buď celá odbornými knihami alebo celá beletriou) – podmienka systematickej organizácie knižnice

    b) V každej poličke, kde sa umiestnia knihy, musí byť obsadená v plnej svojej kapacite.(cieľom je maximálne vyťažiť poličky).

*Vytvorte program, ktorý načíta údaje o voľných poličkách (o každej voľnej poličke načíta
počet jej miest), počet odborných kníh a počet beletrie v zásielke. Spôsob a prípadne formát
zadania vstupu nie sú nijako predpísané (vlastná voľba). Program následne vypíše také
rozdelenie/pridelenie poličiek knihám (ak existuje), ktoré spĺňa vyššie uvedené podmienky.
Ak existuje viacero vyhovujúcich rozdelení poličiek, nájdite to, ktoré obsadzuje čo najmenší
počet poličiek. Ak rozdelenie/priradenie neexistuje tak sa vypíše „nedá sa priradiť knihy“.*

## Príklad:
    Voľné police: 2 4 2 2 5 3 2 3 6
    Počet odborných kníh: 9
    Počet beletrie: 7

## Riešenie:
    Polica veľkosť: 6, -> Skupina: OK
    Polica veľkosť: 5, -> Skupina: B
    Polica veľkosť: 3, -> Skupina: OK
    Polica veľkosť: 2, - > Skupina: B