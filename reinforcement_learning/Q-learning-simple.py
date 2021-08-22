#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-16 00:29
"""

import numpy as np
import pandas as pd
import time


N_STATES = 6
ACTIONS = ['left', 'right']
EPSION = 0.9  # greedy police, 90%选择最优，10%随机选择
ALPHA = 0.1  # learning rate
GAMA = 0.9  # discount
MAX_EPISODES = 13
FRESH_TIME = 0.01  # 走一步花多长时间


def build_q_table(n_states, actions):
    # 初始化
    table = pd.DataFrame(np.zeros((n_states, len(actions))), columns=actions)

    return table


def choose_action(state, q_table):
    state_action_q = q_table.iloc[state, :]
    if np.random.uniform() > EPSION or state_action_q.all() == 0:
        action = np.random.choice(ACTIONS)
    else:
        action = state_action_q.argmax()
    return action


def get_env_feedback(S, A):
    if A == 'right':
        # 向右走到终点时，会得到奖励R=1，其余都是0
        if S == N_STATES - 2:  # T的前一个位置的下标
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminal = False
        update_env(S, episode, step_counter)
        while not is_terminal:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_real = R+GAMA*max(q_table.iloc[S_, :])
            else:
                # 此时已经没有未来的价值了，所以只有R
                q_real = R
                is_terminal = True
            new_q = q_predict + ALPHA * (q_real - q_predict)
            q_table.loc[S, A] = new_q
            S = S_
            update_env(S, episode, step_counter+1)
            step_counter += 1
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print(q_table)
