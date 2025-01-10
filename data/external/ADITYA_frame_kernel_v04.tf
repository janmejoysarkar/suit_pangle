
ADITYA-L1 FRAME-----------------------------------

\begindata
   FRAME_ADITYA                  = -156001
   FRAME_-156001_NAME           = 'ADITYA'
   FRAME_-156001_CLASS          = 3
   FRAME_-156001_CLASS_ID       = -156001
   FRAME_-156001_CENTER         = -156 
   CK_-156001_SCLK              = -156
   CK_-156001_SPK               = -156

\begintext

Heliocentric Inertial (HCI) Frame

     Definition of the Heliocentric Inertial frame:
 
              All vectors are geometric: no aberration corrections are
              used.
 
              The solar rotation axis is the primary vector: the Z axis points
	      in the solar north direction.
 
              The solar ascending node on the ecliptic of J2000 forms the X
              axis.
 
              The Y axis is Z cross X, completing the right-handed
              reference frame.

\begindata

        FRAME_HCI                    =  1810420
        FRAME_1810420_NAME           = 'HCI'
        FRAME_1810420_CLASS          =  5
        FRAME_1810420_CLASS_ID       =  1810420
        FRAME_1810420_CENTER         =  10
        FRAME_1810420_RELATIVE       = 'J2000'
        FRAME_1810420_DEF_STYLE      = 'PARAMETERIZED'
        FRAME_1810420_FAMILY         = 'TWO-VECTOR'
        FRAME_1810420_PRI_AXIS       = 'Z'
        FRAME_1810420_PRI_VECTOR_DEF = 'CONSTANT'
        FRAME_1810420_PRI_FRAME      = 'IAU_SUN'
        FRAME_1810420_PRI_SPEC       = 'RECTANGULAR'
        FRAME_1810420_PRI_VECTOR     = ( 0, 0, 1 )
        FRAME_1810420_SEC_AXIS       = 'Y'
        FRAME_1810420_SEC_VECTOR_DEF = 'CONSTANT'
        FRAME_1810420_SEC_FRAME      = 'ECLIPJ2000'
        FRAME_1810420_SEC_SPEC       = 'RECTANGULAR'
        FRAME_1810420_SEC_VECTOR     = ( 0, 0, 1 )

\begintext

Geocentric Solar Ecliptic (GSE) frame:
+X is parallel to the geometric earth-sun position vector.
+Y axis is the normalized component of the geometric earth-sun velocity vector orthogonal to the GSE +X axis.
+Z axis is parallel to the cross product of the GSE +X axis
and the GSE +Y axis.

\begindata
FRAME_GSE 						= -156101
FRAME_-156101_NAME 			= 'GSE'
FRAME_-156101_CLASS			= 5
FRAME_-156101_CLASS_ID 			= -156101
FRAME_-156101_CENTER 			= 399
FRAME_-156101_RELATIVE 			= 'J2000'
FRAME_-156101_DEF_STYLE 			= 'PARAMETERIZED'
FRAME_-156101_FAMILY 			= 'TWO-VECTOR'
FRAME_-156101_PRI_AXIS 			= 'X'
FRAME_-156101_PRI_VECTOR_DEF 		= 										'OBSERVER_TARGET_POSITION'
FRAME_-156101_PRI_OBSERVER 		= 'EARTH'
FRAME_-156101_PRI_TARGET 		= 'SUN'
FRAME_-156101_PRI_ABCORR 		= 'NONE'
FRAME_-156101_SEC_AXIS 			= 'Y'
FRAME_-156101_SEC_VECTOR_DEF 		= 										'OBSERVER_TARGET_VELOCITY'
FRAME_-156101_SEC_OBSERVER 		= 'EARTH'
FRAME_-156101_SEC_TARGET 		= 'SUN'
FRAME_-156101_SEC_ABCORR 		= 'NONE'
FRAME_-156101_SEC_FRAME 			= 'J2000'


\begintext

Geocentric Solar Magnetospheric (GSM) frame:
+X is parallel to the geometric earth-sun position vector.
+Z axis is normalized component of north centered geomagnetic dipole vector orthogonal to GSM +X axis.
+Y completes the right-handed frame.

\begindata

FRAME_GSM 					= -156209
FRAME_-156209_NAME 		= 'GSM'
FRAME_-156209_CLASS 		= 5
FRAME_-156209_CLASS_ID 		= -156209
FRAME_-156209_CENTER		= 399
FRAME_-156209_RELATIVE 		= 'J2000'
FRAME_-156209_DEF_STYLE 		= 'PARAMETERIZED'
FRAME_-156209_FAMILY 		= 'TWO-VECTOR'
FRAME_-156209_PRI_AXIS 		= 'X'
FRAME_-156209_PRI_VECTOR_DEF 	= 'OBSERVER_TARGET_POSITION'
FRAME_-156209_PRI_OBSERVER 	= 'EARTH'
FRAME_-156209_PRI_TARGET		= 'SUN'
FRAME_-156209_PRI_ABCORR 	= 'NONE'
FRAME_-156209_SEC_AXIS 		= 'Z'
FRAME_-156209_SEC_VECTOR_DEF 	= 'CONSTANT'
FRAME_-156209_SEC_FRAME 		= 'IAU_EARTH'
FRAME_-156209_SEC_SPEC 		= 'LATITUDINAL'
FRAME_-156209_SEC_UNITS 		= 'DEGREES'
FRAME_-156209_SEC_LONGITUDE 	= 288.43
FRAME_-156209_SEC_LATITUDE 	= 79.54

