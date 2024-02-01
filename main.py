import os
import shutil
import time

mods_folder = 'mods'

if not os.path.exists(mods_folder):
    os.makedirs(mods_folder)

prev_jars = set() 

while True:
    curr_jars = set()

    for root, dirs, files in os.walk('.'):
        if mods_folder not in root:
            for file in files:
                if file.endswith('.jar'):
                    file_path = os.path.join(root, file)  
                    curr_jars.add(file_path)

    new_jars = curr_jars - prev_jars
    
    for jar in new_jars:
        print(f'Found new .jar file: {jar}')
        choice = input(f'Move {jar} to mods folder? (Y/n) ')
        if choice.lower() == 'y':
            shutil.move(jar, mods_folder)
            
    prev_jars = curr_jars
    time.sleep(5)
