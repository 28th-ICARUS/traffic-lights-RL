import numpy as np
import Environment
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time



episodeLog, timeStepLog = [], []




class Q_Agent :
    def __init__ (self, actions) :
        self.actions = actions
        self.step_size = 0.1
        self.discount_factor = 0.75
        self.epsilon = 0.8                         
        self.q_table = defaultdict(lambda : [0,0])                              #큐함수 나타낸다
        
    def update_Q (self, state, action, reward, next_state) :                    #큐함수 업데이트
        state, next_state = str(state), str(next_state)
        q_1 = self.q_table[state][action]
        q_2 = reward + self.discount_factor * max(self.q_table[next_state])
        self.q_table[state][action] += self.step_size * (q_2 - q_1)          
        
    def get_action (self, state) :                                              #다음 행동 선택
        if np.random.rand() < self.epsilon :
            action = np.random.choice(self.actions)
        else :
            state = str(state)
            q_list = self.q_table[state]
            action = arg_max(q_list)
        return action



def arg_max (q_list) :                                                          
    max_idx_list = np.argwhere(q_list == np.amax(q_list))
    max_idx_list = max_idx_list.flatten().tolist()
    return np.random.choice(max_idx_list)                                       #최대 큐함수 가지는 행동 중 랜덤으로 하나 반환



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



if __name__ == "__main__" :
    env = Environment.Env()
    tLight1 = Q_Agent(actions = [0,0])
    tLight2 = Q_Agent(actions = [0,0])
    tLight3 = Q_Agent(actions = [0,0])
    tLight4 = Q_Agent(actions = [0,0])
    tLight5 = Q_Agent(actions = [0,0])
    tLight6 = Q_Agent(actions = [0,0])
    tLight7 = Q_Agent(actions = [0,0])
    timeStep = 1
    
    for episode in range(1,1001):
        state = env.reset()
        
        timeStep = 1
                    
        while True:
            print(state, episode, timeStep)
            env.see_state()
            
            action1 = tLight1.get_action(state)
            action2 = tLight2.get_action(state)
            action3 = tLight3.get_action(state)
            action4 = tLight4.get_action(state)
            action5 = tLight5.get_action(state)
            action6 = tLight6.get_action(state)
            action7 = tLight7.get_action(state)
            
            next_state, reward, done = env.step([action1, action2, action3, action4, action5, action6, action7])
            state = next_state
            
            tLight1.update_Q(state, action1, reward, next_state)
            tLight2.update_Q(state, action2, reward, next_state)
            tLight3.update_Q(state, action3, reward, next_state)
            tLight4.update_Q(state, action4, reward, next_state)
            tLight5.update_Q(state, action5, reward, next_state)
            tLight6.update_Q(state, action6, reward, next_state)
            tLight7.update_Q(state, action7, reward, next_state)

            if done :
                episodeLog.append(episode)
                timeStepLog.append(timeStep)
                break
            else :
                timeStep += 1
            time.sleep(0.02)
    print('finished!!!')
    print(episodeLog)
    print(timeStepLog)
