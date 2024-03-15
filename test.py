import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 10)

top_games = pd.read_excel('Hackathon (2).xlsx')


data = top_games['Platform'].unique()
print(data)