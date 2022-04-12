from msvcrt import getch
import os
import time
def sfcscan():
    print("Starting SFC Scan....(Scans the integrity of all protected system files and replaces incorrect versions with correct Microsoft versions.)")
    time.sleep(1)
    os.system("sfc /scannow")
    print("sfc scan has finished scanning.")







def dsimscan():
    print("Starting The DSIM Scan....(DISM enumerates, installs, uninstalls, configures, and updates features and packages in Windows images. The commands that are available depend on the image being serviced and whether the image is offline or running.)")
    time.sleep(1)
    os.system("DISM /Online /Cleanup-Image /ScanHealth")
    print("dsim scan has finished scanning.")
    
    
    

def main():
    print("The Process Will Remain 2 Types Of Scans. Now SFC Scan Will Be Running. Be Patient While The Scan Is Running.")
    print("note: You Must Run The Program As Administrator")
    print("Press Any Key To Start.")
    getch()
    sfcscan()
    dsimscan()
    print("The Scan Has Finished. Its Recommended That You Restart Your Machine.")







main()
