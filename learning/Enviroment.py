#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# In[8]:


class Env() :
    def __init__(self, troll, num, road_len, interval, dis, speed):
        self.troll = troll
        self.num = num
        self.len = road_len
        self.interval = interval
        self.safe_dis = dis
        self.speedMax = speed
        
    def carSpeed(self, car_data):
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

    def carMove(self, car_data) :
        for i in range(car_num) :
            car_data[i][1] += car_data[i][0]
    
    def reward(self, car_data) :
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
                
        return R
    
    def tLight_reward(self, tLight_data) :
        #감소되는 보상 = 1/2(t)(t-1)  ==> 이전 버전. 12.02에 한 타임스텝마다 보상 들어오게 수정함
        R = 0
        for i in range(len(tLight_data)) :
            R += tLight_data[i][2] 
        return R

    def tellState(self) :
        self.update()
        time.sleep(0.5)
        car_state = [car_data[0][0], car_data[25][0], car_data[50][0], car_data[75][0], car_data[99][0]]
        return car_state

    def render():
        time.sleep(0.02)
        self.update()
        
    def visualization(self):
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


# In[9]:


def animate(i) :
    loc, speed = [], []
    for i in range(len(car_data)) :
        loc.append(car_data[i][0])
        speed.append(3 - car_data[i][1])
        
    graph.clear()
    graph.append(loc, speed)


# In[ ]:


troll, num, road_len, interval, dis, speed = 0.02, 100, 2000, 250, 5, 3

car_data = [[0,0]*num]           #인덱스가 작을수록 앞에 있는 차, [위치, 속도]
R = 0
tLight_data = [[0,0,0] * ((road_len // interval)-1)] 
#[loc, state(초록불 = 0, 빨간불 = 1), delay_log(빨간불이었던 타임스텝 - 누적X)]   
for i in range(len(tLight_data)) :
    tLight_data[i][0] = 250 * (i+1)

print('<상수>\n교통정체 발생율 = %.2f \n도로 길이 = %d \n신호등 간격 = %d \n차 개수 = %d \n차간 안전거리 = %d \n(차)최대 속도 = %d' %(troll, road_len, interval, num, dis, speed))
print('\n\n1을 누르면 상수를 변경하며, 1이 아닌 아무 문자를 입력하면 위 상수로 실행합니다',end = ('\t: '))
a = input()

if a == '1' :
    print('교통정체 발생율(현재 값 = %.2f)' %(troll), end = ('\t: '))
    troll_ = float(input())
    print('도로 길이(현재 값 = %d)' %(road_len), end = ('\t: '))
    road_len_ = int(input())
    print('신호등 간격(현재 값 = %d)' %(interval), end = ('\t: '))
    interval_ = int(input())
    print('차 대수(현재 값 = %d)' %(num), end = ('\t: '))
    num_ = int(input())
    print('차간 안전거리(현재 값 = %d)' %(dis), end = ('\t: '))
    dis_ = int(input())
    print('(차)최대 속도(현재 값 = %d)' %(speed), end = ('\t: '))
    speed_ = int(input())
    
    print('\n<바뀐 상수>')
    if troll == troll_ :
        print('교통정체 발생율 = %.2f' %(troll))
    else :
        print('교통정체 발생율 = %.2f  ==>  %.2f' %(troll, troll_))
        troll = troll_
    if road_len == road_len_ :
        print('도로 길이 = %d' %(road_len))
    else : 
        print('도로 길이 = %d  ==>  %d' %(road_len, road_len_))
        road_len = road_len_
    if interval == interval_ :
        print('신호등 간격 = %d' %(interval))
    else :
        print('신호등 간격 = %d  ==>  %d' %(interval, interval_))
        interval = interval_
    if num == num_ :
        print('차 대수 = %d' %(num))
    else :
        print('차 대수 = %d  ==>  %d' %(num, num_))
        num = num_
    if dis == dis_ :
        print('차간 안전거리 = %d' %(dis))
    else :
        print('차간 안전거리 = %d  ==>  %d' %(dis, dis_))
        dis = dis_
    if speed == speed_ :
        print('(차)최대 속도 = %d' %(speed))
    else :
        print('(차)최대 속도 = %d  ==>  %d' %(speed, speed_))
        speed = speed_

#fig = plt.figure()
#graph = fig.add_subplot(100, 10, 1)

#ani = animation.FuncAnimation(fig, animate, interval = 1000)
#plt.show()

#def constant :
    


# In[ ]:




