#!/usr/bin/env python
# coding: utf-8

# # SSBU CV2: Úvod do Pythonu
# 
# ## Python
# Python je vysokoúrovňový programovací jazyk, ktorý je:
# - Interpretovaný (nevytvára spustiteľný kód),
# - Objektovo-orientovaný,
# - Freeware a open source,
# - Dynamicky typovaný,
# - Rozsiahly na knižnice, najmä na spracovanie a vizualizáciu údajov, štatistiku a strojové učenie.
# 
# ---
# 
# ## **1. Základná syntax**
# ### Kľúčové vlastnosti:
# - Kód sa oddeľuje **odsadením (indentáciou - tab)** (nie zátvorkami ako v C/C++).
# - Premenné sa **nemusia vytvárať s definovaním dátového typu** – Python ho priradí automaticky a môže sa dynamicky meniť.
# - Na výpis na konzolu používame **funkciu `print()`** - [Dokumentácia print()](https://docs.python.org/3/library/functions.html#print).
# 
# **Príklad:**

# In[ ]:


print("Hello, World!")


# **Úloha na precvičenie:** Napíšte príkaz, ktorý vypíše vaše meno a vek.

# In[ ]:


# TODO


# ---
# 
# ## **2. Dátové typy a premenné**
# ### Základné dátové typy v Pythone:
# - Vstavané dátové typy a operácie: [Dokumentácia Built-in Types](https://docs.python.org/3/library/stdtypes.html)
# - **Textové:** `str`
# - **Číselné:** `int`, `float`, `complex`
# - **Sekvenčné:** `list`, `tuple`, `range`
# - **Mapovacie:** `dict`
# - **Množinové:** `set`, `frozenset`
# - **Booleovské:** `bool`
# - **Binárne:** `bytes`, `bytearray`, `memoryview`
# - **None:** `NoneType` (None objekt - neobsahuje hodnotu) - [Dokumentácia NoneType](https://docs.python.org/3/library/constants.html#None)
# 
# + dalšie - [Dokumentácia Python Data Types](https://docs.python.org/3/library/datatypes.html)
# 
# + zistenie typu premennej - funkcia type - [Dokumentácia type](https://docs.python.org/3/library/functions.html#type)
# 
# **Príklad:**

# In[ ]:


name = "John"
age = 25
height = 6.2
is_student = False
print(type(name), type(age), type(height), type(is_student))


# **Úloha:** Vytvorte a inicializujte premenné `blood_type`, `insurance_code` a `allergic_to_paracetamol` a vypíšte ich dátové typy.

# In[ ]:


# TODO


# ---
# 
# ## **3. Operátory**
# Operátory sú použiteľné štandardne, alebo ako funkcie (potrebné importovaqť modul operator) - [Dokumentácia operator](https://docs.python.org/3/library/operator.html)
# 
# Python podporuje:
# - **Aritmetické operátory:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
# - **Porovnávacie operátory:** `==`, `!=`, `>`, `<`, `>=`, `<=`
# - **Logické operátory:** `and`, `or`, `not` - pozor na typy, ktoré porovnávate (napr. bool a int)
# 
# **Príklad:**

# In[ ]:


# arithmetic operations
x, y = 10, 3
print(x + y, x * y, x > y, x and y)

# comparison operations
print("Is x smaller than y?: ", x < y)

import operator
compare = operator.ge(x, y) # greater or equal
print("Is x greater or equal to y?:", compare)

# logical operations
is_allergic = True
is_true = is_allergic or 0
print("Value of is_true:", is_true)
print("Operator sign comparison: ", is_true & False)


# **Úloha:** Vytvorte premenné `a = 20`, `b = 5` a vypočítajte súčet, rozdiel a ich podiel.

# In[ ]:


# TODO


# ---
# 
# ## **4. Podmienky**
# ### Kľúčové vlastnosti:
# - Používame `if`, `elif`, `else` na riadenie toku programu.
# - Kód v jednotlivých vetvách sú oddelené odsadením.
# 
# **Príklad:**

# In[ ]:


age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You have just become an adult.")
else:
    print("You are an adult.")


