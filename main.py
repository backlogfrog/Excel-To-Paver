#extract data from a spreadsheet and convert to Paver XML data for import

#finding files by extension in main dir/opening files
import os
import glob

#needed to parse date in scratchXml.py
from datetime import datetime

#needed  run another .py file, unneeded at this time 11.18.20
#from subprocess import Popen

#probably unneeded at this time 11.18.20
#import json

#colored text for funskies
import colorama
from colorama import Fore, Back, Style 
colorama.init()
#reset color/style after printing
colorama.init(autoreset=True)
#Colors, yay...
#Format: print(Fore.BLACK + "TEXT " + str(VARIABLE))
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

#openpyxl package opens excel sheets
from openpyxl import load_workbook

#NEW DATA HAS NO DATE - ANY DATE IN 2010 is first date

##################################################################################
##################################################################################
##################################################################################
#set start positions to read data: 2012.xlsx data starts at row 4
#RowIncr=4
RowIncr=2   
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################




#import class info from inspectionClasses.py for inspection data and from mapping.py based on column to be printed to XML
from inspectionClasses import Inspections
from mapping import INSPECTED_SIZE, INSPECTED_DATE, INSPECTED_PID1, INSPECTED_PID2, DCOMMENT, P_LENGTH, P_WIDTH, SAMPLENUMBER, SWEATHERING_CODE, SWEATHERING_S, SWEATHERING_Q, ALLIGATOR_CODE, ALLIGATOR_S, ALLIGATOR_Q, BLOCKCRACK_CODE, BLOCKCRACK_S, BLOCKCRACK_Q, TRANSVERSE__CODE, TRANSVERSE_S, TRANSVERSE_Q, DEPRESSION_CODE, DEPRESSION_S, DEPRESSION_Q, POTHOLE_CODE, POTHOLE_S, POTHOLE_Q, EDGECRACKING_CODE, EDGECRACKING_S, EDGECRACKING_Q, JOINTSPALLING_CODE, JOINTSPALLING_S, JOINTSPALLING_Q, DURABILITYCRACKING_CODE, DURABILITYCRACKING_S, DURABILITYCRACKING_Q, FAULTING_CODE, FAULTING_S, FAULTING_Q, PATCHING_CODE, PATCHING_S, PATCHING_Q, BUMPSAG_CODE, BUMPSAG_S, BUMPSAG_Q

#set header/schema for xml
xml_header = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>"
xml_schema = "<pavementData xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"PavementInspectionDataV2.xsd\">"

#unneeded at this time
#needed to add date/time to JSON dictionary, 
#def json_serial(obj):
#    """JSON serializer for objects not serializable by default json code"""
#    if isinstance(obj, (datetime)):
#       return obj.isoformat()
#    raise TypeError ("Type %s not serializable" % type(obj))

#############################open workbook from xlsx files in main dir for mult choice
#############################

excel_list = [f for f in glob.glob("*.xlsx")]
print(Fore.BLUE + "Available Spreadsheets:")
for i, db_name in enumerate(excel_list, start=1):
    print ('{}. {}'.format(i, db_name))
  
while True:
	try:
		selected = int(input(Fore.CYAN + 'Select spreadsheet (1-{}): '.format(i)))
		db_name = excel_list[selected-1]
		print(Style.DIM + 'Loading {}'.format(db_name), "\n")
		break
	except (ValueError, IndexError):
		print(Fore.BLUE + 'Invalid. Please enter number between 1 and {}!'.format(i))
		print("	")

#load input/workbook from above and set current active sheet to "sheet"
workbook = load_workbook(filename=db_name, data_only=True)
workbook.sheetnames
sheet = workbook.active

#set/show last row and column to avoid out of range error
#LastRow=sheet.max_row
#LastColumn=sheet.max_column
#print ("Last Column ", LastColumn)
LastRow=sheet.max_row-RowIncr
print("Total row number is ", LastRow)

#request user input to determine how many records are wanted, keep within range of data
#based on the LastRow
while True:
    number = input(Fore.CYAN + "How many rows? ")
    try:
        number = int(number)
    except ValueError:
        print(Fore.BLUE + number, 'is not a number, try again.')
        continue
    if number <= 0:
        print("    ")
        print(Fore.BLUE + "Too low, try again.")
    elif number > LastRow:
        print("    ")
        print(Fore.BLUE + "Too high, try again.")
    else:
        print("    ")
        break

#set row input to final row read
LastRow=number

#LastRow = Copy of 2012.xlsx 685 readable lines
#2012.xlsx has 686 readable lines
FinalRow = sheet.max_row

#check to see if last row has data for first column - if 0 then subtract 1 from last Row
#to avoid empty data/date error
#else, add LastRow to RowIncr(sheet actual-data-start offset)

#WILL NEED TO DETERMINE IF FURTHER ROWS ARE BLANK/0 AND SUBTRACT FURTHER
cellCheck=sheet.cell(row=FinalRow, column=1).value
if cellCheck == 0:
	LastRow=LastRow+RowIncr-1
else:
	LastRow=LastRow+RowIncr


#request filename for output
exec(open("inputStart.py").read())

#add headers to top of page
print(xml_header, "\n", xml_schema, sep="", file=f)

#how many rows read/written
rowsRead=0


for row in sheet.iter_rows(min_row=RowIncr, max_row=LastRow, values_only=True):
			rowsRead=rowsRead+1
			#write to file with the info
			
			exec(open("scratchXml.py").read())
			

print (Fore.RED + "FIRST SS IS IN 2010 - NO SET DATE \n \n")
print(Fore.MAGENTA + str(rowsRead) + " rows read \n")			
#close xml main tag and workbook
print("</pavementData>", sep="", file=f)
f.close()