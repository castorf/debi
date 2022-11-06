# This script is for shooting Bias Frames
# It will write flats and Darks to your C:\Calibration Directory
#
# It's written for sharpcap's IronPython interpreter
# You must have the Pro version sharpcap ($18/year) to use it.


# set Output format to FITS
# set colour space to mono16
# 8 bit will not work
# set capture area to Full Sensor
# set binning to 1
# You Must Have Google Desktop G:\Drive setup for this script to work https://www.google.com/drive/download/
# This script writes to LiveTest LunarEclipse08112022 folder
# Please replace Observer___ with Observer"Your Initials Here"_
# In SharpCap settings it is best to remove all formatting to your fits file naming or you will create multiple sub_folders on the DEB drive
# **** New File and Folder name ****
# Updated 11_5_2022 I changed the date to *** 08112022 *** from 07112022
# *** Updated 11_06_2022
#  This Script is for Shooting Bias Frames
#  Remember to put a lens cap on for Bias Frames
# *** Take the Lens Cap off for Lights and Flats

import time
import os

for q in range (0,20):

    print("0.000ms Bias Frame has been created")
    SharpCap.SelectedCamera = SharpCap.Cameras[0]
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 0.00
    SharpCap.Settings.CaptureFolder = r'C:\Calibration'
    SharpCap.TargetName = "Observer_JMW_Bias_Frame"
    SharpCap.SelectedCamera.CaptureSingleFrame()
   
    
    while True:
      if not SharpCap.SelectedCamera.Capturing :
        break
      time.sleep(0.5) 
    time.sleep(0.5)