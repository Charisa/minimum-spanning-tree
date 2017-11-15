import generator_tock
import dolzina
import minimalno_vpeto_drevo
import ploscine


ponovitve = 1000
st_tock = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 50, 100]

# KROG

polmeri = [1, 1.5, 2, 10]
sez_krog = []

for polmer in polmeri:
    podseznam = []
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.krog(polmer, tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        podseznam.append(maksimum)
    sez_krog.append(podseznam)
print()



# KVADRAT

stranice = [ploscine.ploscina(k, "kvadrat") for k in polmeri]
sez_kvadrat  =[]

for stranica in stranice:
    podseznam = []
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.kvadrat(stranica, tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        podseznam.append(maksimum)
    sez_kvadrat.append(podseznam)
print(sez_kvadrat)


# PRAVOKOTNIK

stranici = ploscine.ploscina(1, "pravokotnik")
sez_pravokotnik = []

for tocke in st_tock:
    maksimum = 0
    for i in range(ponovitve):
        a = generator_tock.pravokotnik(stranici[0], stranici[1], tocke)
        b = dolzina.dolzina_med_tockami(a)
        c = minimalno_vpeto_drevo.prim(a, b)[1]
        if maksimum > c:
            pass
        else:
            maksimum = c
    sez_pravokotnik.append(maksimum)
print(sez_pravokotnik)


# ELIPSA

stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmeri]
stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmeri]
sez_elipsa  =[]

for i in range(len(stranice_ax)):
    podseznam = []
    for tocke in st_tock:
        maksimum = 0
        for k in range(ponovitve):
            a = generator_tock.elipsa(stranice_ax[i], stranice_by[i], tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        podseznam.append(maksimum)
    sez_elipsa.append(podseznam)
print(sez_elipsa)


# ENAKOSTRANICNI TRIKOTNIK

stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmeri]
sez_trikotnik  =[]

for stranica in stranica_a:
    podseznam = []
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.trikotnik(stranica, tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        podseznam.append(maksimum)
    sez_trikotnik.append(podseznam)
print(sez_trikotnik)