import numpy as np
import random
import Enviroment
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.animation as animation



episodeLog, timeStepLog = [], []




class Q_Agent :
    def __init__ (self, actions) :
        self.actions = actions
        self.step_size = 0.1
        self.discount_factor = 0.75
        self.epsilon = 0.8                          #0.8 / 2000 = 0.0004
        self.q_table = defaultdict(lambda : [[0,0] for _ in range(7)])      #큐함수 나타낸다
        
    def update_Q (self, state, action, reward, next_state) :
        state, next_state = str(state), str(next_state)
        q_1 = self.q_table[state][action]
        q_2 = reward + self.discount_factor * max(self.q_table[next_state])
        self.qtable[state][action] += self.step_size * (q_2 - q_1)
        
    def get_action (self, state) :
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
    return random.choice(max_idx_list)                      #최대 큐함수 가지는 행동 중 랜덤으로 하나 반환



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
    env = Enviroment.Env()
    agent = Q_Agent(actions = [0,0])
    timeStep = 1
    for episode in range(2000):
        state = env.reset()
        
        timeStep = 1
                    
        while True:
            env.render()

            action = agent.get_action(state)
            next_state, reward, done = env.step(action)
            state = next_state
            agent.update_Q(state, action, reward, next_state)

            if done :
                episodeLog.append(episode)
                timeStepLog.append(timeStep)
                print(episode, timeStep)
                print(episode + 1, timeStep)
                break
            else :
                timeStep += 1
