import generator_tock
import dolzina
import minimalno_vpeto_drevo
import ploscine


# KROG

polmeri = [1, 1.5, 2, 10]
ponovitve = 1000
st_tock = [10, 100, 500]
sez_krog = []

for polmer in polmeri:
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
        sez_krog.append(maksimum)



# KVADRAT

stranice = [ploscine.ploscina(k, "kvadrat") for k in polmeri]
ponovitve = 1000
st_tock = [10, 100, 500]
sez_kvadrat  =[]

for stranica in stranice:
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
        sez_kvadrat.append(maksimum)


# PRAVOKOTNIK

stranici = ploscine.ploscina(1, "pravokotnik")
ponovitve = 1000
st_tock = [10, 100, 500]
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


# ELIPSA

stranice_ax = [ploscine.ploscina(k, "elipsa")[0] for k in polmeri]
stranice_by = [ploscine.ploscina(k, "elipsa")[1] for k in polmeri]
ponovitve = 1000
st_tock = [10, 100, 500]
sez_elipsa  =[]

for i in range(len(stranice_ax)):
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.elipsa(stranice_ax[i], stranice_by[i], tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        sez_elipsa.append(maksimum)



# ENAKOSTRANICNI TRIKOTNIK

stranica_a = [ploscine.ploscina(k, "trikotnik") for k in polmeri]
ponovitve = 1000
st_tock = [10, 100, 500]
sez_trikotnik  =[]

for stranica in stranica_a:
    for tocke in st_tock:
        maksimum = 0
        for i in range(ponovitve):
            a = generator_tock.trikotnik(stranica_a, tocke)
            b = dolzina.dolzina_med_tockami(a)
            c = minimalno_vpeto_drevo.prim(a, b)[1]
            if maksimum > c:
                pass
            else:
                maksimum = c
        sez_trikotnik.append(maksimum)