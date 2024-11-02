# Код для работы с таблицами
# https://github.com/Gvit0/python_project/blob/main/tablesLib.py
# Вывод таблицы

def tables_to_string(matrix, vertical=True, horizontal=False, bordes=False, inC=False): 
    max_column_len_matrix = []
    out = ""  # Изменено с """ """ на ""
    output_msss = []
    
    for line in matrix:
        linMax = []
        for obj in line:
            linMax.append(len(str(obj)))
        max_column_len_matrix.append(linMax)
    
    max_column_len = [max(column) for column in zip(*max_column_len_matrix)]
    
    if bordes:
        Tline = ""
        if vertical:
            Tline += "+"
        for linLen in max_column_len:
            for i in range(linLen):
                Tline += "-"
            Tline += "+"    
        output_msss.append(Tline)

    for line in matrix:
        Tline = ""
        if vertical and bordes:
            Tline += "|"
        for obj, linLen in zip(line, max_column_len):
            if inC:
                Tline += str(obj).center(linLen)  # Центрируем текст
            else:
                Tline += str(obj).ljust(linLen)  # Заполняем пробелами до полной длины
            if vertical:
                Tline += "|"
            else:
                Tline += " "
        if not bordes:
            Tline = Tline[:-1]
        output_msss.append(Tline)
        if horizontal:
            Tline = ""
            if bordes:
                Tline += "+"
            for linLen in max_column_len:
                for i in range(linLen):
                    Tline += "-"
                Tline += "+"  
            if not bordes:
                Tline = Tline[:-1]
            output_msss.append(Tline)
    
    if not bordes and horizontal:
        output_msss = output_msss[:-1]
    if bordes and not horizontal:
        Tline = ""
        if vertical:
            Tline += "+"
        for linLen in max_column_len:
            for i in range(linLen):
                Tline += "-"
            Tline += "+"    
        output_msss.append(Tline)
    
    for i in output_msss:
        out += i + "\n"
    
    out = out[:-1]  # Удаляем последний символ новой строки
    return out


if __name__ == "__main__":
    table = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    table = [
        [15, 255, 39999],
        [448, 55, 6999],
        [7869, 8, 999]
    ]
    print("tables_to_string(vertical=True, horizontal=False, inC=True)")
    print(tables_to_string(table, vertical=True, horizontal=False, bordes=False, inC=True))
    if True:
        print("tables_to_string(vertical=False, horizontal=True, inC=True)")
        print(tables_to_string(table, vertical=False, horizontal=True, inC=True))
        print("tables_to_string(vertical=False, horizontal=False, inC=False)")
        print(tables_to_string(table, vertical=False, horizontal=False, inC=False))
        print("tables_to_string(vertical=True, horizontal=True, inC=True)")
        print(tables_to_string(table, vertical=True, horizontal=True, inC=True))
        print("tables_to_string(table, vertical=True, horizontal=True, borders=True, inC=True)")
        print(tables_to_string(table, vertical=True, horizontal=True, bordes=True, inC=True))
