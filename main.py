import dc_motor
import camra_app
import servo

class main:
    
    camra = camra_app()
    servo = servo()
    dc_motor = dc_motor()

    screen_widt = camra.get_widt()
    screen_higt = camra.get_higt()

    def moveDc():
        if camra.get_y() > camra.get_y()/2:
            speed = camra.get_y() / 200 -1
            return speed
        if camra.get_y() < camra.get_y()/2:
            speed = camra.get_y() / 200 -1
            return speed * -1
    
    def moveServo():
        if camra.get_x() > camra.get_x()/2:
            angle = camra.get_x() * 180 / 250
            return angle
        if camra.get_x() <   camra.get_x()/2:
            angle = (camra.get_x() * 180 / 250) * -1
            return angle
            


if __name__ == "__main__":
    while True:
        camra = camra_app()
        servo = servo()
        dc_motor = dc_motor()
        main = main()

        camra.run()
        camra._capture_loop()

        dc_motor.set_angle(main.moveDc)
        servo.set_angle(main.moveServo)


        