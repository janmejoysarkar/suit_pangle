#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2025-01-10 11:15:30
@author: janmejoyarch
@hostname: suitpoc1

DESCRIPTION
"""
from astropy.io import fits
import os

### USER-DEFINED ###
img_path= "/home/janmejoyarch/sftp_drive/suit_data/level1.1fits/2024/10/29/engg4/SUT_C24_0406_000626_Lev1.0_2024-10-29T01.00.49.315_4081NB03.fits"
crota2= -5.585685
SAVE=True
####################
project_path='/home/janmejoyarch/Dropbox/Janmejoy_SUIT_Dropbox/satellite_position/suit_pangle_git/'
sav= os.path.join(project_path, "products", f"upd_{os.path.basename(img_path)}")
with fits.open(img_path) as hdul:
    data= hdul[0].data
    hdr= hdul[0].header
hdr['CROTA2']=crota2
if SAVE: 
    fits.writeto(sav, data, header=hdr, overwrite=True)
    print(f"Saved-{sav}")
