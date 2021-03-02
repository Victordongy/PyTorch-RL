from os import path
import matplotlib.pyplot as plt 
import numpy as np 

def assets_dir():
    return path.abspath(path.join(path.dirname(path.abspath(__file__)), '../assets'))

def plotting(logs:dict, algo:str) : 
    fig, ax = plt.subplots()

    scores = logs['avg_reward']
    std = logs['std']
    epochs = len(scores) 

    plt.plot(scores)
    ax.plot(epochs, scores, label=algo)
    ax.fill_between(epochs, scores-std, scores+std ,alpha=0.3, facecolor=clrs[i])