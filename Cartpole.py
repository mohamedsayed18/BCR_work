"""cartpole V0"""
import gym
import numpy as np


class CartPole:
    def __init__(self):
        env = gym.make('CartPole-v0')
        self.total_reward = 0
        self.no_episodes = 10
        

        # Network
        # the input and output
        self.ninputs = env.observation_space.shape[0]
        self.noutpus = env.action_space.n
        self.nhidden = 5
        # generate weights
        self.w1 = np.random.randn(self.nhidden, self.ninputs) * pvariance
        self.w2 = np.random.randn(noutpus, nhidden) * pvariance
        self.b1 = np.zeros((nhidden,1))
        self.b2 = np.zeros((noutpus,1))

    def one_epi():
        observation = env.reset()
        done = False
        while (not done):   
            action = update(observation)
            observation, reward, self.done, _ = env.step(action)
            self.total_reward += reward
            #env.render()
            action = update(observation)
            observation, reward, self.done, _ = env.step(action)
            self.total_reward += reward

if __name__ == '__main__':
    cart = CartPole()
