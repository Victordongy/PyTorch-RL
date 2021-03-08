import os 
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import * 

if __name__ == "__main__" : 
    compare_path = "."
    compare(compare_path)