from gpiozero import Servo

class servo:
    servo = Servo(0)

    def set_angle(angle):
        servo.set_angle(angle= angle)
