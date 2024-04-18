import mend_table as MT
import handler
import calc

print("Добро пожаловать в химический калькулятор!")

def PrintMenu():
	print("возможности:")
	print("1) текстовая формула в формулу")
	print("2) формула в текстовую ")
	print("3) название формулы")

def MenuInput(InMen):
	if int(InMen)== 1:
		calc.TextToFormul(input("Введите формулу"))
	if int(InMen) ==0:
		print(handler.FormulToMass(input("формула:")))
		
while True:
	PrintMenu()
	MenuInput(input("Номер меню: "))
	