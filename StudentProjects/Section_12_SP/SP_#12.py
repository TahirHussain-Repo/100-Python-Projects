import pandas as pd
import os
import openpyxl

directory = 'excel_files'

filenames_2024 = [f for f in os.listdir(directory) if '2024' in f]
filenames_2025 = [f for f in os.listdir(directory) if '2025' in f]

filepaths_2024 = [os.path.join(directory, filename) for filename in filenames_2024]
filepaths_2025 = [os.path.join(directory, filename) for filename in filenames_2025]


dataframes_2024 = [pd.read_excel(filepath) for filepath in filepaths_2024]
merged_df_2024 = pd.concat(dataframes_2024, ignore_index=True)
output_file_path_2024 = os.path.join(directory, '2024.xlsx')
merged_df_2024.to_excel(output_file_path_2024, index=False)

dataframes_2025 = [pd.read_excel(filepath) for filepath in filepaths_2025]
merged_df_2025 = pd.concat(dataframes_2025, ignore_index=True)
output_file_path_2025 = os.path.join(directory, '2025.xlsx')
merged_df_2025.to_excel(output_file_path_2025, index=False)

print(merged_df_2024)
print("Merged data for 2024 saved to '2024.xlsx'.")
print("------------------------------------------------")
print("------------------------------------------------")
print("------------------------------------------------")
print(merged_df_2025)
print("Merged data for 2025 saved to '2025.xlsx'.")