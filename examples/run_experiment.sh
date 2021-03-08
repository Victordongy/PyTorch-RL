#!/bin/sh

python3 trpo_gym.py --num-threads 2 
python3 ppo_gym.py --num-threads 2 
python3 compare_algo.py 