# **Úloha:** Napíšte kód, ktorý skontroluje, či je číslo párne alebo nepárne a overte ho použitím rôznych čísel. - [Dokumentácia expressions (modulo)](https://docs.python.org/3/reference/expressions.html)
# 

# In[ ]:


# TODO


# ---
# 
# ## **5. Cykly**
# - `for` cyklus pre iteráciu cez zoznamy a sekvencie.
# - `while` cyklus na opakovanie, kým je podmienka splnená.
# - Použitie `break` a `continue` je rovnaké ako v iných programovacích jazykoch
# - Použitie `else` - Táto vetva obsahuje príkazy, ktoré sa majú vykonať po vykonaní cyklu, ak nebol ukončený pomocou `break`
# - Pri `for` cykle je potrebné vytvoriť iterovateľný objekt - napr. sekvenciu čísel, zoznam, slovník, množinu, alebo iný iterovateľný objekt
#     - Funkcia `range` - sekvencia čísel - [Dokumentácia range](https://docs.python.org/3/library/functions.html#func-range)
#     - Funkcia `len` - dlžka zoznamu - [Dokumentácia len](https://docs.python.org/3/library/functions.html#len)
# 
# 
# **Príklad:**

# In[ ]:


for i in range(5):
    print(i)


# **Úloha:** Napíšte program, ktorý vypíše čísla od 10 do 1. Použite `for` cyklus a funkciu `range`.

# In[ ]:


# TODO


# ---
# 
# ## **6. Funkcie**
# - Definujeme ich pomocou kľúčového slova `def` a odsadením tela funkcie.
# - Môžu mať parametre a návratové hodnoty.
# - Parametrom funkcie sa môže ale nemusí definovať typ
# - Voliteľné parametre majú predvolenú hodnotu, ktorá sa nastaví, ak hodnota parametra nie je definovaná
# - Dokumentačné komentáre sa nachádzajú pod definíciou (vo vnútri triedy/funkcie) - označené `"""`
# 
# 
# - **Príklad:**

# In[ ]:


# age is optional
def greet(name, age = -1):
    # documentation comment
    """Function to greet a person."""
    print("Name:", name, "\tAge: ", age)

# function call
greet("Alice")
greet("Benjamin", 22)


# **Úloha:** Napíšte funkciu, ktorá vypočíta a vráti druhú mocninu čísla. Použite voliteľný parameter pre zmenu exponentu. - [Dokumentácia functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Dokumentácia pow](https://docs.python.org/3/library/functions.html#pow)

# In[ ]:


# TODO


# ---
# 
# ## **7. Údajové štruktúry**
# - Základné štruktúry:
#     - list (`[]`)
#     - dictionary (`{kľúč : hodnota}`)
#     - set (`{}`)
#     - tuple (`()`)
# - [Dokumentacia datastructures](https://docs.python.org/3/tutorial/datastructures.html)
# 
# **List (Zoznam):**
# 
# - Definícia - pomocou `[]`
# - Uchováva poradie prvkov.
# - Prvky v liste sú indexované - každý prvok má priradený index (začínajúci od 0) na identifikáciu jeho pozície v zozname.
# - Je `mutable` - jeho prvky môžu byť menené.
# 
# **Dictionary (Slovník):**
# 
# - Definícia - pomocou `{}` a kľúčov - `kľúč : hodnota`
# - Uchováva dáta v pároch kľúč-hodnota podobne ako objekty JSON.
# - Kľúče musia byť jedinečné a sú hashovateľné.
# - Poradie prvkov je zachované tak, ako boli vložené (od verzie 3.7).
# - Tiež je `mutable`.
# 
# **Set (Množina):**
# 
# - Definícia - pomocou `{}`
# - Obsahuje **jedinečné prvky**, žiadne duplikáty.
# - Prvky nie sú indexované, nie je možné ich získať pomocou indexu, nie je usporiadaná.
# - Je `mutable` a môže sa použiť na vykonávanie matematických operácií množín, ako sú zjednotenie, prienik, rozdiel atď.
# 
# **Tuple (N-tica):**
# 
# - Definícia - pomocou `()`
# - Uchováva poradie prvkov.
# - Prvky sú indexované a každý prvok má svoj unikátny index.
# - Je `immutable` (nemeniteľná) - jeho prvky nemôžu byť po vytvorení zmenené.
# - Môže obsahovať rôzne dátové typy.
# 
# **Príklad:**

