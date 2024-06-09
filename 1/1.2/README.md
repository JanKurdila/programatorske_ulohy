# Je naše prvé riešenie správne ???

    - Splňuje podmienku a aj podmienku b zo zadania ???
    - A splňa aj podmienku:  Ak existuje viacero vyhovujúcich rozdelení poličiek, nájdite to, ktoré obsadzuje čo najmenší počet poličiek. ???

 ## A čo takýto vstup ???

    police = [6, 5, 5, 3]
    odborne_knihy = 10
    beleteria_knihy = 9

    To by malo byť OK. Keď spustíme náš kód, tak výstup je: Knihy sa nedajú prideliť podľa podmienok zadania
    To znamená, že náš kód nefunguje vždy správne.

      V kóde sme použili algoritmus GREEDY. Ten nie vždy nájde optimálne riešenie!!!

      Prekrokujte si kód v https://pythontutor.com/python-compiler.html#mode=edit

Musíme teda urobiť kód pomocou inej stratégie - backtrack 

   - Pôvodný kód police.py
   - backtrack kód police1.py