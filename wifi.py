import network
from machine import Timer


## wifi 连接
def connet_wifi(ssid,passwd):
    wlan =  network.WLAN(network.STA_IF)
    wlan.active(True)
  
    if not wlan.isconnected():
        print('network connecting')
        wlan.connect(ssid, passwd)
        while not wlan.isconnected():
            pass
    print('network conneted', wlan.ifconfig())
    return True


if __name__=="__main__":
    connet_wifi('nobug','15690798353')
   
        

        