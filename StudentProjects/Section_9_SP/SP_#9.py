import os
import dropbox
import dotenv
 
dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
 
d = dropbox.Dropbox(ACCESS_TOKEN)

local_directory = "files"

for filename in os.listdir(local_directory):
    
    local_filepath = os.path.join(local_directory, filename)
 
    if os.path.isfile(local_filepath):
        with open(local_filepath, 'rb') as file:
            content = file.read()
            dropbox_path = f'/{filename}'
            d.files_upload(content, dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
            print(f'File {filename} uploaded successfully!')