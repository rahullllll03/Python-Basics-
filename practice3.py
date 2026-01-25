import os

directory_path = '/user'

contents = os.listdir(directory_path)

for item in contents:
    print(item)