'''
数字电路模拟虚拟电路
'''
from machine import Pin, PWM, Timer

pwm = PWM(Pin(16), freq=50, duty=25)

duty = 0
ledstatus = True

def time0_irq(timer):   
    global duty
    global ledstatus
    print(duty,ledstatus)
    if duty >= 999 or duty<=0:
        ledstatus = not ledstatus
    if ledstatus:
        duty = duty - 100
        pwm.duty(duty)
    else:
        duty = duty + 100
        pwm.duty(duty)

def pwm_demo():
     time0=Timer(0)  #创建time0定时器对象
     time0.init(period=300,mode=Timer.PERIODIC,callback=time0_irq)

if __name__ == '__main__':
    pwm_demo()

