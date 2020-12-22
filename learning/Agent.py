import numpy as np
import random
import Enviroment
from collections import defaultdict



class Q_Agent :
    def __init__ (self, actions) :
        self.actions = actions
        self.step_size = 0.1
        self.discount_factor = 0.75
        self.epsilon = 0.75
        self.q_table = defaultdict(lambda : [0.0, 0.0, 0.0, 0.0, 0.0])
        
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
    return random.choice(max_idx_list)



if __name__ == "__main__" :
    env = Enviroment.Env()
    agent = Q_Agent(actions = list(range(5))
                    
    for episode in range(2000):
        state = env.tellState()

        while True:
            env.render()

            action = agent.get_action(state)
            next_state, reward, done = env.step(action)
            state = next_state
            update_Q(state, action, reward, next_state)

            if done :
                break
