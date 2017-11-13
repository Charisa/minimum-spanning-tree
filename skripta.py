import generator_tock
import dolzina
import minimalno_vpeto_drevo

# krog s polmerom 1 (10, 100, 1.000, 10.000)

# 10 tock s 100 ponovitvami
polmer = 1
ponovitve = 100
maksimum = 0

for i in range(100):
    a = generator_tock.krog(polmer, ponovitve)
    b = dolzina.dolzina_med_tockami(a)
    c = minimalno_vpeto_drevo.prim(a, b)[1]
    if maksimum > c:
        pass
    else:
        maksimum = c


