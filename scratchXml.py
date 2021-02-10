
#custom XML module YATTAG wouldn't take data correctly so I said Fuck it and XML will be written from scratch
#Distress comment for every distress listed
DistressComment = "Imported"
#row[INSPECTED_SIZE]-- set actual square footage - excel sheet has different size
#inspectedSize=row[P_LENGTH]*row[P_WIDTH]
inspectedSize = 12
#PCI condition, doesn't import
condition=1


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

iS="  "
#unneeded @ this time, current sheet has L M H
######CALL severityConvert TO CONVERT # to L M H
#alligator_Severity=severityConvert(row[ALLIGATOR_S])
#potHole_Severity=severityConvert(row[POTHOLE_S])


#print(sWeathering, sampleNumber, distressQuantity)


# set spacing for indentation


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


#manually write XML data to filename.xml
#Changed comment to say Imp: for imported to identify



print(iS, "<geospatialInspectionData inspectionDate=\"",dateSet,"\"", " units=\"English\" level=\"SAMPLE\" >", sep="", file=f)
print(iS*2, "<inspectedElement inspectedElementID=\"", row[SAMPLENUMBER], "\"", " size=\"", inspectedSize, "\" ", "PID=\"", fullpid, "\" inspectedType=\"R\" comment=\"",DistressComment,  "\" noDistresses=\"false\">",  sep="", file=f)


#if row[ALLIGATOR_S] > 0 or row[POTHOLE_S] > 0:
print (iS*3, "<inspectionData>", sep="", file=f)

#E = extent, S = severity, unsure how to assign which to which at this point 11.09.20
# some streets have extent > 1 but severity is 0, the MKE  folder does not show an example of this, so I'm not sure what it means, may have to use AC_CL, the calculated score somehow as the severity



##alligator cracking
#check if severity is L,M,H (1,2,3) and write that data
#later: need to check ad or statements for all distresses?





#Set distress codes to dict, check to see if codes are > 0, then write
distressCodes = {
	'sweatherC': row[SWEATHERING_CODE],
	'sweatherS': row[SWEATHERING_S],
	'sweatherQ': row[SWEATHERING_Q],
	'alligatorC': row[ALLIGATOR_CODE],
	'alligatorS': row[ALLIGATOR_S],
	'alligatorQ': row[ALLIGATOR_Q],
	'blockcrackC': row[BLOCKCRACK_CODE],
	'blockcrackS': row[BLOCKCRACK_S],
	'blockcrackQ': row[BLOCKCRACK_Q],
	'trasnverseC': row[TRANSVERSE__CODE],
	'trasnverseS': row[TRANSVERSE_S],
	'trasnverseQ': row[TRANSVERSE_Q],
	'depressionC': row[DEPRESSION_CODE],
	'depressionS': row[DEPRESSION_S],
	'depressionQ': row[DEPRESSION_Q],
	'potholeC': row[POTHOLE_CODE],
	'potholeS': row[POTHOLE_S],
	'potholeQ': row[POTHOLE_Q],
	'edgecrackC': row[EDGECRACKING_CODE],
	'edgecrackS': row[EDGECRACKING_S],
	'edgecrackQ': row[EDGECRACKING_Q],
	'jointspallC': row[JOINTSPALLING_CODE],
	'jointspallS': row[JOINTSPALLING_S],
	'jointspallQ': row[JOINTSPALLING_Q],
	'durabilityC': row[DURABILITYCRACKING_CODE],
	'durabilityS': row[DURABILITYCRACKING_S],
	'durabilityQ': row[DURABILITYCRACKING_Q],
	'faultC': row[FAULTING_CODE],
	'faultS': row[FAULTING_S],
	'faultQ': row[FAULTING_Q],
	'patchingC': row[PATCHING_CODE],
	'patchingS': row[PATCHING_S],
	'patchingQ': row[PATCHING_Q],
	'bumpsagC': row[BUMPSAG_CODE],
	'bumpsagS': row[BUMPSAG_S],
	'bumpsagQ': row[BUMPSAG_Q]
}

distressCheck = []
distressCheck += distressCodes.values()
print (distressCheck)





#Function for printing distress to file
def distressPrint(code, severity, quantity):
	if float(code) > 0:
		print (iS*6, "<levelDistress distressCode=\"", code, "\"", "severity=\"", severity, "\" quantity=\"", quantity, "\"", "comment=\"", DistressComment, "\" />", sep="", file=f)



print (iS*5, "<PCIDistresses>", sep="", file=f)
distressPrint(distressCodes["sweatherC"],distressCodes["sweatherS"],distressCodes["sweatherQ"])
distressPrint(distressCodes["alligatorC"],distressCodes["alligatorS"],distressCodes["alligatorQ"])
distressPrint(distressCodes["blockcrackC"],distressCodes["blockcrackS"],distressCodes["blockcrackQ"])
distressPrint(distressCodes["trasnverseC"],distressCodes["trasnverseS"],distressCodes["trasnverseQ"])
distressPrint(distressCodes["depressionC"],distressCodes["depressionS"],distressCodes["depressionQ"])
distressPrint(distressCodes["edgecrackC"],distressCodes["edgecrackS"],distressCodes["edgecrackQ"])
distressPrint(distressCodes["jointspallC"],distressCodes["jointspallS"],distressCodes["jointspallQ"])
distressPrint(distressCodes["durabilityC"],distressCodes["durabilityS"],distressCodes["durabilityQ"])
distressPrint(distressCodes["durabilityC"],distressCodes["durabilityS"],distressCodes["durabilityQ"])
distressPrint(distressCodes["faultC"],distressCodes["faultS"],distressCodes["faultQ"])
distressPrint(distressCodes["patchingC"],distressCodes["patchingS"],distressCodes["patchingQ"])
distressPrint(distressCodes["bumpsagC"],distressCodes["bumpsagS"],distressCodes["bumpsagQ"])
print (iS*5, "</PCIDistresses>", sep="", file=f)


#close initial opened xml tags
#if row[ALLIGATOR_S] > 0 or row[POTHOLE_S] > 0:
print (iS*3, "</inspectionData>", sep="", file=f)
print(iS*2, "</inspectedElement>", sep="", file=f)
print(iS, "</geospatialInspectionData>", sep="", file=f)


#possibly unneeded, Paver seems to calculate simply based on distresses.
#unpaved roads will show PQI of "0," rating the road failed

print (iS, "<geospatialInspectionData level=\"SECTION\" units=\"English\" inspectionDate=\"", dateSet, "\" >", sep="", file=f)
print (iS*2, "<inspectedConditions PID=\"", fullpid, "\" >", sep="", file=f)
print (iS*3, "<conditions>", sep="", file=f)
print (iS*4, "<levelCondition comment=\"\" source=\"\" cndMeasureUID=\"StructPCI\" cndMeasure=\"SCI\" conditionText=\"\" condition=\"", condition, "\"/>", sep="", file=f)
print (iS*3, "</conditions>", sep="", file=f)
print (iS*2, "</inspectedConditions>", sep="", file=f)
print (iS, "</geospatialInspectionData>", sep="", file=f)

#close the exec sheet





#may need to check if PCI_DIESTRESS is > than 0 before printing anythingaaaa