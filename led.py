import random
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

# 드론 객체 생성
if __name__ == '__main__':
    drone = Drone(True, True, True, True, True, True)
    #     flagCheckBackground :bool = True, 
    #     flagShowErrorMessage:bool = True, 
    #     flagShowLogMessage:bool = True,
    #     flagShowTransferData:bool = True,
    #     flagShowReceiveData:bool = True,
    # )
    drone.open()

    # LED 색상 변경
    drone.sendLightDefaultColor(DeviceType.Drone, 255, 0, 0)
    sleep(2)
    drone.sendLightDefaultColor(DeviceType.Drone, 0, 255, 0)
    sleep(2)
    drone.sendLightDefaultColor(DeviceType.Drone, 0, 0, 255)
    sleep(2)

    drone.close()