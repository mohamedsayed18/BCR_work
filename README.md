# BCR_work
Behavioural and Cognitive Robotics course work. based on this [repo](https://github.com/snolfi/evorobotpy)<br/>

### Exercise 2:
in exercise two we built a simple neural network to solve the cartpoleV0 environment(can be also applied to other environments). in the beginning i was having problems with the steady state evolutionary strategy but i mange to solve it.<br/>
Does the robot solve it every time? i think this depend on the inital values of the parameters if they are close to the solution or not and also if they are local minimum or not<br/>
i tried changing the generation i relized that it has great effect no the reward the higher number of generations the higher the reward

### Exercise 3:
this exercise is about getting used evorobotpy library which help us to evolve robot in different environments. i tried this lib with the acrobot environment.<br/>
From the [documentation](https://github.com/openai/gym/blob/master/gym/envs/classic_control/acrobot.py)<br/>
**The actions** is either applying +1, 0 or -1 torque on the joint between the two pendulum links.<br/>
**The state** consists of the sin() and cos() of the two rotational joint angles and the joint angular velocities.<br/>
[cos(theta1) sin(theta1) cos(theta2) sin(theta2) thetaDot1 thetaDot2].<br/>

Let's run different seeds using this command
```python
python3 ../bin/es.py -f acrobot.ini -s 11
```
Where s parameter represent the seed number

Plot performance across generations  
```python
python3 ../bin/plotstat.py
```
This command ```python3 ../bin/plotstat.py``` should be run while inside xacrobot directory<br/>
Error when running ```python3 ../bin/plotave.py```

Then i observed the behavior of the evolved robots
```python
python3 ../bin/es.py -f acrobot.ini -t bestgS11.npy
```

### Exercise 4
Compare the behavior of robots evolved with the original and revised reward functions
I tried with hopper. first I replaced the original files in 
```/usr/local/lib/pyс.5/dist-packages/pybullet_envs/```
with the modified version in 
```/opt/evorobotpy/pybullet/gym_locomotion_envs.py```
then I evolved my robot using this command 
```python3 ../bin/es.py -f hopper.ini -s 11```
then I watched the result of the original and the modified using this commands respectively
```python3 ../bin/es.py -f hopper.ini -t bestgS9.npy```<br/>
```python3 ../bin/es.py -f hopper.ini -t bestgS11.npy```<br/>
From the simulation the robot evolved with the original do more movements to locomote and move forward. On the other side the robot evolved with the modified files it locomote to the goal but it didn't make use of most of the joints he have and this is obvious from the gym_locomotion_envs.py files. In the original we can see that reward in the step method is the summation of the (progress, electric_torque, feet_collison, joint_limits). while in the modified version is only the progress. So I can say that in evoloutionary stratigies we only care about the progress and locomotion to the goal while reinforcement we also care about other factors and give penalites if the robot exceeded its limits for example (electric_torque, joint_limits)

### Exercise 5
The balance bot environment was created with the proposed structure and files. I copied the balancebot_simple.xml to the ```balance-bot/balance_bot/envs/```. I also created a balance_bot.ini which specify some parameters like number of episodes, trials, hidden layers ...etc. I added the import statment to```import balance_bot``` es.py<br/>
Finally I evolved the robot using this command<br/>
```python3 ../bin/es.py -f balance_bot.ini -s 11```

### Exercise 6
Run 10 replications
I executed 10 applicaitons using different seeds using this command
```python3 ../bin/es.py -f ErDiscrim.ini -s 1``` where 1 is the seed number<br/>
After running the experiments. I can say that the evolved robots can be catogrized into two groups. First group which do an oscillation (moving back and forth) at the obstacle. Second group find the obstacle and keep rotating near it.<br/> 

I used a feed-forward neural architecture by changing the parameter architecture to zero<br/>
The evolution processes was faster (maybe because we don't have any kind of memorey just feedforward). The evolved robot didn't succed in every trial (expected as the robot don't have a memory to help him to get better rewards). Having a look at the reward inside discrim.cpp we can see that the robot is reward by 1 as long as he is close to the object.