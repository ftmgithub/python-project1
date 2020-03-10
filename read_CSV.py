import pandas as pd

df = pd.read_csv('C:/Users/fatemeh/Desktop/py.project/log2.txt', names= ['Data'])

pd.set_option('display.max_colwidth', None)

print(df)
