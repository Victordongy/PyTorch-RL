from os import path
import matplotlib.pyplot as plt 
import numpy as np 
import os 
import glob 
import pandas as pd 

def assets_dir():
    return path.abspath(path.join(path.dirname(path.abspath(__file__)), '../assets'))

def plotting(logs:dict, algo:str) : 
    fig, ax = plt.subplots()

    scores = logs['avg_reward']
    std = logs['std']
    epochs = len(scores) 

    plt.plot(scores)
    ax.plot(epochs, scores, label=algo)
    ax.fill_between(epochs, scores-std, scores+std ,alpha=0.3)

def compare(path) : 
    extension = '.csv'
    os.chdir(path)
    logs_to_compare = glob.glob('*.{}'.format(extension))

    for log in logs_to_compare : 
        data = pd.read_csv(log).to_dict() 
        algo = os.path.splitext(data)[0]
        plotting(data, algo)

    
