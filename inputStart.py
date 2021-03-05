#input for requesting filename for excel sheet
#then writing xml info/writing file based on filename
#deletes old file if exists



fileName=input(Fore.CYAN + "Enter Filename: ")
print(Style.DIM + fileName + ".xml")

#delete old filename if exists
#writing logfile and xml to find data printing errors
if os.path.exists("/XML"+fileName+".xml"):
  os.remove("/XML"+fileName+".xml")
  os.remove("/XML"+fileName+".log")
  print(Style.DIM + Fore.RED +"Original File Deleted \n \n")
else:
  print(Style.DIM + Fore.BLUE +"New file created \n \n")
f = open("/XML"+fileName + ".xml", "a+")
logFile = open("/XML"+fileName + ".log", "a+")