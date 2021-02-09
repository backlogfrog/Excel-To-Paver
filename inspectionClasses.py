#Class names for all variables pulled for each distress


import datetime
from dataclasses import dataclass


@dataclass
class Inspections:
	size: str
	idate: str
	pid1: str
	pid2: str
	comment: str
	alligatorE: str
	alligatorS: str
	potholeE: str
	potholeS: str
	pcidistress: str
	plength: str
	pwidth: str

    #quantity
	#Unknown variables
#add to inspectionClasses.py once determined
#SWEI20: str
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