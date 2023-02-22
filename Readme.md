# Project2: highway_env的RL决策

## 环境配置

1. anaconda prompt打开 

   `conda create -n RL python=3.9` 无python=3.9会找不到python.exe加不进pycharm interpreter

   `pip install pygame -i http://pypi.douban.com/simple --trusted-host pypi.douban.com` 

   `pip install highway-env`

   参考：

   https://highway-env.readthedocs.io/en/latest/installation.html

   https://github.com/eleurent/highway-env 上面有colab的jupyter notebook示例+注意参考这个文件夹`MARL_CAVs-main`（是期刊文献的代码参考实验+文章写法，先模仿）

   https://blog.csdn.net/weixin_46258429

2. 复制代码到DDPG.py运行

   `conda install pytorch torchvision torchaudio cpuonly -c pytorch`