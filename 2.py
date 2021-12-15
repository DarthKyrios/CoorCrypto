linea1 = ["a", "b", "c", "d"]
linea2 = ["e", "f", "g", "h"]
linea3 = ["i", "j", "k", "l"]
linea4 = ["m", "ñ", "n", "o"]
linea5 = ["p", "q", "r", "s"]
linea6 = ["t", "u", "v", "w"]
linea7 = ["x", "y", "z"]

msglist = []
cont = 0


def first_num_finder(letra):
    if letra in linea1:
        numfinal = "1" + str(linea1.index(letra))
        msglist.append(numfinal)
    else:
        if letra in linea2:
            numfinal = "2" + str(linea2.index(letra))
            msglist.append(numfinal)
        else:
            if letra in linea3:
                numfinal = "3" + str(linea3.index(letra))
                msglist.append(numfinal)
            else:
                if letra in linea4:
                    numfinal = "4" + str(linea4.index(letra))
                    msglist.append(numfinal)
                else:
                    if letra in linea5:
                        numfinal = "5" + str(linea5.index(letra))
                        msglist.append(numfinal)
                    else:
                        if letra in linea6:
                            numfinal = "6" + str(linea6.index(letra))
                            msglist.append(numfinal)
                        else:
                            if letra in linea7:
                                numfinal = "7" + str(linea7.index(letra))
                                msglist.append(numfinal)
                            else:
                                if letra == " ":
                                    numfinal = "&"
                                    msglist.append(numfinal)


msg = str(input("Mensaje: "))
msglst = []

for i in msg:
    msglst.append(i)


for i in msglst:
    first_num_finder(msglst[cont])
    cont = cont + 1

opt = "-".join([str(i) for i in msglist])
print(opt)
