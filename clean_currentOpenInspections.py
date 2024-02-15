import pandas as pd

file_path = 'currentOpenInspections.csv'

df = pd.read(file_path)

pd.set_option('display.max_columns', None)
print(df.head(20))