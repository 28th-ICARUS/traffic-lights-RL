#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time



troll, num, road_len, interval, dis, speed = 0.02, 100, 2000, 250, 5, 3

car_data = [[0,0] for _ in range(100)]          #인덱스가 작을수록 앞에 있는 차, [위치, 속도]

car_state = [0,0,0,0,0]         #일종의 대푯값 => 0,25,50,75,99번 인덱스 차량 위치

tLight_Data = [[250, 0, 0],[500, 0, 0],[750, 0, 0],[1000, 0, 0],[1250, 0, 0],[1500, 0, 0],[1750, 0, 0]]
                                #[loc, state(초록불 = 0, 빨간불 = 1), delay_log(빨간불이었던 타임스텝 - 누적X)]

    
class Env():
    def __init__(self) :                            #상수 설정
        super(Env, self).__init__()
        self.troll = troll
        self.num = num
        self.len = road_len
        self.interval = interval
        self.safe_dis = dis
        self.speedMax = speed

    def step(self, action) :                        #타임스텝 진행하고 보상 결정
        #기존의 carSpeed 파트
        for i in range(car_num-1):
            dis = car_data[i][0] - car_data[i+1][0]
            if dis > self.safe_dis :
                if car_data[i][1] < self.speedMax :
                    car_data[i][1] += 1
                else : 
                    pass
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

            if randint(1,1000) <= self.troll * 1000 :
                car_data[i][1] = 1

        #기존의 reward, tLight_reward 부분
        R = 0
        for i in range(self.num) :
            if car_data[i][1] == 3 : 
                R += 1
            elif car_data[i][1] == 2 : 
                pass
            elif car_data[i][1] == 1 :
                R -= 1
            elif car_data[i][1] == 0 :
                R -= 4
                
            R += tLight_data[i][2]

        #에피소드 종료 여부 결정
        if car_data[0][0] >= 2000 :
            done = True
        else :
            done = False

        #기존의 carMove 부분
        for i in range(car_num) :
            car_data[i][1] += car_data[i][0]

        #에피소드 종료 여부와 carMove 부분 서로 바꿔야 하나?
        
        return next_state, R, done

    def act(self, action) :                         #action 따라 움직인다
        for i in range(7):
            if tLight_Data[i][1] == 1 :
                tLight_Data[i][2] += 1
                
            tLight_Data[i][1] = action[i]

    def reset(self) :                               #환경 초기화
        self.update()
        car_data = [[0,0]*num]
        tLight_Data = [[250, 0, 0],[500, 0, 0],[750, 0, 0],[1000, 0, 0],[1250, 0, 0],[1500, 0, 0],[1750, 0, 0]]

    def render(self):                               #   ???
        time.sleep(0.02)
        self.update()
        
    def visualization(self):                        #state를 비주얼화한다
        n=0
        for i in range(self.len):
            if car_data[n][0]==i :
                plt.bar(i, 3-car_data[n][1], width=0.1)
                n=n+1
            else:
                plt.bar(i, 0, width=0.1)
        
        plt.ylim(0, 3.5)
        plt.xlabel("Road")
        plt.ylabel("Degree of congetion(Vmax-Vcar)")
        plt.title("Visualization")
        plt.show()

#car_state = [car_data[0][0], car_data[25][0], car_data[50][0], car_data[75][0], car_data[99][0]]
