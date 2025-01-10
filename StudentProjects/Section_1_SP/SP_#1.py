#Project Description
    # How to rename files with python, and classifying it by number of words and the day of the week.
import os
from datetime import datetime

directory = 'files'
filenames = os.listdir(directory)
for filename in filenames:
    filepath = os.path.join(directory, filename)
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_filename = f'{filename[:-4]}-{current_date}.txt'
    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    print(f"Renamed {filename} to {new_filename}")
print("File renaming completed!")
     
