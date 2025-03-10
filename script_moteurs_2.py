# script permettant le test de mise en marche des deux moteurs (safran et GV) simultanément.
# Les commandes se font en PWM uniquement pour le moment.

import RPi.GPIO as GPIO
from time import sleep

# Définition des pins utilisés
ENA_GV = 32  # PWM0 matériel par défaut moteur A GV : GPIO12
sens_GV = 29  # Controle le sens du moteur : GPIO5

ENA_saf = 33  # PWM1 matériel par défaut moteur B Safran : GPIO13
sens_saf = 31  # Controle le sens du moteur : GPIO18 -> GPIO6

# Configuration des GPIOs
GPIO.setmode(GPIO.BOARD) # note les entrées avec les numéros des pins et non ceux des GPIOs
GPIO.setup(ENA_GV, GPIO.OUT) # on utilise le pin 32 comme une sortie GPIO
GPIO.setup(sens_GV, GPIO.OUT)
GPIO.setup(ENA_saf, GPIO.OUT)
GPIO.setup(sens_saf, GPIO.OUT)

# Initialisation des signaux PWM
PWM_GV = GPIO.PWM(ENA_GV, 100) # initialise un signal PWM sur une broche GPIO (ENA_GV) à 100 Hz
PWM_saf = GPIO.PWM(ENA_saf, 100) # pareil pour le safran 
PWM_GV.start(0) # le signal vaut 0 (moteur éteint)
PWM_saf.start(0)

try:
    while True:
        # Test moteur 1 (GV) & 2 (safran) :
        GPIO.output(sens_GV, GPIO.HIGH) # on force le sens de rotation du moteur
        GPIO.output(sens_saf, GPIO.HIGH)
        PWM_GV.ChangeDutyCycle(20) # on fait tourner le moteur à 30% de sa vitesse
        PWM_saf.ChangeDutyCycle(10)

        sleep(1) # maintient la vitesse pendant 5 secondes

        PWM_GV.ChangeDutyCycle(0)
        PWM_saf.ChangeDutyCycle(0)

        sleep(2) # s'arrête pendant 2s

        GPIO.output(sens_GV, GPIO.LOW) # on inverse le sens de rotation du moteur
        GPIO.output(sens_saf, GPIO.LOW)
        PWM_GV.ChangeDutyCycle(20)
        PWM_saf.ChangeDutyCycle(10)

        sleep(1) # les moteurs tournent dans l'autre sens pendant 5s

        PWM_GV.ChangeDutyCycle(0)
        PWM_saf.ChangeDutyCycle(0)

        sleep(2) # s'arrête pendant 2s

except KeyboardInterrupt:
    print("Arrêt du programme")
    PWM_GV.stop()
    PWM_saf.stop()
    GPIO.cleanup()
