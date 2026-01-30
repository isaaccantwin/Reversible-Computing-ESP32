from machine import Pin
import math

kB=1.38e-23
t=300

leds = [Pin(5, Pin.OUT), Pin(6, Pin.OUT), Pin(7, Pin.OUT)]

def display(states):
    for i in range(len(leds)):
        if i < len(states):
            leds[i].value(states[i])
        else:
            leds[i].value(0)

a=int(input("a:1 or 0:"))
b=int(input("b:1 or 0:"))
inbitir=(a,b)
outir=(a&b,)
display(outir)

a=int(input("a:1 or 0:"))
b=int(input("b:1 or 0:"))
c=int(input("c:1 or 0:"))
inbitr=(a,b,c)
outr=(a,b,(a&b)^c)
display(outr)

def info_loss(inbit,outbit):
    infoLoss=len(inbit)-len(outbit)
    return max(0,infoLoss)
def energy_loss(infoLoss):
    ELoss=infoLoss*kB*t*math.log(2)
    return max(0,ELoss)

lossInfo_ir=info_loss(inbitir,outir)
lossEnergy_ir=energy_loss(lossInfo_ir)
print(f"Irreversible(AND):loss {lossInfo_ir} bit and {lossEnergy_ir} J")

lossInfo_r=info_loss(inbitr,outr)
lossEnergy_r=energy_loss(lossInfo_r)
print(f"Reversible(TOF):loss {lossInfo_r} bit and {lossEnergy_r} J")
