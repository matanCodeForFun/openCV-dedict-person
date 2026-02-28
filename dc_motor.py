import math
from gpiozero import Motor

class dc_motor:

    Motor = Motor(forward= 5, backward= 6)

    def set_speed(speed):
        speed = math.max(-1, math.Min(1, speed))
        Motor.value = speed