#!/usr/bin/env python3

import time
import math

from Mulebot import MuleBot

bot = MuleBot()

#print("Duration: ", bot.dcMotorPWMDurationLeft)
bot.setMotorsDirection('f')

bot.motorSpeed(3.0, 3.0)

for i in range(5):
#                  time.sleep(1.5)

                  print(" ")
                  print(" ")
                  angle_rad = math.radians(i / 3)

                  bot.lidarNav_turn(angle_rad)

                  print("sleep")
                  time.sleep(5)
#                  bot.motorSpeed(0, 0)
