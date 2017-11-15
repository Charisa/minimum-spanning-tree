
# uvoz knjiznic
import matplotlib.pyplot as plt
from copy import deepcopy


def narisi_krog(polmer, seznam_tock, drevo, risi):
    '''Funkcija sprejme dolzino polmera in seznam tock, in v koordinatni sistem narise krog in minimalno vpeto drevo'''
    if risi == "tocke":
        plt.plot( [i['x'] for i in seznam_tock], [i['y'] for i in seznam_tock], 'ro')
    dolzina_stranice = polmer * 2
    plt.xlim([-dolzina_stranice/2 - 2, dolzina_stranice/2 + 2])
    plt.ylim([-dolzina_stranice/2 - 2, dolzina_stranice/2 + 2])
    #plt.axis([-dolzina_stranice - 4, dolzina_stranice + 4, - dolzina_stranice - 4, dolzina_stranice + 4])
    plt.axis([-polmer, polmer, - polmer, polmer])
    circle = plt.Circle((0,0), dolzina_stranice/2)
    plt.gcf().gca().add_artist(circle)
    if risi == "drevo":
        x_tocke = [i['x'] for i in seznam_tock]
        y_tocke = [i['y'] for i in seznam_tock]
        drevo1 = deepcopy(drevo)
        while drevo1:
            plt.plot([x_tocke[drevo1[0]], x_tocke[drevo1[1]]], [y_tocke[drevo1[0]], y_tocke[drevo1[1]]], 'ro-')
            del drevo1[0]
            del drevo1 [0]
    plt.show()
    return