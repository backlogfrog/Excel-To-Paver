
#custom XML module YATTAG wouldn't take data correctly so I said Fuck it and XML will be written from scratch
#Distress comment for every distress listed
DistressComment = "Imported"
#severity of alligator cracking based on 1,2,3 from excel sheet, mapping.py column locations - 1=Low 2=Med 3=High, use L M H
alligator_Severity = "NONE"
potHole_Severity = "NONE"


#sampleNum
#distressQuantity


#
#check the severity of the distress and give Low Medium or High value
#will probably need changing/uneccessary with new data. 
def severityConvert(rowDataHere):
	severityReal = "NONE"
	if rowDataHere == 1:
		severityReal = "L"
	elif rowDataHere == 2:
		severityReal = "M"
	elif rowDataHere == 3:
		severityReal = "H"
	print("severityConvert Testing", severityReal)
	return severityReal


######CALL severityConvert TO CONVERT # to L M H
alligator_Severity=severityConvert(row[ALLIGATOR_S])
potHole_Severity=severityConvert(row[POTHOLE_S])


#print(sWeathering, sampleNumber, distressQuantity)


# set spacing for indentation
iS="  "

#set pid without editing excel sheet to format NETWORK::STREET::PID#
address=str(row[INSPECTED_PID1]).replace(" ","")
address=address.replace(".","")
address=address.upper()
fullpid="WINFIELD::" + address + "::" + str(row[INSPECTED_PID2])



#set date to proper format

#spread_date = row[INSPECTED_DATE]
#parsed_date = datetime.strftime(spread_date, "%m/%d/%Y")

#temporary date needed due to date change and not present in excel
#or set dateSet=parsed_date to pull a proper parsed date from spreadsheet
dateSet="01/01/2010"


#print(xml_header, "\n", xml_schema, "\n", file=f) and opening xml tags

#row[INSPECTED_SIZE]-- set actual square footage - excel sheet has different size
inspectedSize=row[P_LENGTH]*row[P_WIDTH]

#manually write XML data to filename.xml
#Changed comment to say Imp: for imported to identify



print(iS, "<geospatialInspectionData inspectionDate=\"",dateSet,"\"", " units=\"English\" level=\"FRAME\" >", sep="", file=f)
print(iS*2, "<inspectedElement inspectedElementID=\"", row[INSPECTED_PID2], "\"", " size=\"", inspectedSize, "\" ", "PID=\"", fullpid, "\" inspectedType=\"R\" comment=\"",DistressComment,  "\" noDistresses=\"false\">",  sep="", file=f)


#if row[ALLIGATOR_S] > 0 or row[POTHOLE_S] > 0:
print (iS*3, "<inspectionData>", sep="", file=f)

#E = extent, S = severity, unsure how to assign which to which at this point 11.09.20
# some streets have extent > 1 but severity is 0, the MKE  folder does not show an example of this, so I'm not sure what it means, may have to use AC_CL, the calculated score somehow as the severity



##alligator cracking
#check if severity is L,M,H (1,2,3) and write that data
#later: need to check ad or statements for all distresses?

print("Alligator/Pothole Extent and severity: AES: ", row[ALLIGATOR_E],row[ALLIGATOR_S],"PES: ", row[POTHOLE_E],row[POTHOLE_S], " \n")




if row[ALLIGATOR_E] > 0 or row[POTHOLE_E] > 0:
		#determine if distresses exist/are greater than 0
		print (iS*5, "<PCIDistresses>", sep="", file=f)
		if row[ALLIGATOR_E] > 0:
			print (iS*6, "<levelDistress distressCode=\"1\" severity=\"", alligator_Severity, "\" quantity=\"2\" comment=\"", DistressComment, "\" />", sep="", file=f)
		if row[POTHOLE_E] > 0:
			print (iS*6, "<levelDistress distressCode=\"13\" severity=\"", potHole_Severity, "\" quantity=\"2\" comment=\"", DistressComment, "\" />", sep="", file=f)
		print (iS*5, "</PCIDistresses>", sep="", file=f)


#close initial opened xml tags
#if row[ALLIGATOR_S] > 0 or row[POTHOLE_S] > 0:
print (iS*3, "</inspectionData>", sep="", file=f)
print(iS*2, "</inspectedElement>", sep="", file=f)
print(iS, "</geospatialInspectionData>", sep="", file=f)


#possibly unneeded, Paver seems to calculate simply based on distresses.
#unpaved roads will show PQI of "0," rating the road failed
if row[PCI_DISTRESS] > 0:
			print (iS, "<geospatialInspectionData level=\"SECTION\" units=\"English\" inspectionDate=\"", dateSet, "\" >", sep="", file=f)
			print (iS*2, "<inspectedConditions PID=\"", fullpid, "\" >", sep="", file=f)
			print (iS*3, "<conditions>", sep="", file=f)
			print (iS*4, "<levelCondition comment=\"\" source=\"\" cndMeasureUID=\"StructPCI\" cndMeasure=\"SCI\" conditionText=\"\" condition=\"", row[PCI_DISTRESS], "\"/>", sep="", file=f)
			print (iS*3, "</conditions>", sep="", file=f)
			print (iS*2, "</inspectedConditions>", sep="", file=f)
			print (iS, "</geospatialInspectionData>", sep="", file=f)

#close the exec sheet





#may need to check if PCI_DIESTRESS is > than 0 before printing anythingaaaa