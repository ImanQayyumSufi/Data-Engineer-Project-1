import pandas as pd

file_path = 'currentOpenInspections.csv'

df = pd.read(file_path)

print(df.head(20))