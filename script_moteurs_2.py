import RPi.GPIO as GPIO
import time

# Définition des pins utilisés
ENA_GV = 32  # PWM0 matériel par défaut moteur A GV : GPIO12
sens_GV = 29  # Controle le sens du moteur : GPIO5

ENA_saf = 33  # PWM1 matériel par défaut moteur B Safran : GPIO13
sens_saf = 12  # Controle le sens du moteur : GPIO18

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
        # Test moteur 1 :
        GPIO.output(sens_GV, HIGH) # on force le sens de rotation du moteur
        PWM_GV.ChangeDutyCycle(30) # on fait tourner le moteur à 30% de sa vitesse
        sleep(5) # maintient la vitesse pendant 5 secondes
        GPIO.output(sens_GV, LOW) # on inverse le sens de rotation du moteur
        sleep(5) # il tourne dans l'autre sens pendant 5s

        # Test moteur 2 :
        GPIO.output(sens_saf, HIGH) # on force le sens de rotation du moteur
        PWM_saf.ChangeDutyCycle(30) # on fait tourner le moteur à 30% de sa vitesse
        sleep(5) # maintient la vitesse pendant 5 secondes
        GPIO.output(sens_saf, LOW) # on inverse le sens de rotation du moteur
        sleep(5) # il tourne dans l'autre sens pendant 5s

except KeyboardInterrupt:
    print("Arrêt du programme")
    PWM_GV.stop()
    PWM_saf.stop()
    GPIO.cleanup()