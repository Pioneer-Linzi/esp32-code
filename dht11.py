'''

温湿度传感器
'''



from machine import Pin,Timer
import dht

dht11 = dht.DHT11(Pin(16))

def get_temp(timer):
    dht11.measure()
    temp = dht11.temperature()
    humi = dht11.humidity()
    if temp == None:
        print("DHT11传感器检查失败")
    else:
        print("temp=%d度  humi=%dRH" %(temp,humi))
    



if __name__ == '__main__':
    time0=Timer(0)  #创建time0定时器对象
    time0.init(period=500,mode=Timer.PERIODIC,callback=get_temp)