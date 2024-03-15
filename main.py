import pandas as pd
import matplotlib.pyplot as plt

def pie_chart(df, column):
  count_list = []
  data = df[column].unique()
  data = list(data)
  for elem in data:
    count = 0
    for index in df[column]:
      if str(elem) == str(index):
        count += 1
    count_list.append(count)
  plt.title(column)
  plt.pie(count_list, labels = data, autopct = '%.2f')
  plt.show()


pd.set_option('display.max_columns', 10)

top_games = pd.read_excel('Top games.xlsx')

pie_chart(top_games, "Publisher")
