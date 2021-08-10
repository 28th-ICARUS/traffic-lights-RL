import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

np.random.seed(0)

num = 100
car_data = [[0,0] for _ in range(num+1)]
                                                                                                                                    #인덱스가 작을수록 뒤에 있는 차, [위치, 속도]
tLight_data = [[500, 1, 0],[750, 1, 0],[1000, 1, 0],[1250, 1, 0],[1500, 1, 0],[1750, 1, 0]]
                                                                                                                                    #[loc, state(초록불 = 0, 빨간불 = 1), delay_log(빨간불이었던 타임스텝 - 누적X)]

class Env():
    def __init__(self) :                                                                                                            #상수 설정
        super(Env, self).__init__()
        self.troll = 0.6
        self.len = 2000
        self.max_speed = 3

    def step(self, action) :                                                                                                        #타임스텝 진행하고 보상 결정
        troll_list, next_state = [], []
        global car_data, tLight_data, num
        R = 0
        done = False

        for i in range(num) :
            for L in range(6) :                                                                                                     #신호등 보고 행동
                if tLight_data[L][0] - 3 <= car_data[i][0] and car_data[i][0] <= tLight_data[L][0] :
                    if tLight_data[L][1] == 1 :
                        car_data[i][1] = 0
        
            if np.random.rand() <= self.troll and car_data[i][1] > 0 :                                                              #인공적으로 도로 정체 형성
                car_data[i][1] -= 1
                troll_list.append(i+1)

        for i in range(num-1) :                 
            dis = car_data[i+1][0] - car_data[i][0] - 1                                                                             #차간 거리
            spd = car_data[i][1] - car_data[i+1][1]                                                                                 #상대속도

            if dis < spd :
                car_data[i][1] -= spd - dis
            elif dis > spd :
                car_data[i][1] += 1
            if car_data[i][1] < 0 :
                car_data[i][1] = 0
            if car_data[i][1] > 3 :
                car_data[i][1] = 3
                
        if(car_data[num-1][1] < 3) :
            car_data[num-1][1] += 1
                                                                     
        for i in range(num) :                                                                                                       #reward
            if car_data[i][1] == 3 : 
                R += 4
            elif car_data[i][1] == 2 : 
                R += 1
            elif car_data[i][1] == 1 :
                R -= 1
            elif car_data[i][1] == 0 :
                R -= 4

        for i in range(len(tLight_data)) :
            if tLight_data[i][2] > 0 :
                R -= (tLight_data[i][2] ** 2) // 2
            else :
                R += 20

        #에피소드 종료 여부 결정
        if car_data[0][0] >= self.len :
            done = True

        for i in range(num-1, -1, -1) :                                                                                             #다른 차가 도로 벗어났을 때 무시하기 위함
            if car_data[i][0] >= self.len :
                car_data.pop(i)
                num -= 1
            else :
                break

        for i in range(num) :                                                                                                       #속도 따라 차 움직인다
            car_data[i][0] += car_data[i][1]

        if(car_data) :
            next_state = [car_data[0][0], car_data[num//4][0], car_data[num//2][0], car_data[(num*3)//4][0], car_data[num-1][0]]
        return next_state, R, done

    def act(self, action) :                                                                                                         #action 따라 움직인다
        global tLight_data
        for i in range(len(tLight_data)):
            if tLight_data[i][1] == 0 :
                tLight_data[i][2] += 1
                
            tLight_data[i][1] = action[i]

    def reset(self) :                                                                                                               #환경 초기화
        global num, car_data, tLight_data
        num = 100
        car_data = [[i*3,3] for i in range(num)]
        tLight_Data = [[250, 0, 0],[500, 0, 0],[750, 0, 0],[1000, 0, 0],[1250, 0, 0],[1500, 0, 0],[1750, 0, 0]]
        return car_data[0][0], car_data[num//4][0], car_data[num//2][0], car_data[(num*3)//4][0], car_data[num-1][0]
