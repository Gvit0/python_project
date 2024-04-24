import mend_table as MT
import handler
import calc
from time import sleep
print("Добро пожаловать в химический калькулятор!")

def PrintMenu():
	print("возможности:")
	print("1)Найти молярную массу")
	#print("2) формула в текстовую ")
	#print("3) название формулы")
	print("q-выход")

def MenuInput(InMen):
	if InMen == "q":
		exit()
	elif int(InMen)== 1:
		print(f"Молярная масса: {calc.FindMolMass(handler.FormulToMass(input("Введите формулу для поиска молярной массы: ")))}")
	elif int(InMen) ==0:
		print(handler.FormulToMass(input("формула:")))
		
while True:
	PrintMenu()
	MenuInput(input("Номер меню: "))
	sleep(3)
	