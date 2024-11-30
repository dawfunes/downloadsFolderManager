# This script is used to manage the downloads folder. It will move all the files to their respective folders based on their extensions or date of creation.
# Author: dawfunes
# Date: 30-11-2024

# imports
import os
import time

# Intro: 
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
font= fr"""{RED}
______                        _                    _      
|  _  \                      | |                  | |     
| | | | ___ __      __ _ __  | |  ___    __ _   __| | ___ 
| | | |/ _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` |/ __|
| |/ /| (_) |\ V  V / | | | || || (_) || (_| || (_| |\__ \
|___/  \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_||___/
______      _      _                                      
|  ___|    | |    | |                                     
| |_  ___  | |  __| |  ___  _ __                          
|  _|/ _ \ | | / _` | / _ \| '__|                         
| | | (_) || || (_| ||  __/| |                            
\_|  \___/ |_| \__,_| \___||_|                            
___  ___                                                  
|  \/  |                                                  
| .  . |  __ _  _ __    __ _   __ _   ___  _ __           
| |\/| | / _` || '_ \  / _` | / _` | / _ \| '__|          
| |  | || (_| || | | || (_| || (_| ||  __/| |             
\_|  |_/ \__,_||_| |_| \__,_| \__, | \___||_|             
                               __/ |                      
                              |___/                       
"""

print(font)
print(f"{CYAN}Author: {YELLOW}dawfunes\n\n")

# Script starts here
print(f"{BLUE}Press Enter to start the script...")

howSort = input("How do you want to sort the files? (1: By extension, 2: By date of creation): ")

# DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")
DOWNLOADS_FOLDER = "D:\\Downloads\\" # Carpeta de pruebas

if howSort == "1":
    # By extension
    print(f"{BLUE}Sorting files by extension...")
    files = os.listdir(DOWNLOADS_FOLDER)
    idx = 0
    for file in files:
        idx += 1
        print(f"{idx}/{len(files)}")
        print(file)
        file=DOWNLOADS_FOLDER+file
        if os.path.isfile(file):
            extension = DOWNLOADS_FOLDER + file.split(".")[-1]
            print("."+extension+"\n")
            if not os.path.exists(extension):
                os.mkdir(extension)
            os.rename(file, f"{extension}/{file[len(DOWNLOADS_FOLDER):]}")
    print(f"{GREEN}Files sorted successfully!")
elif howSort == "2":                                        # Se puede mejorar este codigo para que no se repita tanto
    # By date of creation
    print(f"{BLUE}Sorting files by date of creation...")
    files = os.listdir(DOWNLOADS_FOLDER)
    idx = 0
    for file in files:
        idx += 1
        print(f"{idx}/{len(files)}")
        print(file)
        file=DOWNLOADS_FOLDER+file
        if os.path.isfile(file):
            creationTime = os.path.getatime(file)
            creationDate = str(creationTime).split(" ")[0]
            print(time.strftime('%Y-%m-%d', time.localtime(creationTime))+"\n")
            creationDate = os.path.join(DOWNLOADS_FOLDER, time.strftime('%Y-%m-%d', time.localtime(creationTime)))
            if not os.path.exists(creationDate):
                os.mkdir(creationDate)
            os.rename(file, f"{creationDate}/{file[len(DOWNLOADS_FOLDER):]}")
    print(f"{GREEN}Files sorted successfully!")
else:
    print(f"{RED}Invalid option. Please try again.")