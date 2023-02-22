#创建环境
import gym
import highway_env
from matplotlib import pyplot as plt
# pycharm不行，jupyter notebook可以用 %matplotlib inline，可直接在你的console里面生成图像,plt.show()

#配置环境
import pprint

# step1：create higwayenv
# env=gym.make('highway-v0')
# env.reset()
# for _ in range(10): #说明不在意叫什么，所以用_
#     action=env.action_type.actions_indexes["IDLE"]
#     obs,reward,done,info=env.step(action)
#     env.render()
# # 基于pygame开发
# plt.imshow(env.render(mode="rgb_array"))
# plt.show()

# step2: configure env
# env=gym.make("highway-v0")
# #   查看配置
# pprint.pprint(env.config)
# #   改配置
# env.config['lanes_count']=2
# # The environment must be reset() for the change of configuration to be effective.
# env.reset()
# plt.imshow(env.render(mode="rgb_array"))
# plt.show()

# step3: train an agent