# In[ ]:


# list
numbers = [1, 2, 3, 4, 5]
print("First element of the list:", numbers[0])  # Accessing elements of the list by index
numbers = numbers + [6, 7, 8]  # Adding elements to the list

# dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Name:", person['name'])
person['city'] = 'Los Angeles'  # Changing value of the key 'city'
person['blood_type'] = 'A+'  # Adding new key-value pair

# set
medical_treatment = {'paracetamol', 'ibuprofen', 'aspirin'}
print("Medical treatments:", medical_treatment)
medical_treatment.add('antibiotics')  # Adding new element to the set

# tuples
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("Coordinate x:", coordinates[0])


# **Úloha:** Vytvorte zoznam `patients` s údajmi o pacientoch (meno, vek, diagnóza). Vypíšte vek pacienta s indexom 2.
# 

# In[ ]:


# TODO


# ---
# 
# ## **8. Práca so súbormi**
# ### Čítanie a zápis do súborov:
# - Pri otvorení súboru je potrebné definovať mód otvorenia - určuje, ako bude súbor použitý (čítanie, zápis, pridávanie do existujúceho súboru, atď.).
#     - 'w' pre zápis (vytvorenie súboru, prípadne prepis existujúceho súboru)
#     - 'r' pre čítanie
#     - 'a' pre pridávanie (zápis na koniec existujúceho súboru (append)).
# 
# - Použitie `with` klauzuly (kontextový manažér) - [Dokumentácia input/output](https://docs.python.org/3/tutorial/inputoutput.html)
#     - Pomáha spravovať súbory, automatizuje zatvorenie súboru po tom, čo je blok kódu pod klauzulou with dokončený. (aj pri vyhodení výnimky)
#     - Znižuje riziko zanechania otvoreného súboru, čo by mohlo viesť k únikom pamäti alebo iným problémom.
# 
# 
# **Príklad:**

# In[ ]:


# writing to a file
with open("data/example.csv", "w+") as file:
    file.write("patient_id,name,age,diagnosis\n") # writing a header

# reading from a file
with open('data/example.csv', 'r') as file:
    contents = file.read()
    print("File contents:", contents)


# **Úloha:** Otvorte súbor `example.csv`v móde "append" a zapíšte do neho údaje o troch pacientoch. (Údaje vymyslite)

# In[ ]:


# TODO


# ---
# ## **9. Moduly**
# - Modulom môže byť akýkoľvek vlastný .py skript
# - Importuje sa do projektu použitím kĺúčového slova `import`
# - Pri importovaní modulu je možné priradiť mu alias - skratku, ktorá sa používa ďalej v skripte na zavolanie funkcií alebo metód tried modulu (napr. `import my_module as mod`)
# - Možnosť importovať len konkrétne objekty/funkcie z knižnice (napr. `from my_module import module_foo`)
# 
# **Vytvorenie modulu**
# - Python skript (my_module.py)
# 
# **Príklad:**

# In[ ]:


import my_module

my_module.module_foo()


# **Úloha:** Vytvorte vlastný modul a importujte ho do projektu s aliasom.

# In[ ]:


# TODO


# ---
# ## **10. Ošetrovanie výnimiek**
# - Pri ošetrovaní výnimiek sa používa `try-except` blok - [Dokumentácia errors](https://docs.python.org/3/tutorial/errors.html)
# - Príklady základných typov výnimiek:
#     - TypeError: vykonanie operácie s nekompatibilným typom (sčítanie reťazca a čísla)
#     - IndexError: pristúpenie k prvku zoznamu pomocou indexu, ktorý je mimo rozsah
#     - KeyError: pristúpenie k hodnote v slovníku pomocou kľúča, ktorý neexistuje
#     - ValueError: funkcia dostane argument s nevhodnou hodnotou
#     - NameError: použitie nedefinovanej premennej
#     - FileNotFoundError: pokus o otvorenie neexistujúceho súboru
#     - ZeroDivisionError: delenie čísla nulou
# 
# **Príklad:**

