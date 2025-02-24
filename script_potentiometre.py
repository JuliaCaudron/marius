# -*- coding: utf-8 -*-
from MCP3008 import MCP3008
from time import sleep

try:
    while True:
        adc = MCP3008()
        value = adc.read( channel = 0 ) # Vous pouvez bien entendu adapter le canal à lire
        print("Tension appliquée : %.2f" % (value / 1023.0 * 3.3) ) # affichage de la valeur du potentiomètre
        sleep(1) # rafraichissement tout les 1 secondes

except KeyboardInterrupt:
    print("Arrêt du programme")