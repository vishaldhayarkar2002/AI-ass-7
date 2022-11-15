
import numpy as np

def act_func(y):
    if y > 0:
        y = 1
    elif y <= 0:
        y = 0
    return y

W = np.array([0.3, -0.2])

b = 0.4

def p_algo(x):
    # y = w1x1 + w2x2 + b
    # In NOR and NAND we will be adding bias value 
    y = np.dot(W, x) + b
    # y = 1 if Wx+b > 0 else y = 0 
    y = act_func(y)
    return y

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

print('NOR Logic: \n')
print(f'x1 = 0 and x2 = 0 => y = {p_algo(input1)}')
print(f'x1 = 0 and x2 = 1 => y = {p_algo(input2)}')
print(f'x1 = 1 and x2 = 0 => y = {p_algo(input3)}')
print(f'x1 = 1 and x2 = 1 => y = {p_algo(input4)}')
