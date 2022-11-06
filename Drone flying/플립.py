from time import sleep
from e_drone.drone import*
from e_drone.protocol import*

if __name__ == '__main__':

        drone = Drone()
        drone.open("com5")
        print("TakeOff")
        drone.sendTakeOff()  #이륙명령
        sleep(0.01)



        print("Hovering")
        drone.sendControlWhile(0,0,0,0,5000) #컨트롤은 0인 상태로 5초 정지

        print("Flip")
        drone.sendFlightEvent(FlightEvent.FlipLeft) #전진 명령(피치 50%)을 전송 후 2초 전진
        sleep(1)
        print("Hovering")
        drone.sendControlWhile(0,0,0,0,3000) #컨트롤은 0인 상태로 5초 정지
        print("Landing")
        drone.sendLanding() # 안전하게 착륙하기 위해 landing 함수는 2번정도 호출함
        sleep(0.01)
        drone.sendLanding()
        sleep(0.01)

        drone.close()

