#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import state


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
speaker = ev3.speaker
colorsensor = ColorSensor(Port.S1)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
top_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, 55, 90)

#state_machine = state.state_manager()
#state_machine.add_state("driving", drive_state())

class drive_state(state.state):
    def __init__(self, manager, robot, speed, angle):
        super(drive_state, self).__init__(manager, robot, speed, angle)

    def enter(self):
        self.robot.drive(self.speed, self.angle)

        super(drive_state, self).enter()

    def tick(self):
        if colorsensor.color() is Color.RED:
            self.manager.set_state("left_turn")

        super(drive_state, self).tick()

    def exit(self):
        self.robot.stop()
        super(drive_state, self).exit()

class turn_on_spot_state(state.state):
    def __init__(self, manager, robot, speed, angle):
        super(turn_on_spot_state, self).__init__(manager, robot, speed, angle)

    def enter(self):
        self.robot.turn(self.angle)

        super(turn_on_spot_state, self).enter()

    def tick(self):
        
        if self.robot.angle > self.angle:
            self.manager.set_state("driving")

        super(turn_on_spot_state, self).tick()

    def exit(self):
        self.robot.stop()
        super(turn_on_spot_state, self).exit()


state_machine = state.state_manager()
state_machine.add_state("driving", drive_state(state_machine, robot, 200, 0))
state_machine.add_state("left_turn", turn_on_spot_state(state_machine, robot, 0, 90))
state_machine.add_state("right_turn", turn_on_spot_state(state_machine, robot, 0, -90))
state_machine.set_state("driving")

ev3.speaker.beep()

while True:
    state_machine.tick()

ev3.speaker.beep()