# In[ ]:


undefined_variable = 5

try:
    print(undefined_variable)
except NameError as e:
    print("Error:", e)


# **Úloha:** Ošetrite výnimku pri delení čísla nulou.

# In[ ]:


# TODO


# ---
# ## **11. Práca s obrázkami**
# Na prácu s obrázkami sa používajú knižnice, napr. pillow (PIL) - [Dokumentácia Image](https://pillow.readthedocs.io/en/stable/reference/Image.html)
# - Základnými operáciami pre prácu s obrázkami sú načítanie a uloženie (open/save)
# - Knižnice ponúkajú rôzne možnosti transformácie obrazu, napr. prevod na odtiene šedej (hodnoty 0-255) - funkcia convert [Dokumentácia convert](https://www.codecademy.com/resources/docs/pillow/image/convert)
# - Normalizácia obrazu (prevod na hodnoty 0-1) je prospešná pre strojové učenie
# - Knižnice ponúkajú množstvo ďalších úprav (rotácie, orezanie, zmena veľkosti, pridanie filtrov, atď.) - všetky operácie sú vždy dostupné v dokumentácii knižnice
# 
# **Príklad:**

# In[ ]:


from PIL import Image
img = Image.open("../data/microscope.jpg")
gray_img = img.convert("L")
gray_img.save("data/microscope_g.jpg")


# **Úloha:** Otvorte obrázok `microscope_g.jpg`, otočte ho o 90° a uložte. Použite funkciu rotate - [Dokumentácia rotate](https://www.codecademy.com/resources/docs/pillow/image/rotate)

# In[ ]:


# TODO


# ---
# 
# ## **12. OOP v Pythone**
# - Triedy definujeme pomocou `class`.
# - Používame konštruktor `__init__`.
# - Prístup k atribútom triedy je pomocou `self`.
# - Metódy triedy majú ako prvý parameter `self`.
# - Metódy triedy sa volajú na inštancii triedy.
# - Atribúty triedy sú definované v konštruktore.
# - Metódy triedy sú definované v rámci triedy.
# - Prístup k atribútom triedy je pomocou `.`.
# - Vytvorenie inštancie triedy - `object = ClassName()`.
# - Dedičnosť - trieda môže dediť od inej triedy.
# - Trieda môže byť abstraktná - nemôže byť inštanciovaná, ale môže byť použitá ako základ pre iné triedy.
# - Polymorfizmus - triedy môžu mať metódy s rovnakým názvom, ale s rôznou implementáciou.
# - Encapsulácia - skrytie atribútov triedy pred priamym prístupom zvonku.
# - Private atribúty a metódy - začínajú dvojitým podčiarkovníkom `__`.
# 
# **Príklad:**

# In[ ]:


class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def __check_if_info_is_defined(self):
        if self.name and self.age and self.diagnosis:
            return True
        return False

    def display_info(self):
        if self.__check_if_info_is_defined():
            print(f"Patient: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}")
        else:
            print("Some of the information is undefined.")

p1 = Patient("Anna", 30, "Diabetes")
p2 = Patient("Peter", 25, None)
p1.display_info()
p2.display_info()


# **Úloha:** Vytvorte triedu `Doctor` s atribútmi `name`, `specialization` a `patients`. Vytvorte metódu `add_patient`, ktorá pridá pacienta do zoznamu pacientov. - [Dokumentácia classes](https://docs.python.org/3/tutorial/classes.html). Pridajte pacientov p1 a p2 do zoznamu a vypíšte zoznam pacientov.

# In[ ]:


# TODO


# ---
# 
# ## **13. Lambda funkcie**
# 
# - Lambda funkcie sú anonymné funkcie, definované pomocou kľúčového slova lambda - [Dokumentácia lambda](https://docs.python.org/3/reference/expressions.html#lambda)
# - Môže mať ľubovoľný počet argumentov, a obsahuje výraz alebo list výrazov, ktorý je vyhodnotený a vrátený
# - Forma zápisu je `lambda arguments: expression`
# - Používa sa na definovanie jednoduchých funkcií, ktoré sa používajú len raz
# - Môže byť použitá spoločne s funkciami `map`, `filter`, `reduce`
# - Môže obsahovať podmienky a cykly
# 
# **Príklad:**

