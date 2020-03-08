import gym
import numpy as np
from collections import OrderedDict


def update(observation):
    observation.resize(ninputs, 1)
    z1 = np.dot(w1, observation) + b1
    a1 = np.tanh(z1)
    z2 = np.dot(w2,a1) + b2 
    a2 = np.tanh(z2)

    if(isinstance(env.action_space, gym.spaces.box.Box)):
        action = a2
    else:
        action = np.argmax(a2)
    
    return action


def run_epi(observation):
    global total_reward
    done = False
    while (not done):
        #env.render()
        action = update(observation)
        observation, reward, done, _ = env.step(action)
        total_reward += reward


env = gym.make('CartPole-v0')

pvariance = 0.1
ppvariance = 0.02


# the input and output
ninputs = env.observation_space.shape[0]
noutpus = env.action_space.n
nhidden = 5

# generate weights
w1 = np.random.randn(nhidden, ninputs) * pvariance
w2 = np.random.randn(noutpus, nhidden) * pvariance
b1 = np.zeros((nhidden,1))
b2 = np.zeros((noutpus,1))


no_episodes = 10
total_reward = 0
scores = {}#store the scores

def new_pop(d):
    global param
    l = []  # rank indicies of the dictionary
    # sort the values

    for k, v in sorted(d.items(), key=lambda item: item[1]):
       l.append(k)

    for i in range(1, len(l)//2):    # modifiy the parameters
      param[l[i]] = param[l[i+len(l)//2]] + np.random.randn(1, no_parmaters) * ppvariance


population = 4
no_parmaters = nhidden*ninputs + noutpus*nhidden + nhidden + noutpus # number of parameters
# initalize the parameters
param = np.random.randn(population, no_parmaters)
#print(param.shape)

generations = 100
first_layer = nhidden * ninputs
second_layer = noutpus * nhidden
# evolution
for _ in range(generations):
    for i in range(population):
        w1 = param[i, :first_layer].reshape((nhidden, ninputs))
        #print(w1.shape)
        w2 = param[i, first_layer:first_layer+second_layer].reshape((noutpus, nhidden))
        #print(w2.shape)
        b1 = param[i, first_layer+second_layer: first_layer+second_layer+nhidden].reshape((nhidden,1))
        #print(b1.shape)
        b2 = param[i, first_layer+second_layer+nhidden:].reshape((noutpus,1))
        #print(b2.shape)

        total_reward = 0
        # run for number of episodes
        for _ in range(no_episodes):
            observation = env.reset()
            run_epi(observation)
            #print(total_reward)
        
        scores[i] = total_reward
    print(max(scores.values()))
    new_pop(scores)


