import pandas as pd
import random as rd 


lst = ['robot'] * 10
lst += ['human'] * 10
rd.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
firstColumn = pd.DataFrame({'human' : data.replace(['human', 'robot'], [1, 0])['whoAmI']})
secondColumn = pd.DataFrame({'robot' : data.replace(['human', 'robot'], [0, 1])['whoAmI']})
print(pd.concat([firstColumn, secondColumn], axis=1))
