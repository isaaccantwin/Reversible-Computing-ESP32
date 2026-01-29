from machine import Pin
import time

led_a=Pin(5, Pin.OUT)
led_b=Pin(6, Pin.OUT)
led_c=Pin(7, Pin.OUT)

def display_state(states):
    led_a.value(states[0])
    led_b.value(states[1])
    led_c.value(states[2])
    
a=int(input("a:1 or 0:"))
b=int(input("b:1 or 0:"))
c=int(input("c:1 or 0:"))
out_c=(a&b)^c
display_state((a,b,out_c))
time.sleep(1.5)
