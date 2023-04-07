import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    n = len(x)
    sample_mean = np.mean(x)
    sample_std = np.std(x, ddof=1)
    
    t_stat = (sample_mean - 300) / (sample_std / np.sqrt(n))
    p_value = t.sf(t_stat, n-1)
    
    return p_value < 0.08
