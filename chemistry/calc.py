import handler
import mend_table as MT


def TextToFormul(text):
	pass
def FindMolMass(formul):
	molMassT = 0
	for formulObj in formul:
		for obj in formulObj:
			if obj in MT.funcSumbol:
				molMass = "Поиск молярной массы в формуле не временно поддерживается"
			else:
				Fobj = ""
				FobjIndex = ""
				for sumbol in obj:
					
					if sumbol in MT.upReg or sumbol in MT.downReg:
						Fobj += sumbol
					elif sumbol in MT.num:
						FobjIndex += sumbol
				if FobjIndex == "":
					FobjIndex = "1"
				MTobj = MT.get_use_name(Fobj)
				molMassT +=float(MTobj["atom_mass"]) * int(FobjIndex)
	molMass = str(molMassT)
	return molMass