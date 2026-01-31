from machine import Pin
import time
import math

kB=1.38e-23
T=300

tatalEsave=0

leds=[Pin(5,Pin.OUT),Pin(6,Pin.OUT),Pin(7,Pin.OUT)]

def display(state):
    for i in range(len(leds)):
        if i < len(state):
            leds[i].value(state[i])
        else:
            leds[i].value(0)

def toffoli(a,b,c):
    return a,b,(a&b)^c

def info_loss(inbit,outbit):
    infoLoss=len(inbit)-len(outbit)
    return max(0,infoLoss)

def energy_loss(infoLoss):
    ELoss=infoLoss*kB*T*math.log(2)
    return max(0,ELoss)

def AND (ina,inb):
    inir=(ina,inb)
    outir=(ina&inb,)
    LossInfo=info_loss(inir,outir)
    return energy_loss(LossInfo)

def back(ina,inb,inc):
    global tatalEsave
    inbit=(ina,inb,inc)
    oua=ina
    oub=inb
    ouc=toffoli(ina,inb,inc)
    print(ouc)
    display(ouc)
    infoLoss=info_loss(inbit,ouc)
    rEloss=energy_loss(infoLoss)
    time.sleep(0.3)
    ooua=oua
    ooub=oub
    oouc=toffoli(oua,oub,ouc[2])
    print(oouc)
    display(oouc)
    print(f"energy loss:{rEloss}")
    irEloss=AND(ina,inb)
    Esave=irEloss-rEloss
    tatalEsave+=Esave
    if ooua==ina:
        if ooub==inb:
            if oouc[2]==inc:
               print("reversible")
            else:
               print("irreversible")
    time.sleep(0.3)

#a=int(input("outputA:"))
#b=int(input("outputB:"))
#c=int(input("outputC:"))
for a in range(2):
    for b in range(2):
        for c in range(2):
            back(a,b,c)

print(f"tatal energy sav:{tatalEsave}")

totalBrainIr=1e25*kB*T*math.log(2)
waterBoilE=4184*80

print(f"ir burns {totalBrainIr/waterBoilE}L water per sec")
