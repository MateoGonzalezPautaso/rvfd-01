from machine import ADC
from math import log
from time import sleep

adc = ADC(28)
# declaro el pin 28 para adc

while(1):

  lecturaADC = adc.read_u16()
  tension = lecturaADC * (3.3 / 65535)
  # tension es igual a la lectura que da el pin 28 por el Vref 16 bits (50.3 uV)
  resistenciaNTC = (10000) / ((3.3 / tension) - 1)
  temperaturaK = 3950 / (log(resistenciaNTC/10000) + (3950 / 298))
  temperaturaC = temperaturaK - 273.15
  print ("El valor del ADC es :", lecturaADC)
  print ("El valor de tension medido es:", tension)
  print ("El valor de la resistencia del NTC es:", resistenciaNTC)
  print ("El valor de la temperatura en C es: {:.3f}" .format(temperaturaC))
  print ("El valor de la temperatura en K es: {:.3f}" .format(temperaturaK))
  print ("-")
  sleep(1)