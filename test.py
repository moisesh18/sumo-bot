#!/usr/bin/env python3
from  ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
import time
import threading

proximity = UltrasonicSensor()


def pursue ():
    try:
        y = 100.0
        x = proximity.distance_centimeters 
        return x
    except:
        return y

def mainAttack():
    while True:
        if pursue()<15.0:
            #attack.on_for_rotations(SpeedPercent(speed), rotations) #si es positivo el speed, baja
            #attack.on_for_rotations(SpeedPercent(-speed), rotations)
            print ("ataque...")
    #time.sleep(1)

def mainWalk():
    while True:
        if 15.1<pursue()<40.0:
            #tank.on_for_rotations(SpeedPercent(-speed),SpeedPercent(-speed), rotations)
            print ("caminar...")
    #time.sleep(1)

# threads = list()
# t = threading.Thread(target=mainWalk)
# threads.append(t)
# t.start()
# t2 = threading.Thread(target=mainAttack)
# threads.append(t2)
# t2.start()
