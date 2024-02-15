import pandas as pd
from fuzzywuzzy import fuzz

file_path = r"C:\Users\user\Desktop\Coursera\Data Engineering\Escape Data Engineering\Project 1\Project1Data\currentOpenInspections.csv"

df = pd.read_csv(file_path)

# Drop column RestaurantName
df = df.drop('RestaurantName', axis = 1)

# Convert 'LegalBusinessName' column to uppercase
df['LegalBusinessName'] = df['LegalBusinessName'].str.upper()

# Remove duplicates rows based on LegalBusinessName columns
df = df.drop_duplicates(subset=['LegalBusinessName'])

#column1_datatype = df['LegalBusinessName'].dtype
#print(column1_datatype)

# Function to calculate similarity ratio between two strings
df['LegalBusinessName'] = df['LegalBusinessName'].astype(str)

def similarity_ratio(str1, str2):
    return fuzz.token_set_ratio(str1, str2)

# Identify and remove duplicates based on similarity ratio
def remove_similar_duplicates(df, threshold=80):
    df_no_duplicates = df.copy()
    df_no_duplicates['cluster'] = df_no_duplicates['LegalBusinessName'].apply(lambda x: similarity_ratio(x, df_no_duplicates['LegalBusinessName'].max()))
    df_clean = df_no_duplicates[df_no_duplicates['cluster'] <= threshold]
    return df_clean

df_clean = remove_similar_duplicates(df)

pd.set_option('display.max_columns', None)
print(df_clean)

df_clean.to_csv(r"C:\Users\user\Desktop\Coursera\Data Engineering\Escape Data Engineering\Project 1\Project1Data\output.csv", index=False)