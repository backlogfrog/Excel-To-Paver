#inspection data locations based on column number
#############################################################
##########       COLUMNS START AT 0 MOTHERFUCK ################
#############################################################

#Size already in PAVER, unsure where excel # comes from, Calculated in scratchXml by P_LENGTH*P_WIDTH
INSPECTED_SIZE=5
#no set date at this time
INSPECTED_DATE=17
#Name which will be truncated ex: CS Smith Rd. to CSSSmithRd in scratchXML
INSPECTED_PID1=2
INSPECTED_PID2=0
DCOMMENT=57
P_LENGTH=3
P_WIDTH=4


SAMPLENUMBER=4

#distresscode data locations based on column
#E= exctent, S= severity
#Severity: 1= low, 2=med, 3=high
#Need quantity and other distresses

SWEATHERING_CODE=5
SWEATHERING_S=6
SWEATHERING_Q=7


ALLIGATOR_CODE=8
ALLIGATOR_S=9
ALLIGATOR_Q=10


BLOCKCRACK_CODE=11
BLOCKCRACK_S=12
BLOCKCRACK_Q=13

TRANSVERSE__CODE=14
TRANSVERSE_S=15
TRANSVERSE_Q=16

DEPRESSION_CODE=17
DEPRESSION_S=18
DEPRESSION_Q=19

POTHOLE_CODE=20
POTHOLE_S=21
POTHOLE_Q=22


EDGECRACKING_CODE=23
EDGECRACKING_S=24
EDGECRACKING_Q=25


JOINTSPALLING_CODE=26
JOINTSPALLING_S=27
JOINTSPALLING_Q=28

DURABILITYCRACKING_CODE=29
DURABILITYCRACKING_S=30
DURABILITYCRACKING_Q=31

FAULTING_CODE=32
FAULTING_S=33
FAULTING_Q=34

PATCHING_CODE=35
PATCHING_S=36
PATCHING_Q=37

BUMPSAG_CODE=38
BUMPSAG_S=39
BUMPSAG_Q=40

#Paver doesn't allow import of PCI w/o distresses, calculates based on distresses,
#unneeded but tracked anyway 

#Surface Weathering #






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
