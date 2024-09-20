#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
speaker = ev3.speaker

colorsensor = ColorSensor(Port.S1)
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
drivebase = DriveBase(left_motor, right_motor, 55, 90)

lastcolor = Color

speaker.set_speech_options('en', 'f1', 200, 50)
speaker.set_volume(100)
speaker.say("Initialized. Starting program.")
forward = True

while True:
    
    if forward:
        drivebase.drive(-50, 0)
    else:
        drivebase.drive(50, 0)

    if colorsensor.color() is not lastcolor:
        lastcolor = colorsensor.color()
        ev3.light.on(lastcolor)
        wait(10)

    if lastcolor is Color.RED:
        forward = False

    if lastcolor is Color.BLACK:
        forward = True