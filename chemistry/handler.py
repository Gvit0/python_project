import mend_table as MT
def FormulToMass(formulIn):
	formul= []
	status = "nil"
	formulNumb = 1
	tempMass =[]
	tempForm = ""
	for sumbol in formulIn:
		if sumbol in MT.upReg and status=="nil":
			tempForm += sumbol
			status = "ReadForm"
			
			t =1
		elif sumbol in MT.downReg and status =="ReadForm":
			tempForm += sumbol
			
			t=2
		elif sumbol in MT.upReg and status =="ReadForm":
			status = "nil"
			tempMass.append(tempForm)
			tempForm=sumbol
			
			t=3
		elif sumbol in MT.funcSumbol:
			status = "nil"
			formul.append(tempMass)
			formul.append([sumbol])
			
			t=4
		elif sumbol in MT.upReg and status== "ReadForm":
			status = "nil"
			tempMass.append(tempForm)
			tempForm=sumbol
			
			t=5
		elif sumbol == " ":
			pass
		print(str(formul)+str(tempMass)+tempForm)
	tempMass.append(tempForm)
	formul.append(tempMass)
	return formul