\begintext


MAGNETOMETER FRAME---------------------------------

\begindata

      FRAME_ADITYA_MAG                  =  -156566
      FRAME_-156566_NAME               = 'ADITYA_MAG'
      FRAME_-156566_CLASS              =  4
      FRAME_-156566_CLASS_ID           =  -156566
      FRAME_-156566_CENTER             =  -156
      TKFRAME_-156566_RELATIVE         = 'ADITYA'
      TKFRAME_-156566_SPEC             = 'ANGLES'
      TKFRAME_-156566_UNITS            = 'DEGREES'
      TKFRAME_-156566_ANGLES           = ( 0.0, 0.0, 0.0 )
      TKFRAME_-156566_AXES             = ( 1,   2,   3   )

\begintext


HEL1OS FRAME---------------------------------
The misalignment angles of collimator plane normal wrt to spacecraft axes is obtained pre-dynamic and those angles of rotation about roll and pitch axes are used below for the HEL1OS frame.

\begindata

      FRAME_ADITYA_HEL1OS                  =  -156666
      FRAME_-156666_NAME               = 'ADITYA_HEL1OS'
      FRAME_-156666_CLASS              =  4
      FRAME_-156666_CLASS_ID           =  -156666
      FRAME_-156666_CENTER             =  -156
      TKFRAME_-156666_RELATIVE         = 'ADITYA'
      TKFRAME_-156666_SPEC             = 'ANGLES'
      TKFRAME_-156666_UNITS            = 'DEGREES'
      TKFRAME_-156666_ANGLES           = ( 0.0, 0.0397, 0.1017 )
      TKFRAME_-156666_AXES             = ( 1,   2,   3   )

\begintext


FOLLOWING IS A SAMPLE FRAME DEFINITION FOR VELC: YOU MAY CHANGE THE LAST THE 3 DIGITS IN THE ID(156450) , IF YOU WISH
IN PLACE OF THE ANGLES GIVEN AS 0,0,0 WRT ADITYA AXES, ONE CAN INCLUDE THE MISALIGNMENT ANGLES HERE.

VELC FRAME ---------------------------------------
Two frames for VELC: one for continuum channel  & one for spectroscopy channel

\begindata

      FRAME_ADITYA_VELC_CONT                  =  -156450
      FRAME_-156450_NAME               = 'ADITYA_VELC_CONT'
      FRAME_-156450_CLASS              =  4
      FRAME_-156450_CLASS_ID           =  -156450
      FRAME_-156450_CENTER             =  -156
      TKFRAME_-156450_RELATIVE         = 'ADITYA'
      TKFRAME_-156450_SPEC             = 'ANGLES'
      TKFRAME_-156450_UNITS            = 'DEGREES'
      TKFRAME_-156450_ANGLES           = ( 0.0, -0.0419, -0.0608 )
      TKFRAME_-156450_AXES             = ( 1,   2,   3   )
      
      
      FRAME_ADITYA_VELC_SPECT                  =  -156451
      FRAME_-156451_NAME               = 'ADITYA_VELC_SPECT'
      FRAME_-156451_CLASS              =  4
      FRAME_-156451_CLASS_ID           =  -156451
      FRAME_-156451_CENTER             =  -156
      TKFRAME_-156451_RELATIVE         = 'ADITYA'
      TKFRAME_-156451_SPEC             = 'ANGLES'
      TKFRAME_-156451_UNITS            = 'DEGREES'
      TKFRAME_-156451_ANGLES           = ( 0.0, -0.0419, -0.0608 )
      TKFRAME_-156451_AXES             = ( 1,   2,   3   )
       

\begintext


SUIT FRAME2---------------------------------

  \begindata
  
        FRAME_ADITYA_SUIT2                  =  -156300
        FRAME_-156300_NAME               = 'ADITYA_SUIT2'
        FRAME_-156300_CLASS              =  4
        FRAME_-156300_CLASS_ID           =  -156300
        FRAME_-156300_CENTER             =  -156
        TKFRAME_-156300_RELATIVE         = 'ADITYA'
        TKFRAME_-156300_SPEC             = 'ANGLES'
        TKFRAME_-156300_UNITS            = 'DEGREES'
        TKFRAME_-156300_ANGLES           = ( -0.4, 0.032, -0.037 )
        TKFRAME_-156300_AXES             = ( 1,   2,   3   )
  
  \begintext


ADITYA-L1 Mission NAIF ID Codes -- Definition Section
========================================================================

   This section contains name to NAIF ID mappings for the ADITYA-L1 mission.

\begindata

            NAIF_BODY_NAME += ( 'ADIT' )         
            NAIF_BODY_CODE += ( -156 )

            NAIF_BODY_NAME += ( 'ADITYA' )        
            NAIF_BODY_CODE += ( -156001 )

            NAIF_BODY_NAME += ( 'ADITYA_VELC_CONT' )           
            NAIF_BODY_CODE += ( -156450 )

            NAIF_BODY_NAME += ( 'ADITYA_VELC_SPECT' )           
            NAIF_BODY_CODE += ( -156451 )
            
            NAIF_BODY_NAME += ( 'ADITYA_MAG' )           
            NAIF_BODY_CODE += ( -156566 )

            NAIF_BODY_NAME += ( 'ADITYA_HEL1OS' )         
            NAIF_BODY_CODE += ( -156666 )

            NAIF_BODY_NAME += ( 'ADITYA_SUIT2' )         
            NAIF_BODY_CODE += ( -156300 )


 \begintext

