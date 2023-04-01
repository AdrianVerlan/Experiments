import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
image_folder = os.path.expanduser("~/Pictures")

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

for file_name in os.listdir(download_folder):
    if file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        file_path= os.path.join(download_folder,file_name)
        shutil.move(file_path, image_folder)