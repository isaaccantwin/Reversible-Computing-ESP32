from machine import Pin
import time
import math

leds=[Pin(5,Pin.OUT),Pin(6,Pin.OUT),Pin(7,Pin.OUT),Pin(8,Pin.OUT)]

def display(state):
    for i in range(len(leds)):
        if i < len(state):
            leds[i].value(state[i])
        else:
            leds[i].value(0)

def toffoli(a,b,c):
    return a,b,(a&b)^c

def CNOT(a,b,cbit):
    tbit=0
    tbit=cbit-tbit
    kbit=(a,b,cbit,tbit)
    display(kbit)
    print(kbit)

def info_loss(inbit,outbit):
    infoLoss=len(inbit)-len(outbit)
    return max(0,infoLoss)

def energy_loss(infoLoss):
    ELoss=infoLoss*kB*T*math.log(2)
    return max(0,ELoss)

def back(ina,inb,inc):
    global tatalEsave
    inbit=(ina,inb,inc)
    oua=ina
    oub=inb
    ouc=toffoli(ina,inb,inc)
    print(ouc)
    display(ouc)
    time.sleep(0.3)
    CNOT(oua,oub,ouc[2])
    time.sleep(0.3)
    bouc=toffoli(oua,oub,ouc[2])
    display(bouc)
    print(bouc)
    print(" ")
    time.sleep(1)

for a in range(2):
    for b in range(2):
        for c in range(2):
            back(a,b,c)

