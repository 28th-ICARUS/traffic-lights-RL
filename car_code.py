import time
import random

class god:

    def __init__(self):
        #self.road_data = road_data
        #self.car_data = car_data
        #self.car_len = car_len
        #self.traffic_rate = traffic_rate
        
    def roadTroll(self, car_speed):             
        for i in range(car_num):
            if random.randint(1,1000) <= 2:
                if car_speed[i] ==  0:
                    break
                else:
                    car_speed[i] -= 1
    
    def carGod(self):
        return

class car:
    
    def __init__(self):
        #self.road_data = road_data
        #self.car_data = car_data
        #self.car_len = car_len

    def carSpeed(self, car_loc, car_speed, road_data):
        for i in range(car_num):
            if road_data[car_loc[i] + 3] > 0:
                car_speed[i] = 2
            elif road_data[car_loc[i] + 2] > 0:
                car_speed[i] = 1
            elif road_data[car_loc[i] + 1] > 0:
                car_speed[i] = 1
            else:
                car_speed[i] = 0

    def carMove(self, car_loc, car_speed, road_data, car_num):          #car_loc와 road_data는 포인터처럼
        for i in range(car_num):
            road_data[car_loc[i]] -= 1
            car_loc[i] += car_speed[i]
            road_data[car_loc[i]] += 1
            
        

car_num = int(input())
roadData, carLoc, carSpeed = list(), list(), list()     #carLoc에서 인덱스가 작을수록 앞에 있는 차로 가정한다


