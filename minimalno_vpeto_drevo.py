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
    korak = 0
    # Ponavljamo, dokler ne uporabimo vseh vozlisc (torej je mnozica Q prazna)
    while len(Q):
        # Najdemo najmanjso vrednost v C (iscemo po cenah vozlisc, ki so se v Q)
        minimum = min([C[i] for i in Q])
        # naredimo seznam vseh indeksov z minimumom (=minimum)
        vsi_indeksi = [i for i, x in enumerate(C) if x == minimum]
        # Odstranimo vozlisce iz mnozice neuporabljenih vozlisc (pazimo na morebitne ponovitve razdalj
        # ki so sicer pri nakljucni izbiri zelo malo verjetne)
        vozlisce = 0
        for i in vsi_indeksi:
            if i in Q:
                vozlisce = i
                Q.remove(i)
                break
        # Dodamo vozlisce v F
        F.append(vozlisce)
        # Ce E[vozlisce] nima vrednosti -1 ("flag value), dodamo E[vozlisce] v F
        if E[vozlisce] != -1:
            F.append(E[vozlisce])
        # Zanka gre cez vsako vozlisce i, za katero velja, da med i in vozlisce obstaja povezava
        for sosed in range(st_vozlisc):
            cena = float(matrika_dolzin[vozlisce][sosed])
            # Ce je vozlisce i v Q in je cena povezave med i in vozlisce manjsa od C[i],
            # potem C[i] nastavimo na zdajsnjo ceno povezave in v E[i] shranimo vozlisce, tako da kaze na
            # povezavo med i in vozlisce
            if (sosed in Q) and (cena != 0) and (cena < C[sosed]):
                C[sosed] = cena
                E[sosed] = vozlisce
    # Funkcija vrne povezave drevesa in vsoto cen med povezavemi v minimalnem vpetem drevesu
    # Vzamemo povezave od vkljucno drugega vozlisca
    F = F[1:]
    vsota = sum([(matrika_dolzin[F[2*i]][F[2*i+1]])**2 for i in range(st_vozlisc -1) ])
    return [F, vsota]