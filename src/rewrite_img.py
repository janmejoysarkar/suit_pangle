#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2025-01-10 11:15:30
@author: janmejoyarch
@hostname: suitpoc1

DESCRIPTION
"""
from astropy.io import fits
import spiceypy 
from datetime import datetime, timedelta
import numpy as np
import os
import glob

def p_angle(UTC_img):
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
    print("Time:", UTC_img, "P-ANG(deg):", p_angle_deg)
    spiceypy.kclear() #Clear the KEEPER subsystem: unload all kernels, clear the kernel pool, and re-initialize the subsystem. Existing watches on kernel variables are retained.
    return p_angle_deg

if __name__=="__main__":
    ### USER-DEFINED ###
    project_path='/home/janmejoyarch/Dropbox/Janmejoy_SUIT_Dropbox/satellite_position/suit_pangle_git/'
    drive= '/home/janmejoyarch/sftp_drive/'
    img_path='suit_data/level1.1fits/\
2024/03/12/normal_4k/SUT_T24_0588_000293_Lev1.0_2024-03-12T06.58.01.409_0971NB04.fits'    
    img_path= os.path.join(drive, img_path)
    SAVE=True
    ####################
    project_path='/home/janmejoyarch/Dropbox/Janmejoy_SUIT_Dropbox/satellite_position/suit_pangle_git/'
    sav= os.path.join(project_path, "products", f"upd_{os.path.basename(img_path)}")
    with fits.open(img_path) as hdul:
        data= hdul[0].data
        hdr= hdul[0].header
    packet= hdr['FOLDNAME']
    ## KERNELS SYMLINKS ##
    CK_filepath= glob.glob(os.path.join(drive, "suitproducts/level0/*/*/*", packet, "*.bc"))[0]
    ADTSPK_filepath= glob.glob(os.path.join(drive, "suitproducts/level0/*/*/*", packet, "*.bsp"))[0]
    os.symlink(CK_filepath, os.path.join(project_path, "data/external/local_CK.bc"))
    os.symlink(ADTSPK_filepath, os.path.join(project_path, "data/external/", os.path.basename(ADTSPK_filepath)))
    hdr['CROTA2']=p_angle(hdr['T_OBS'])
    os.unlink(os.path.join(project_path, "data/external/local_CK.bc"))
    os.unlink(os.path.join(project_path, "data/external/", os.path.basename(ADTSPK_filepath)))
    print(CK_filepath, "\n", ADTSPK_filepath )
    ######################
    if SAVE: 
        fits.writeto(sav, data, header=hdr, overwrite=True)
        print(f"Saved-{sav}")
