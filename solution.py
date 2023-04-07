import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.08
    mean_x = np.mean(x)
    n = len(x)
    std_x = np.std(x, ddof=1)
    se = std_x / np.sqrt(n)
    t_statistic = (mean_x - 300) / se
    p_value = ttest_1samp(x, 300)[1] / 2
    return p_value < alpha
