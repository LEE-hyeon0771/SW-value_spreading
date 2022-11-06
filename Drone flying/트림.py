from time import sleep
from e_drone.drone import*
from e_drone.protocol import*

def eventTrim(trim):
    print("{0},{1},{2},{3}".format(trim.roll, trim.pitch, trim.yaw, trim.throttle))
    
if __name__ == '__main__':   #name 변수

    drone = Drone()
    drone.open("com5")  # <- 사용자 port

    drone.setEventHandler(DataType.Trim, eventTrim) #<- 이벤트 핸들링 함수 등록
    drone.sendTrim(0,0,0,0)  # <- 트림 설정 변경(roll, pitch, yaw, throttle)
    sleep(0.01)
    drone.sendRequest(DeviceType.Drone, DataType.Trim) #<- 변경 사항을 확인
    sleep(0.1)

    print("TakeOff")
    drone.sendTakeOff()  #이륙명령
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0, 0, 0, 0, 5000) #컨트롤은 0인 상태로 5초 정지
    print("Go Stop")
    drone.sendControlWhile(0, 0, 0, 0, 1000) #1초 더 정지

    print("Landing")
    drone.sendLanding() # 안전하게 착륙하기 위해 landing 함수는 2번정도 함
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)
    drone.close()