# In[ ]:


# Lambda function to calculate square of a number
square = lambda x: x**2

print("Square of 5 using lambda function:", square(5))


# **Úloha:** Vytvorte lambda funkciu s podmienkou (`if-else`), ktorá vráti text `even` alebo `odd`, podľa toho, čí je číslo párne alebo nepárne. Použitie podmienky v lambda funkcii má formu `lambda arguments: true_return_expression if condition else false_return_expression`.

# In[ ]:


# TODO


# ---
# ## **14. Mapovanie, Filtrovanie a Redukcia**
# 
# - Tieto fukcie sa používajú pri spracovaní kolekcií, ako sú zoznamy, slovníky, množiny, atď., podobne ako v jazyku Matlab.
# + **`map`** - [Dokumentácia map](https://docs.python.org/3/library/functions.html#map)
#     - Aplikuje danú funkciu na každý prvok iterovateľného objektu (napr. zoznam) a vracia iterátor s výsledkami
#     - napr. použitie s lambda funkciou na výpočet štvorca každého čísla v zozname numbers
# + **`filter`** - [Dokumentácia filter](https://docs.python.org/3/library/functions.html#filter)
#     - Odfiltruje prvky iterovateľného objektu, ponechávajúc len tie, pre ktoré funkcia vráti True
#     - napr. lambda funkcia s vyselektovanie len párnych čísel zo zoznamu numbers
# + **`reduce`** - [Dokumentácia reduce](https://docs.python.org/3/library/functools.html)
#     - Postupne aplikuje funkciu na prvky iterovateľného objektu, znižuje ich na jediný výsledok
#     - napr. funkcia reduce z modulu functools s lambda funkciou na výpočet súčinu všetkých čísel v zozname numbers
# 
# **Príklad:**

# In[ ]:


# map function
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)


# **Úloha:** Vytvorte zoznam `ages` s vekmi pacientov. Použite funkciu `filter` a lambda funkciu na vyselektovanie pacientov vo veku 18-65 rokov.

# In[ ]:


# TODO


# ---
# 
# ## **15. Práca s DataFrame (Pandas)**
# Použitie knižnice `pandas` na spracovanie tabuliek - [Dokumentácia DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
# - Dataframe je dvojrozmerná dátová štruktúra (tabuľka) v knižnici Pandas, vhodná pre spracovanie textových a číselných datasetov
# - Práca so štruktúrovanými dátami
# - Využitie štruktúry DataFrame je vhodné najmä kvôli efektívnej implementácii rôznych operácií nad dátami
# - Základné vlastnosti DataFrame:
#     - Môže obsahovať heterogénne údaje - čísla, reťazce, objekty, ..
#     - Podporuje aritmetické operácie na riadkoch a stĺpcoch
#     - Umožňuje jednoduché zlučovanie, spájanie, filtrácia dát, atď.
# 
# **Príklad:**

# In[ ]:


import pandas as pd

# create DataFrame from dictionary
data = {
    'name': ['Christina', 'Jan', 'Peter', 'Adam'],
    'age': [28, 15, 29, 67],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Boston']
}
df = pd.DataFrame(data)

# show dataframe
print(df)


# **Úloha:** Vytvorte DataFrame s dátami zo súboru `data/example.csv`. Pre vytvorenie DataFrame priamo z csv súboru použite funkciu read_csv - [Dokumentácia read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Použite funkciu `describe` na zobrazenie štatistík dát - [Dokumentácia describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html).

# In[ ]:


# TODO


# ---
# 
# ### **Zhrnutie**
# - Python je jednoduchý jazyk vhodný na spracovanie dát.
# - Poskytuje množstvo knižníc na spracovanie dát, strojové učenie, vizualizáciu, atď.
# 
# ##### Referencie
# 
# https://docs.python.org/3.12/tutorial/index.html
# 
# https://python.input.sk/z/01.html
# 
# https://unsplash.com/photos/a-close-up-of-a-section-of-a-humans-stomach-Q2PkRn63Oug
