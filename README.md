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


