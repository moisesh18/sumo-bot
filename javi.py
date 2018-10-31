#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from  ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
import time
import threading

color = ColorSensor()
proximity = UltrasonicSensor()
attack = Motor(OUTPUT_B)
motor_left = LargeMotor(OUTPUT_A)
motor_right = LargeMotor(OUTPUT_D)
tank = MoveTank(OUTPUT_A, OUTPUT_D)

def turnLeft (speed=75,rotations=5):
    motor_left.on_for_rotations(SpeedPercent(speed), rotations)

def turnRight (speed=75,rotations=5):
    motor_right.on_for_rotations(SpeedPercent(speed), rotations)

def turnRight2 (speed=75,rotations=5):
    tank.on_for_rotations(SpeedPercent(speed),SpeedPercent(-speed), rotations)

def toAttack (speed=100,rotations=10):
    attack.on_for_rotations(SpeedPercent(-speed), rotations) #si es positivo el speed, baja

def pursue ():
    return proximity.distance_centimeters

def walk (speed=100,rotations=0.5):
    tank.on_for_rotations(SpeedPercent(-speed),SpeedPercent(-speed), rotations)

def Main ():
    print (pursue())
    print (color.color_name)
    while True:
        if pursue()<15.0:
            threads = list()
            t = threading.Thread(target=walk)
            threads.append(t)
            t2 = threading.Thread(target=toAttack)
            threads.append(t2)
            t.start()
            t2.start()
        elif pursue()<40.0:
            walk()
        else:
            walk()
            turnLeft(100,1)
    time.sleep(0.05)

#Main

def toAttack (speed=100,rotations=6):
    attack.on_for_rotations(SpeedPercent(-speed), rotations)
    attack.on_for_rotations(SpeedPercent(speed), rotations) #si es positivo el speed, baja

toAttack()