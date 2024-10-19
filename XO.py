# by GatVit_Game https://github.com/Gvit0/python_project/

import random

scorep1, scorep2 = 0, 0
def paintPos():#┼ ─ │
    print("1│2│3")
    print("─┼─┼─")
    print("4│5│6")
    print("─┼─┼─")
    print("7│8│9")

def paint(pole):
    p = []
    for i in pole:
        if i == 1:
            p.append('X')
        elif i == -1:
            p.append('O')
        else:
            p.append(' ')
    print(f"{p[0]}│{p[1]}│{p[2]}    1│2│3")
    print("─┼─┼─    ─┼─┼─")
    print(f"{p[3]}│{p[4]}│{p[5]}    4│5│6")
    print("─┼─┼─    ─┼─┼─")
    print(f"{p[6]}│{p[7]}│{p[8]}    7│8│9")

def handlerWin(pole):
    global scorep1, scorep2
    for i in range(3):
        if pole[i] == pole[i + 3] == pole[i + 6]:
            if pole[i] == pf1:
                scorep1 += 1
                print("Игрок 1 выиграл!")
                return "p1"
            elif pole[i] == pf2:
                scorep2 += 1
                print("Игрок 2 выиграл!")
                return "p2"
        if pole[i * 3] == pole[i * 3 + 1] == pole[i * 3 + 2]:
            if pole[i * 3] == pf1:
                scorep1 += 1
                print("Игрок 1 выиграл!")
                return "p1"
            elif pole[i * 3] == pf2:
                scorep2 += 1
                print("Игрок 2 выиграл!")
                return "p2"
    if (pole[0] == pole[4] == pole[8]) or (pole[2] == pole[4] == pole[6]):
        if pole[4] == pf1:
            scorep1 += 1
            print("Игрок 1 выиграл!")
            return "p1"
        elif pole[4] == pf2:
            scorep2 += 1
            print("Игрок 2 выиграл!")
            return "p2"
    if not 0 in pole:
        print("НИЧЬЯ")
        return "N"
    
    return None

def ai_move(pole, pf2):
    # Проверка на возможность выигрыша ИИ
    for i in range(9):
        if pole[i] == 0:
            pole[i] = pf2
            if handlerWin(pole) == "p2":
                return i + 1  # Возвращаем номер позиции (1-9)
            pole[i] = 0  # Сбрасываем, если это не выигрышный ход

    # Проверка на возможность блокировки игрока
    for i in range(9):
        if pole[i] == 0:
            pole[i] = pf1
            if handlerWin(pole) == "p1":
                pole[i] = pf2
                return i + 1  # Возвращаем номер позиции (1-9)
            pole[i] = 0  # Сбрасываем, если это не блокирующий ход

    # Если нет ни выигрыша, ни блокировки, выбираем случайную позицию
    available_positions = [i for i in range(9) if pole[i] == 0]
    if available_positions:
        pos = random.choice(available_positions)
        pole[pos] = pf2
        return pos + 1  # Возвращаем номер позиции (1-9)

    return None

def game(mode):
    global pf1, pf2
    pole = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    nplay = int(input("Первый(1(вы)/2): "))
    pf1 = ""
    while not (pf1 == "X" or pf1 == "O"):
        pf1 = input("X/O: ")
    if pf1 == "X":
        pf1 = 1
        pf2 = -1
    else:
        pf1 = -1
        pf2 = 1
    while True:
        if nplay == 1:
            pos = int(input(" Игрок 1: Номер поля: "))
            while pole[pos - 1] != 0:
                pos = int(input("Игрок 1: Номер поля: "))
            pole[pos - 1] = pf1
            paint(pole)
            win = handlerWin(pole)
            if win != None:
                if win == "N":
                        print("НИЧЬЯ")
                        print(f"{scorep1}:{scorep2}")
                        return
                print("ИГРОК 1 ВЫИГРАЛ")
                print(f"{scorep1}:{scorep2}")
                return
            nplay = 2
        elif nplay == 2:
            if mode == 1:
                pos = int(input("Игрок 2: Номер поля: "))
                while pole[pos - 1] != 0:
                    pos = int(input("Игрок 2: Номер поля: "))
                pole[pos - 1] = pf2
                paint(pole)
                win = handlerWin(pole)
                if win != None:
                    if win == "N":
                        print("НИЧЬЯ")
                        print(f"{scorep1}:{scorep2}")
                        return
                    print("ИГРОК 2 ВЫИГРАЛ")
                    print(f"{scorep1}:{scorep2}")
                    return
            elif mode == 2:
                print("Ход ИИ...")
                ai_move(pole, pf2)
                paint(pole)
                win = handlerWin(pole)
                if win != None:
                    if win == "N":
                        print("НИЧЬЯ")
                        print(f"{scorep1}:{scorep2}")
                        return
                    print("ИИ ВЫИГРАЛ")
                    print(f"{scorep1}:{scorep2}")
                    return
            nplay = 1

while True:
    print("p/1)Игрок")
    print("a/2)ИИ")
    print("q)Выход")
    select = input("Select: ")
    if select == "q":
        exit()
    elif select == "p" or select == "1":
        paintPos()
        game(1)
    elif select == "a" or select == "2":
        paintPos()
        game(2)
