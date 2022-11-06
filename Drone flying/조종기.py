from time import sleep
from turtle import*
from e_drone.drone import*
from e_drone.protocol import*

def eventJoystick(joystick):
    goto(joystick.right.x, joystick.right.y)
if __name__=='__main__':
    drone = Drone()
    drone.open('com5') # 장치관리자에서 포트 확인
    drone.setEventHandler(DataType.Joystick, eventJoystick)
    drone.sendPing(DeviceType.Controller)


'''
def eventButton(button):
    print(button.button)
    if button.button == 1:
        circle(10)
    elif button.button == 2:
        circle(30)
    elif button.button == 4:
        circle(50)
    elif button.button == 8:
        circle(100)
if(__name__ =='__main__'):
    drone = Drone()
    drone.open('com5') # 장치관리자에서 포트 확인
    drone.setEventHandler(DataType.Button, eventButton)
    drone.sendPing(DeviceType.Controller)
'''    
'''
def eventJoystick(joystick):
    print(joystick.left.x, joystick.left.y, joystick.right.x, joystick.right.y)
if(__name__ =='__main__'):
    drone = Drone()
    drone.open('com5') # 장치관리자에서 포트 확인
    drone.setEventHandler(DataType.Joystick, eventJoystick)
    drone.sendPing(DeviceType.Controller)
    for i in range(10, 0, -1):
        print(i)
        sleep(1)
    drone.close()
'''

'''
def eventButton(button):  #버튼을 눌렀을 때
    print(button.button)

if __name__ == '__main__':
    drone = Drone()
    drone.open('com5') # 장치관리자에서 포트 확인
    drone.setEventHandler(DataType.Button, eventButton)
    drone.sendPing(DeviceType.Controller)

    print("버튼을 입력하세요")
    '''

