import machine
import time
green_led = machine.Pin(0, machine.Pin.OUT)
b_1 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
red_led = machine.Pin(2, machine.Pin.OUT)
b_2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

correct_combo = [1, 2, 1, 2]
user_combo = []


while True:
    if b_1.value() == 0:
        user_combo.append(1)
        time.sleep(0.3)
        
    if b_2.value() == 0:
        user_combo.append(2)
        time.sleep(0.3)
        
    if len(correct_combo) == len(user_combo):
        if correct_combo == user_combo:
            green_led.value(1)
            time.sleep(1)
            green_led.value(0)
            
        else:
            red_led.value(1)
            time.sleep(1)
            red_led.value(0)
        user_combo = []   
        
            
