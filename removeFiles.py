import os
import shutil
import time

days = time.time()

path = 'C:/Users/manas/OneDrive/Pictures/Screenshots'

ctime = os.stat(path).st_ctime

if os.path.exists(path):
    os.walk(path)
    os.path.join(path+"/")

    if(ctime > days):
        os.remove(path)
    else:
        shutil.rmtree(path)
else:
    print("Path not found")