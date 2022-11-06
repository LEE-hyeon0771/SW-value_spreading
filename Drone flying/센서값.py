import random
from time import sleep
from e_drone.drone import*
from e_drone.protocol import*

if __name__=='__main__':
    drone = Drone(True, True, True, True, True)
    drone.open('com5')
    for i in range(0, 10, 1):
        r = int(random.randint(0,255))
        g = int(random.randint(0,255))
        b = int(random.randint(0,255))
        dataArray = drone.sendLightDefaultColor(LightModeDrone.BodyDimming,1,r,g,b)
        print("{0} / {1}". format(i, covertByteArrayToString(dataArray)))
        sleep(2)
        drone.close()

'''
if __name__=='__main__':
    drone = Drone(True, True, True, True, True)
    drone.open('com5')
    while True:
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 255,0, 0)
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0)
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255)
        sleep(2)

    drone.close()
'''        
'''
def  eventMotion(motion):
    print("eventMotion()")
    print("- Accel: {0:5},{1:5}, {2:5}".format(motion.accelX. motion.accelY,motion.accelZ))
    print("- Gyro: {0:5},{1:5}, {2:5}".format(motion.gygoRoll. motion.gyroPitch,motion.gyroYaw))
    print("- Angle: {0:5},{1:5}, {2:5}".format(motion.angleRoll. motion.anglePitch,motion.angleYaw))
if __name__=='__main__':
    drone = Drone()
    drone.open('com5') # 장치관리자에서 포트 확인
    drone.setEventHandler(DataType.Motion, eventMotion)
    while True:
        drone.sendRequest(DeviceType.Drone, DataType.Motion)
        sleep(1)
    drone.close()
'''
