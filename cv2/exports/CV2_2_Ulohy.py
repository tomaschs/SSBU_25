#!/usr/bin/env python
# coding: utf-8

# ## Doplnkové Úlohy
# 
# ---
# #### Úloha 1: Klasifikácia veku pacienta
# 
# Vytvorte funkciu, ktorá každého pacienta zaradí do kategórie `minor` (<18 rokov), `adult` (18-65 rokov) alebo `senior` (>65 rokov). 
# - Vstupom do funkcie je parameter `ages`, čo je štruktúra `list` obsahujúca vek niekoľkých pacientov.
# - Funkcia vracia štruktúru `dictionary`, ktorá pre každú kategóriu obsahuje počet pacientov v nej.
# - Vytvorte list `ages`, ktorý bude obsahovať aspoň 5 pacientov a vypíšte, počet pacientov podľa veku v jednotlivých kategóriách.

# In[ ]:


# TODO


# #### Úloha 2: Spracovanie súborov s údajmi o pacientoch
# 
# Zapište údaje o pacientoch (meno, diagnóza) do súboru s názvom `data/patients.csv`.
data = [
    ["Terri Mcmillan", "Hypertension"],
    ["David Thomas", "Diabetes"],
    ["Joshua Stewart", "Diabetes"],
    ["Jeffrey Martinez", "Depression"],
    ["Victor Roth", "Chronic Pain"],
    ["Timothy Schwartz", "Chronic Pain"],
    ["Desiree Palmer", "Hypertension"],
    ["Nathan Leonard", "Asthma"],
    ["Sara Lane", "Chronic Pain"],
    ["Ronald Riley", "Asthma"],
    ["Brian Roberts", "Depression"],
    ["Angel Harrington", "Hypertension"],
    ["Christina Hernandez", "Hypertension"],
    ["Christina Garza", "Asthma"],
    ["Joshua Armstrong", "Diabetes"],
    ["Lisa King", "Depression"],
    ["Erica Ferguson", "Diabetes"],
    ["Jesus Hansen", "Asthma"],
    ["Michael Thompson", "Chronic Pain"],
    ["Alexander Barajas", "Asthma"]
]
# In[ ]:


# TODO


# #### Úloha 3: Načítanie údajov do štruktúry DataFrame a ich vizualizácia
# 
# Načítajte údaje zo súboru `data/patients.csv` do štruktúry DataFrame (knižnica Pandas).
# - Vytvorte hlavičku pre tento DataFrame (pridajte názvy stĺpcov - `name` a `diagnosis`)
# - Pridajte do štruktúry DataFrame nový stĺpec s názvom "ID". hodnoty tohto stĺpca tvorí sekvencia čísel od 0 do 19.
# - Vypíšte hodnoty v stĺpci `diagnosis` a počet hodnôt pre jednotlivé diagnózy.

# In[ ]:


# TODO


# #### Úloha 4: Práca s obrazom
# Načítajte obrázok data/microscope_g.jpg a vykonajte na ňom operáciu priblíženia a orezania, tak aby na obrázku boli viditeľné iba bunky, nie okulár mikroskopu. (Použite súradnice (300, 550, 1000, 1250) - (left, top, right, bottom)) Nakoniec obrázok zobrazte.
# 
# Použite funkcie knižnice PIL:
#    - `Image.open()` - [Dokumentácia open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open)
#    - `Image.resize()` - [Dokumentácia resize](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize)
#    - `Image.crop()` - [Dokumentácia crop](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop)
#    - `Image.show()` - [Dokumentácia show](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.show)

# In[ ]:


# TODO


# #### Úloha 5: Vytvorenie triedy a analýza pacientov
# Vytvorte triedu `PatientData`, ktorá načíta údaje zo CSV súboru do DataFrame a umožní základnú analýzu.
# - Načítanie CSV súboru v konštruktore (použite súbor `data/patients.csv`) a uloženie do atribútu typu **DataFrame**.
# - Metóda `count_diagnoses()`, ktorá vráti počet pacientov s jednotlivými diagnózami.
# - Metóda `get_most_common_diagnosis(n)`, ktorá vráti n najčastejších diagnóz.
# - Metóda `display_summary()`, ktorá zobrazí základné štatistiky.

# In[ ]:


# TODO

