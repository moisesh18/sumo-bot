#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from  ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
import time
import threading

sound = Sound()
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

def toAttack (speed=100,rotations=6):
    attack.on_for_rotations(SpeedPercent(-speed), rotations)
    attack.on_for_rotations(SpeedPercent(speed), rotations) #si es positivo el speed, baja

def pursue ():
    return proximity.distance_centimeters

def walk (speed=40):
    tank.on_for_rotations(SpeedPercent(speed),SpeedPercent(speed), 0.3)

def backWalk (speed=100,rotations=2.5):
    tank.on_for_rotations(SpeedPercent(-speed),SpeedPercent(-speed), rotations)

def Main ():
    while True:
        print (pursue())
        print (color.color_name)
        if color.color_name != "Black":
            if pursue()<15.0:
                print ("en ataque locooo...")
                walk(100)
            elif pursue()<30.0:
                print ("buscando atacar")
                walk(40)
            else:
                print ("no encuentra nada...")
                while color.color_name != "Black":
                    walk()
                if pursue()<30.0:
                    turnLeft(100,1.5)
                else:
                    turnRight(100,1.5)
        else:
            print ("de regreso....")
            backWalk()

Main()
