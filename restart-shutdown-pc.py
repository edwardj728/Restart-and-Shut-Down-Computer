import tkinter.messagebox
import os.path
import getpass
import time
from shutil import copyfile
import ctypes

user = getpass.getuser()
save_path = "C:/Users/"+user+"/Desktop/"
startup_path = "C:/Users/"+user+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
file_path = os.path.join(save_path, "restart-shutdown-temp.txt")
py_file_path = os.path.realpath(__file__)

#Shut down
if os.path.exists(file_path):
    ctypes.windll.user32.MessageBoxW(0, "Your computer will shut down in 5 seconds.", "Shutting down...", 1)
    time.sleep(5)
    os.remove(file_path)
    os.remove(startup_path+"/restart-shutdown-temp.py")
    os.system("shutdown /s -t 1")

#Restart
else:
    if tkinter.messagebox.askyesno("Restart Then Shut Down by Edward Jiang", "Are you sure you want to restart and then shut down your computer?"):
        file1 = open(file_path, "w")
        copyfile(py_file_path, startup_path+"/restart-shutdown-temp.py")
        os.system("shutdown -r -t 1")
    else:
        exit()