import os
import zipfile

def zip_folders_in_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            zip_filename = f"{item}.zip"
            with zipfile.ZipFile(f'{directory}/{zip_filename}', 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, item_path)
                        zipf.write(file_path, arcname)

if __name__ == "__main__":
    target_directory = "D:/test"
    zip_folders_in_directory(directory=target_directory)