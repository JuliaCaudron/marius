import RPi.GPIO as GPIO
import time

# Définition des broches
PWM_GV = 32  # PWM0 matériel par défaut moteur A GV : GPIO12
sens_GV = 29  # Controle le sens du moteur : GPIO5

PWM_saf = 33  # PWM1 matériel par défaut moteur B Safran : GPIO13
sens_saf = 12  # Controle le sens du moteur : GPIO18

# Configuration des GPIO
GPIO.setmode(GPIO.BOARD) # note les entrées avec les numéros des GPIOs et non ceux des pins
GPIO.setup(PWM_GV, GPIO.OUT)
GPIO.setup(sens_GV, GPIO.OUT)
GPIO.setup(PWM_saf, GPIO.OUT)
GPIO.setup(sens_saf, GPIO.OUT)