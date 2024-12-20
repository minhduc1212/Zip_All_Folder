import os
import shutil
import zipfile

def zip_folders_in_directory(directory, new_directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            zip_filename = f"{item}.zip"
            with zipfile.ZipFile(f'{new_directory}/{zip_filename}', 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, item_path)
                        zipf.write(file_path, arcname)
            print(f"Added zip file: {item_path} to {new_directory}/{zip_filename}")
        else:
            new_path = os.path.join(new_directory, item)
            shutil.copy(item_path, new_path)
            print('Moved file:', item_path, 'to', new_path)
            

if __name__ == "__main__":
    directory = "E:/Test"
    new_directory = "E:/test 2"
    zip_folders_in_directory(directory=directory, new_directory=new_directory)