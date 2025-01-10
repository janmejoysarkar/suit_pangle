#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2025-01-09 17:45:59
@author: janmejoyarch
@hostname: suitpoc1

DESCRIPTION
- Find P-angle of image based on UTC of image.
- Inputs- * UTC time of image.
          * Camera Kernel from specific data packet.
- Output- (float) CROTA2 in degrees. -ve value means image is rotated clockwise.
"""
import spiceypy 
from datetime import datetime, timedelta
import numpy as np
import os
import glob

UTC_img = '2024-07-23T01:04:09.58'
project_path='/home/janmejoyarch/Dropbox/Janmejoy_SUIT_Dropbox/satellite_position/suit_pangle_git/'
###############
CK_file = os.path.join(project_path, 'data/external/local_CK.bc')
spiceypy.furnsh(os.path.join(project_path, "data/interim/meta-kernel.txt"))
ET_img = spiceypy.str2et(UTC_img) #convert utc_fits to ET
SC_ID = -156001;    #spacecraft NAIF ID
# Time coverage of CK (Camera Matrix Kernel) 
coverage = spiceypy.ckcov(CK_file, SC_ID, False, "SEGMENT", 0.0, "TDB") #Find the coverage window for a specified object in a specified CK file.
### Define SUIT Axes in SUIT frame
SUIT_ROLL_VEC = np.array([0.0, 1.0, 0.0])
#SUIT_YAW_VEC = np.array([1.0, 0.0, 0.0]); SUIT_PITCH_VEC = np.array([0.0, 0.0, 1.0])
### Define Sun north in HelioCentricInertial Frame ###
SUN_NORTH_VEC = np.array([0.0, 0.0, 1.0]);
### Transform HCI frame to SUIT payload frame ###
transform_matrix = spiceypy.pxform('HCI', 'ADITYA_SUIT2', ET_img) #Return the matrix that transforms position vectors from one specified frame to another at a specified epoch.
SUN_NORTH_SUIT_FRAME_VEC= spiceypy.mxv(transform_matrix, SUN_NORTH_VEC) # SUN NORTH in SUIT frame.
SUN_NORTH_SUIT_FRAME_VEC[0]=0 # Tilt in the direction towards/away from the direction of obs is set to 0.
p_angle_rad = spiceypy.vsep(SUIT_ROLL_VEC, SUN_NORTH_SUIT_FRAME_VEC) #Angular sep between two vectors in radian.
# Changes the direction of correction
if SUN_NORTH_SUIT_FRAME_VEC[2]<0 :
    p_angle_deg =-p_angle_rad*180/np.pi
else:
    p_angle_deg =p_angle_rad*180/np.pi
print(p_angle_deg)
spiceypy.kclear() #Clear the KEEPER subsystem: unload all kernels, clear the kernel pool, and re-initialize the subsystem. Existing watches on kernel variables are retained.
