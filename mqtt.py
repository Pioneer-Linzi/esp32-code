from umqtt.simple import MQTTClient
from machine import Pin

from wifi import connet_wifi
import _thread
import time
# 全局配置WiFi连接参数
ssid = 'nobug'
password = '15690798353'
# 全局配置mqtt连接参数
mqttHost = "nas.linzi.tech" # MQTT代理服务器地址 这里使用公用的MQTT服务器做测试
mqttPort = 1883 #端口
keepalive = 60 #保活时间 单位s
clientID = 1
userName ="admin" #客户端的用户名
userPassword = 'Fhrs4235' #客户端用户密码

flagThread=True#设置一个标志位 默认设备上电只开启一个线程，设备断网重连后不开启新的线程
flagUploadData = False#设置一个标志位 判断是否断网 决定是否上传数据
deviceGetTime = 10#设备周期采集时间

master = Pin(16,Pin.OUT)




def mqtt_init():
    global mqttHost,mqttPort,keepalive,flagUploadData,flagThread,clientID,userName,userPassword,deviceGetTime
    #申明全局变量
    flagUploadData = True
    clientID = "esp32"
    deviceGetTime = 10 # 初始化设备采样周期

    client = MQTTClient(clientID, mqttHost, mqttPort, userName, userPassword, keepalive)  # 建立一个MQTT客户端
    client.set_callback(sub_cb)  # 设置回调函数
    client.connect()  # 建立连接
    client.subscribe(b"test1")  # 订阅EditTime主题
    
    if flagThread == True:
        _thread.start_new_thread(publish_readSensorData, (client,clientID))# 开启线程发布主题及内容
        flagThread=False

    while True:
        print('更新数据')
        client.check_msg()
        time.sleep(1)
  
        


#数据采集及主题发布函数
def publish_readSensorData(client, clientID):
        if flagUploadData == True:          
            # 发布主题，主题内容为获取到的传感器的数据
            client.publish(topic='test2',msg="Hello,I am ESP32!",qos=1)
            
        else:
            time.sleep(2)
            print('当前网络异常，停止上传数据')

# 主题订阅处理函数
def sub_cb(topic, msg):
    print(topic, msg)
    master.value(1)
    # 申明全局变量
    #global deviceGetTime
    #if topic.decode("utf-8") == "test1" :
        #data = json.loads(msg)
     #   print ("data['deviceGetTime']: ", json.loads(msg)['deviceGetTime'])
      #  deviceGetTime = json.loads(msg)['deviceGetTime']



if __name__ == '__main__':
    connet_wifi(ssid,password)
    print('初始化mqtt')
    mqtt_init()
   
   