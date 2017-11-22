# An Optimal Bound for the MST Algorithm to Compute Energy Efficient Broadcat Strees in Wireless Networks

# uvoz knjiznic
import numpy
import math


###########################################################
# Poln graf na zgeneriranih tockah razlicnih likov in     #
# matrika dolzin med tockami                              #
###########################################################

def prim(seznam_tock, matrika_dolzin):
    '''Funkcija sprejme seznam slovarjev tock (return funkcij generatorjev tock) in matriko dolzin med
        temi tockami (return funkcije dolzina).
        Funkcija najde minimalno vpeto drevo. Izracunamo se vsoto cen minimalnega vpetega drevesa,
        ki pa ni del Primovega algoritma'''
    st_vozlisc = len(seznam_tock)
    # Na zacetku pripravimo mnozico vozlisc, ki jih bomo za lepsi pregled oznacili z indeksi (0, 1, 2, ...)
    # Q bo vseboval vsa vozlisca, ki jih se nismo uporabili v seznamu F
    Q = {i for i in range(st_vozlisc)}
    # Pripravimo seznam, za katerega bo veljalo: C[i] = najcenejsa povezava do i.
    # Sprva natavimo vse vrednosti na neskoncno.
    C = [math.inf for i in range(st_vozlisc)]
    # Nastavimo se vrednosti seznama E na "special flag value" (-1), kar kaze na to, da ne obstaja nobena povezava,
    # ki bi povezovala vozlisce E[i] s prejsnjimi vozlisci.
    # Komentar k izbiri "flag value" -> uporabimo -1 in ne npr. 0, ker imamo vozlisca nastavljena po indeksih: 0,1,...
    E = [-1 for i in range(st_vozlisc)]
    # Pripravimo prazen seznam F
    F = []
    # Ponavljamo, dokler ne uporabimo vseh vozlisc (torej je mnozica Q prazna)
    while len(Q):
        # Najdemo "vozlisce", ki je v Q in ima najcenejso povezavo do "vozlisce"
        vozlisce = C.index(min([C[i] for i in Q]))
        # Odstranimo vozlisce iz mnozice neuporabljenih vozlisc
        Q.remove(vozlisce)
        # Dodamo vozlisce v F
        F.append(vozlisce)
        # Ce E[vozlisce] nima vrednosti -1 ("flag value), dodamo E[vozlisce] v F
        if E[vozlisce] != -1:
            F.append(E[vozlisce])
        # Zanka gre cez vsako vozlisce i, za katero velja, da med i in vozlisce obstaja povezava
        for cena_povezave in matrika_dolzin[vozlisce]:
            i = numpy.where(matrika_dolzin[vozlisce] == cena_povezave)[0][0]
            # Ce je vozlisce i v Q in je cena povezave med i in vozlisce manjsa od C[i],
            # potem C[i] nastavimo na zdajsnjo ceno povezave in v E[i] shranimo vozlisce, tako da kaze na
            # povezavo med i in vozlisce
            if (i in Q) and (cena_povezave != 0) and (cena_povezave < C[i]):
                C[i] = cena_povezave
                E[i] = vozlisce
    # Funkcija vrne povezave drevesa in vsoto cen med povezavemi v minimalnem vpetem drevesu
    # Vzamemo povezave od vkljucno drugega vozlisca
    F = F[1:]
    vsota = sum([(matrika_dolzin[F[2*i]][F[2*i+1]])**2 for i in range(st_vozlisc -1) ])
    return [F, vsota]