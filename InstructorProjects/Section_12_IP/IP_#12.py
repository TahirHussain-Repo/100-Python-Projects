import pandas as pd
import openpyxl
import os

directory = 'excel_files'

filenames = os.listdir(directory)
filepaths = [os.path.join(directory, filename) for filename in filenames]

dataframes = [pd.read_excel(filepath) for filepath in filepaths]

merged_df = pd.concat(dataframes, ignore_index=True)

print(merged_df)

merged_df.to_excel('excel_files/merged.xlsx', index=False)