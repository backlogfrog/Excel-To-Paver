#input for requesting filename for excel sheet
#then writing xml info/writing file based on filename
#deletes old file if exists



fileName=input(Fore.CYAN + "Enter Filename: ")
print(Style.DIM + fileName + ".xml")

#delete old filename if exists

if os.path.exists(fileName+".xml"):
  os.remove(fileName+".xml")
  print(Style.DIM + Fore.RED +"Original File Deleted \n \n")
else:
  print(Style.DIM + Fore.BLUE +"New file created \n \n")
f = open(fileName + ".xml", "a+")
logFile = open(fileName + ".log", "a+")