import os
import time

folder_path = './data/images'

while True:
  if not os.listdir(folder_path):
    print('Folder is empty')
  else:
    print('Folder is not empty')

  time.sleep(1)  # check every 1 second