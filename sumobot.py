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

accion = " "
velocidad_llantas = 0

def Caminar(Speed):
    global velocidad_llantas
    velocidad_llantas = str(Speed)
    llantas.on(Speed, Speed)

def Detener():
    global accion
    accion = "Detenido"
    llantas.off()

def Atras(velocidad, rotaciones):
    global accion
    accion = "Reversa"
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(-velocidad), rotaciones)

def GirarDerecha(velocidad, rotaciones):
    global accion
    accion = "Girando derecha"
    llantas.on_for_rotations(SpeedPercent(-velocidad),SpeedPercent(velocidad), rotaciones)

def GirarIzquierda(velocidad, rotaciones):
    llantas.on_for_rotations(SpeedPercent(velocidad),SpeedPercent(-velocidad), rotaciones)

def Atacar(speed, rotations):
    global accion
    accion = "Atacando"
    Caminar(100)
    #rampa.on_for_rotations(SpeedPercent(-speed), rotations)

def Encontrado(speed):
    global accion
    accion = "Encontrado"
    Caminar(speed)

def Defender(speed, rotations):
    rampa.on_for_rotations(SpeedPercent(speed), rotations)

def Buscar():
    log = open("log.txt", "w")
    datos = " "
    global accion
    while color.color_name != 'Black':
        if (distancia.distance_centimeters <= 8):
            Atacar(100, 1)
        elif distancia.distance_centimeters <= 30:
            Encontrado(70)
        else:
            accion = "Buscando"
            Caminar(20)
        
        datos = velocidad_llantas + "," + color.color_name+ "," + str(distancia.distance_centimeters) + "," + accion
        log.write(datos + '\n')
        print(datos)
    Detener()
    Atras(50, 1)
    GirarDerecha(50, 0.5)
    log.write(datos + '\n')
    print(datos)
    log.close()
    Buscar()

#Buscar()
Detener()
#Defender(100,1)