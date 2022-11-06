from time import sleep
from e_drone.drone import*
from e_drone.protocol import*

def eventTrim(trim):
    print("{0},{1},{2},{3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))

def eventMotion(motion):
    print("eventMotion()")
    print("- Accel: {0:5},{1:5}, {2:5}".format(motion.accelX. motion.accelY,motion.accelZ))
    print("- Gyro: {0:5},{1:5}, {2:5}".format(motion.gygoRoll. motion.gyroPitch,motion.gyroYaw))
    print("- Angle: {0:5},{1:5}, {2:5}".format(motion.angleRoll. motion.anglePitch,motion.angleYaw))

if __name__ == '__main__':  # <-name 변수

    drone = Drone()
    drone.open("com 5")  # <- 사용자 port
        
    drone.setEventHandler(DataType.Trim, eventTrim)
    drone.setEventHandler(DataType.Motion, eventMotion)

    drone.sendClearBias()  # <- Accel, Gyro,Anglw, Trim Reset
    sleep(0.01)

    drone.sendRequest(DeviceType.Drone, DataType.Trim)
    sleep(0.1)                                             # <- 변경 사항을 확인
    drone.sendRequest(DeviceType.Drone, DataType.Motion)
    sleep(0.1)

    drone.close()
