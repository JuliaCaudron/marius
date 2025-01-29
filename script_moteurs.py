import RPi.GPIO as GPIO
import time

# Définition des broches
PWMA = 12  # PWM0 matériel par défaut moteur A GV
SENSA = 5  # Controle le sens du moteur

PWMB = 13  # PWM1 matériel par défaut moteur B Safran
SENSB = 18  # Controle le sens du moteur

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([SENSA, SENSB], GPIO.OUT)
GPIO.setup([PWMA, PWMB], GPIO.OUT)

# Initialisation du PWM matériel
pwmA = GPIO.PWM(PWMA, 1000)  # Fréquence 1 kHz
pwmB = GPIO.PWM(PWMB, 1000)  # Fréquence 1 kHz
pwmA.start(0)  # Vitesse à 0%
pwmB.start(0)

def moteur_A(vitesse, sens):
    """Contrôle le moteur A (gauche)"""
    if sens == "avant":
        GPIO.output(SENSA, GPIO.HIGH)
    elif sens == "arrière":
        GPIO.output(SENSA, GPIO.LOW)
    else:
        GPIO.output(SENSA, GPIO.LOW) # par défaut le sens est arrière si on précise pas ou un truc faux

    pwmA.ChangeDutyCycle(vitesse)

def moteur_B(vitesse, sens):
    """Contrôle le moteur B (droit)"""
    if sens == "avant":
        GPIO.output(SENSB, GPIO.HIGH)
    elif sens == "arrière":
        GPIO.output(SENSB, GPIO.LOW)
    else:
        GPIO.output(SENSB, GPIO.LOW)

    pwmB.ChangeDutyCycle(vitesse)

try:
    while True:
        # Avancer à 50% de vitesse
        moteur_A(50, "avant")
        moteur_B(50, "avant")
        time.sleep(2) # fait tourner le moteur pendant 2 secondes

        # Reculer à 50% de vitesse
        moteur_A(50, "arrière")
        moteur_B(50, "arrière")
        time.sleep(2) # fait tourner le moteur pendant 2 secondes

        # Arrêt
        moteur_A(0, "stop")
        moteur_B(0, "stop")
        time.sleep(2) # s'arrête pendant 2 secondes

except KeyboardInterrupt:
    print("Arrêt du programme")
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
