from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

from time import sleep
from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':
    drone = Drone()
    drone.open("COM5")
    
    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0,0,0,0,4000)

    print("Right turn")
    drone.sendControlWhile(0,0,-30,0,600)   # 0.6초 시계방향으로 45도 정도 회전

    print("ZifZag")
    for i in range(4, 0, -1):
        drone.sendControlWhile(0,80,0,0,1000)
        drone.sendControlWhile(0,0,80,0,600)
        drone.sendControlWhile(0,80,0,0,1000)
        drone.sendControlWhile(0,0,-80,0,600)

    print("left turn")
    drone.sendControlWhile(0,0,30,0,600)  #0.6초 반시계방향으로 45도 정도 회전

    print("GO Stop")
    drone.sendControlWhile(0,0,0,0,1000)

    print("Landing")
    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()
    
    
