num01 = " _ "
num02 = "| |"
num03 = "|_|"

num11 = "   "
num12 = "  |"
num13 = "  |"

num21 = " _ "
num22 = " _|"
num23 = "|_ "

num31 = "_  "
num32 = "_| "
num33 = "_| "

num41 = "   "
num42 = "|_|"
num43 = "  |"

num51 = " _ "
num52 = "|_ "
num53 = " _|"

num61 = " _ "
num62 = "|_ "
num63 = "|_|"

num71 = " _ "
num72 = "  |"
num73 = "  |"

num81 = " _ "
num82 = "|_|"
num83 = "|_|"

num91 = " _ "
num92 = "|_|"
num93 = " _|"





def input_text():
    line1 = input()
    line2 = input()
    line3 = input()
    return line1, line2, line3


def srav(lt1,lt2,lt3):
    otvet = ""
    if lt1 == num01 and lt2 == num02 and lt3 == num03:
        otvet = "0"
    elif lt1 == num11 and lt2 == num12 and lt3 == num13:
        otvet = "1"
    elif lt1 == num21 and lt2 == num22 and lt3 == num23:
        otvet = "2"
    elif lt1 == num31 and lt2 == num32 and lt3 == num33:
        otvet = "3"
    elif lt1 == num41 and lt2 == num42 and lt3 == num43:
        otvet = "4"
    elif lt1 == num51 and lt2 == num52 and lt3 == num53:
        otvet = "5"
    elif lt1 == num61 and lt2 == num62 and lt3 == num63:
        otvet = "6"
    elif lt1 == num71 and lt2 == num72 and lt3 == num73:
        otvet = "7"
    elif lt1 == num81 and lt2 == num82 and lt3 == num83:
        otvet = "8"
    elif lt1 == num91 and lt2 == num92 and lt3 == num93:
        otvet = "9"
    return otvet



def main():
    otvetus = ""
    i = 0
    l1 , l2, l3 = input_text()
    lennumb = len(l1)
    #if len(l1) == len(l2) == len(l3):
    count_numb = int((lennumb+1)/4)
    for im in range(count_numb):
        otvetus= otvetus + str(srav(l1[i:i+3],l2[i:i+3],l3[i:i+3]))
        i+= 4
    return otvetus



print(main())
