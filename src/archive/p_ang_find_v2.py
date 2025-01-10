
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:15:52 2024

@author: rushikesh
"""

import spiceypy 
from datetime import datetime, timedelta
import numpy as np
import os

project_path='/home/janmejoyarch/Dropbox/Janmejoy_SUIT_Dropbox/satellite_position/spice_git'
utc_fits = '2024-10-30T01:16:12.194'
spiceypy.furnsh(os.path.join(project_path, "data/interim/meta-kernel.txt"))
et_now = spiceypy.str2et(utc_fits)

sc_id = -156001;    #spacecraft NAIF ID
sc_obj_id = -156;
bc = os.path.join(project_path, 'data/external/SUT81N18P1AL10019108NNNN24305053620769_C24_0409_000630_00_qib.bc')
# C file coverage
coverage = spiceypy.ckcov (bc,sc_id,False,"SEGMENT",  0.0,  "TDB") #Find the coverage window for a specified object in a specified CK file.

# coverage of C kernel
begin_c, end_c = spiceypy.wnfetd(coverage,0) #Fetch a particular interval from a double precision window.
cov_c = int(end_c-begin_c)
t_vec = np.linspace(coverage[0], coverage[1], cov_c);
t_req = int(et_now) - int(begin_c)
utc_start, utc_end = spiceypy.et2utc(coverage, 'ISOC', 3);
print(t_vec[t_req])

# divide the et duration into small intervals and find the state and other values:
t_bin = 1; #in seconds
t_vec = np.linspace(coverage[0],coverage[1],int((coverage[1]- coverage[0])/t_bin));
if  begin_c < et_now < end_c :
    #define suit axes in its frame:
    vec_yaw_suit = np.array([1.0, 0.0, 0.0])
    vec_roll_suit = np.array([0.0, 1.0, 0.0])
    vec_pitch_suit = np.array([0.0, 0.0, 1.0])
    
    # solar north in HCI frame....Z axis
    hci_sun_north = np.array([0.0, 0.0, 1.0]);
    
    # Calculate everything in SUIT CCD frame
    cmat3 = spiceypy.pxform('HCI','ADITYA_SUIT2',et_now) #Return the matrix that transforms position vectors from one specified frame to another at a specified epoch.
    # get solar north in SUIT frame using the above transformation
    solar_north_in_suitframe = spiceypy.mxv(cmat3,hci_sun_north) #Multiply a 3x3 double precision matrix with a 3-dimensional double precision vector.
    # project the solar north in suitframe onto the CCD plane :
    # considering that the CCD plane is closely aligned with ROLL-PITCH plane and YAW is the boresight
    solar_north_suitccd = np.array([0,solar_north_in_suitframe[1],solar_north_in_suitframe[2]]);
    # the separation between suit roll vector(which should align with CCD columns) and solar_north_suitccd : p-angle
    p_angle_radian = spiceypy.vsep(vec_roll_suit, solar_north_suitccd)
    p_angle_deg = spiceypy.dpr()*p_angle_radian
    #if float(solar_north_suitccd[2]) < 0:
       # p_angle_deg = -1 * p_angle_deg
    #print('p_angle =',  p_angle_deg)
    spiceypy.kclear()
