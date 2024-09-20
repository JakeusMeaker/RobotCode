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
drivebase = DriveBase(left_motor, right_motor, 55.5, 104)

lastcolor = Color

speaker.set_speech_options('en', 'f1', 200, 50)
speaker.set_volume(100)
speaker.say("Initialized. Starting program.")

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 1.2

while True:
    
    deviation = colorsensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation

    drivebase.drive(DRIVE_SPEED, turn_rate)

    wait(10)
   