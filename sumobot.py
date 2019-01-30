#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.led import Leds


distancia = UltrasonicSensor()
color = ColorSensor()

llantaIzq = LargeMotor(OUTPUT_D)
llantaDer = LargeMotor(OUTPUT_A)

llantas = MoveTank(OUTPUT_A, OUTPUT_D)

rampa = Motor(OUTPUT_B)

def Caminar (Speed):
    while color.color_name != 'Black':
        llantas.on(Speed, Speed)
        if (distancia.distance_centimeters <= 8):
            Atacar(100, 5)
            print ("atacando")

def Detener ():
    llantas.off()

def Atras(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(-velocidad), rotaciones)

def GirarDerecha(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(velocidad), rotaciones)

def GirarIzquierda(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(velocidad),SpeedPercent(-velocidad), rotaciones)

def Buscar():
    
    Caminar(50)
    Detener()
    Atras(50, 1)
    GirarDerecha(50, 0.8)

def Atacar(speed, rotations):
    print ("esta atacando")
    rampa.on_for_rotations(SpeedPercent(-speed), rotations)

def Defender(speed, rotations):
    rampa.on_for_rotations(SpeedPercent(speed), rotations)

def Main():
    while True:
        Buscar()

Main()
Detener()