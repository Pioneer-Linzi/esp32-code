
#导入Pin模块
from machine import Pin,Timer
from servo import Servo

my_servo = Servo(Pin(17))

angle = 0

def servo_angle(timer):
    global angle
    angle = angle + 45
    my_servo.write_angle(angle)


if __name__ == '__main__':
    time0=Timer(0)  #创建time0定时器对象
    time0.init(period=600,mode=Timer.PERIODIC,callback=servo_angle)
    

        
       