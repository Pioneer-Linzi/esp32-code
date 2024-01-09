from machine import Pin,Timer
from hcsr04 import HCSR04

'''
超声波测距
'''

hcsr = HCSR04(trigger_pin=16, echo_pin=17)

def get_distance(timer):
     distance = hcsr.distance_cm()
     print(distance)


if __name__ == '__main__':
    time0=Timer(0)  #创建time0定时器对象
    time0.init(period=1000,mode=Timer.PERIODIC,callback=get_distance)

        
       
