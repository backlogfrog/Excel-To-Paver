#inspection data locations based on column number
#############################################################
##########       COLUMNS START AT 0 - - - - -################
#############################################################

#Size already in PAVER, unsure where excel # comes from, Calculated in scratchXml by P_LENGTH*P_WIDTH
INSPECTED_SIZE=5
INSPECTED_DATE=17
INSPECTED_PID1=2
INSPECTED_PID2=0
DCOMMENT=57
P_LENGTH=3
P_WIDTH=4


#WRONG COLUMN NUMBERS - PLACEHOLDERS
SAMPLE_NUM=12
DISTRESS_QUANTITY=13
SURFACE_WEATHERING=14

#distresscode data locations based on column
#E= exctent, S= severity
#Severity: 1= low, 2=med, 3=high
#Need quantity and other distresses

ALLIGATOR_E=23
ALLIGATOR_S=24
POTHOLE_E=33
POTHOLE_S=34
#Paver doesn't allow import of PCI w/o distresses, calculates based on distresses,
#unneeded but tracked anyway 
PCI_DISTRESS=55




#Unknown distress variables

#add to inspectionClasses.py once determined
#Columns double checked 2.9.20, probably unneeded given new data incoming
#SWEI=20 #swell?
#SWSI=21
#RCEI=26 #radial cracking?
#RCSI=27
#TCEI=29 #transverse cracking?
#TCSI=30
#SSEI=39 #surface swell?
#SSSI=40
#CEI=42 
#CSI=43
#JOEI=45 
#JOES=46
#BPT=48 #blow up/shatter?
#BPEI=49 #blow up/shatter?
#BPSI=50 #blow up/shatter?
#BSEI=52 #blow up/shatter?
#BSSI=53 #blow up/shatter?
