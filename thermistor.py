#!/usr/bin/env python
import ADC0832
import time
import math

def init():
  ADC0832.setup()

def resistance_to_temperature(Rt):
    BETA = 3950
    T0 = 298.15
    R0 = 10000

    T = 1 / (1 / T0 + (1 / BETA) * math.log(Rt / R0))
    T_celsius = T - 273.15
    return T_celsius

def temperature_to_fahrenheit(T_celsius):
    return (T_celsius * 9/5) + 32

def loop():
  while True:
    res = ADC0832.getADC(0)
    Vr = 3.3 * float(res) / 255
    Rt = 10000 * Vr / (3.3 - Vr)
    
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1/(273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    
    print('Temperature: %.2f°C / {Fah:%.2f}°F' %(Cel, Fah))
    time.sleep(0.2)
   
if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        print ('The end !')
