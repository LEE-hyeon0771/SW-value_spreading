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
        drone.sendControlWhile(50,0,-60,25,5000) # 4초 시계방향으로 회전합니다.

        print("Go Stop")
        drone.sendControlWhile(0, 0, 0, 0, 1000)  #회전을 멈춰줍니다.

        print("Landing")
        drone.sendLanding() # 안전하게 착륙하기 위해 landing 함수는 2번정도 호출함
        sleep(0.01)
        drone.sendLanding()
        sleep(0.01)

        drone.close()
