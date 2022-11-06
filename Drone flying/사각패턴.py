from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':

        drone = Drone()
        drone.open("com5")  
        print("TakeOff")
        drone.sendTakeOff()
        sleep(0.01)

        print("Hovering")
        drone.sendControlWhile(0,0,0,0,4000)

        print("Go Start")
        drone.sendControlWhile(0, 50, 0, 0, 1000) #1초 동안 전진 (피치 50%)
        drone.sendControlWhile(0, 0, 0, 0, 1000)  # 1초 동안 전진을 멈춤(피치 0%)
        drone.sendControlWhile(50, 0, 0, 0, 1000) #1초 동안 우측으로 이동(roll 50%)
        drone.sendControlWhile(0, 0, 0, 0, 1000)  # 1초 동안 우측 이동을 멈춤(roll 0%)
        drone.sendControlWhile(0, -50, 0, 0, 1000) # 1초 동안 후진시킴(pitch -50%)
        drone.sendControlWhile(0, 0, 0, 0, 1000)  #1초 동안 후진을 멈춤(pitch 0%)
        drone.sendControlWhile(-50, 0, 0, 0, 1000) # 1초 동안 좌측으로 이동시킴 (roll -50%)
        drone.sendControlWhile(0, 0, 0, 0, 1000) #1초 동안 좌측 이동을 멈춤(roll 0%)
        print("Go Stop")

        drone.sendLanding()
        sleep(0.01)
        drone.sendLanding()
        sleep(0.01)

        drone.close()
    
