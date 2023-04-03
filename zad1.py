# Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu,
# zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i szerokość podłogi,
# (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)

import math


def my_function_with_parameter(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, opakowanie):
    pole = (dlugosc_podlogi * szerokosc_podlogi) * 1, 1
    powierzchnia_paneli = dlugosc_panela * szerokosc_panela * opakowanie
    ilosc_opakowan = math.ceil(powierzchnia_paneli / powierzchnia_paneli)
    print(ilosc_opakowan)


my_function_with_parameter(10, 10, 20, 10, 10)
