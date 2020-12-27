#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

np.random.seed(0)


car_data = car_data = [[0,0] for _ in range(100)]
                                                    #인덱스가 작을수록 뒤에 있는 차, [위치, 속도]
tLight_data = [[250, 0, 0],[500, 0, 0],[750, 0, 0],[1000, 0, 0],[1250, 0, 0],[1500, 0, 0],[1750, 0, 0]]
                                                    #[loc, state(초록불 = 0, 빨간불 = 1), delay_log(빨간불이었던 타임스텝 - 누적X)]

class Env():
    def __init__(self) :                            #상수 설정
        super(Env, self).__init__()
        self.troll = 0.5
        self.num = 100
        self.len = 2000
        self.safe_dis = 5
        self.max_speed = 3

    def step(self, action) :                        #타임스텝 진행하고 보상 결정
        done = False
        
        for i in range(self.num-1) :                 
            dis = car_data[i][0] - car_data[i+1][0] #차의 속도 결정
            if dis > self.safe_dis :
                if car_data[i][1] < self.max.speed :
                    car_data[i][1] += 1
            elif dis == self.safe_dis :
                if car_data[i][1] < car_data[i+1] :
                    car_data[i][1] += 1
                elif car_data[i][1] > car_data[i][1] :
                    car_data[i][1] -= 1    
            elif dis == 0 :
                car_data[i][1] = 0
            else :
                if car_data[i][1] > car_data[i+1][1] :
                    car_data[i][1] -= 1
                elif car_data[i][1] < car_data[i+1][1] :
                    car_data[i][1] += 1

            if np.random.rand() <= self.troll :     #인공적으로 도로 정체 형성
                car_data[i][1] = 1

            for L in range(5) :                     #신호등 보고 행동
                if tLight_data[L][0] - 3 <= car_data[i][0] <= tLight_data[L][0] :
                    if tLight_data[L][1] == 1 :
                        if car_data[i][0] == tLight_data[L][0] :
                            car_data[i][0] = 0
                        elif tLight_data[L][0] + 1 <= car_data[i][0] <= tLight_data[L][0] :
                            if car_data[i][1] > 1 :
                                car_data[i][1] = 1
                        else :
                            if car_data[i][1] == 3 :
                                car_data[i][1] = 2
                                

        R = 0                                       #reward
        for i in range(self.num) :
            if car_data[i][1] == 3 : 
                R += 1
            elif car_data[i][1] == 2 : 
                pass
            elif car_data[i][1] == 1 :
                R -= 1
            elif car_data[i][1] == 0 :
                R -= 4

        for i in range(len(tLight_data)) :
            R += tLight_data[i][2]

        #에피소드 종료 여부 결정
        if car_data[0][0] >= self.len :
            done = True

        for i in range(-1, -1*self.num, -1) :            #다른 차가 도로 벗어났을 때 무시하기 위함
            if car_data[i][0] >= self.len :
                car_data.pop(i)
                self.num -= 1
            else :
                break

        for i in range(self.num) :                       #속도 따라 차 움직인다
            car_data[i][0] += car_data[i][1]

        next_state = [car_data[0][0], car_data[self.num//4][0], car_data[self.num//2][0], car_data[(self.num*3)//4][0], car_data[self.num-1][0]]
        
        return next_state, R, done

    def act(self, action) :                         #action 따라 움직인다
        for i in range(len(tLight_data)):
            if tLight_Data[i][1] == 1 :
                tLight_Data[i][2] += 1
                
            tLight_Data[i][1] = action[i]

    def reset(self) :                               #환경 초기화
        for i in range(self.num) :
            car_data[i][0] = i * 3
            car_data[i][1] = self.max_speed
        tLight_Data = [[250, 0, 0],[500, 0, 0],[750, 0, 0],[1000, 0, 0],[1250, 0, 0],[1500, 0, 0],[1750, 0, 0]]

        return car_data[0][0], car_data[self.num//4][0], car_data[self.num//2][0], car_data[(self.num*3)//4][0], car_data[self.num-1][0]

    def see_state(self) :
        for i in range(len(tLight_data)) :
            print(tLight_data[i][1], end = ' ')
