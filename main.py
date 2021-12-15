global cont

linea1 = ["a", "b", "c", "d"]
linea2 = ["e", "f", "g", "h"]
linea3 = ["i", "j", "k", "l"]
linea4 = ["m", "ñ", "n", "o"]
linea5 = ["p", "q", "r", "s"]
linea6 = ["t", "u", "v", "w"]
linea7 = ["x", "y", "z"]

msglist = []

cont = 0

def main ():
    print("")
    print("")
    print("")
    print("---------------------------------------")
    print("Programa Encriptador - Desencriptador")
    print("---------------------------------------")
    print("1. Encriptador")
    print("2. Desencriptador")
    print("3. Cerrar")
    print("---------------------------------------")
    opt = int(input("Escriba opción -> "))
    print("---------------------------------------")
    print("")
    if opt == 1:
        encrypter.encrypter_main()
    if opt == 2:
        decripter.decripter_main()
    if opt ==3:
        quit()

def megaprint():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

class encrypter():
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

    def encrypter_main():
        msg = str(input("Mensaje: "))
        print("")
        print("---------------------------------------")
        msglst = []

        for i in msg:
            msglst.append(i)

        for i in msglst:
            global cont
            encrypter.first_num_finder(msglst[cont])
            cont = cont + 1

        opt = "-".join([str(i) for i in msglist])
        print("")
        print("Mensaje Encriptado -> ", opt)
        print("---------------------------------------")
        input("Pulse cualquier tecla para continuar ->")
        megaprint()
        msglist.clear()
        msglst.clear()
        cont = 0
        main()

class decripter():

    #Definimos la función que desencriptará nuestro mensaje en analizando los pares de números por separado.

    def find_num_list(linea, letra):
        #Aquí toma la primera variable para localizar la lista a la que hace referencia el primer dígito
        if linea == 1:
            #Aquí, mediante el segundo dígito, localiza la letra en la lista correspondiente
            letter = linea1[letra]
            #Aquí agrega dicha letra a la lista del mensaje final
            msglist.append(letter)
        else:
            if linea == 2:
                letter = linea2[letra]
                msglist.append(letter)
            else:
                if linea == 3:
                    letter = linea3[letra]
                    msglist.append(letter)
                else:
                    if linea == 4:
                        letter = linea4[letra]
                        msglist.append(letter)
                    else:
                        if linea == 5:
                            letter = linea5[letra]
                            msglist.append(letter)
                        else:
                            if linea == 6:
                                letter = linea6[letra]
                                msglist.append(letter)
                            else:
                                if linea == 7:
                                    letter = linea7[letra]
                                    msglist.append(letter)

    def decripter_main():
        msg = str(input("Mensaje a desencriptar: "))
        print("")
        print("")
        msglst = []
        countmsg = msg.count("-")
        contador = msg.count("&")
        #Transforma el mensaje en una lista que poder manipular
        for i in msg:
            #Eliminamos los guiones ignorándolos
            if i != "-":
                #Añadimos a la lista los espacios que se reflejan mediante &
                if i == "&":
                    msglst.append(" ")
                else:
                    #Si el item no es ni - ni & se añade el número tal cual a la lista de desencriptado
                    msglst.append(i)

        #Definimos variables contador para trabajar con items pares en la lista
        k = 0
        j = 1
        #Calculo la diferencia entre & y guiones y le sumo 1 porque hemos visto que esa es la diferencia exacta
        #Esta diferencia es necesaria para el limite del range del siguiente loop, de lo contrario da out of range
        lop = countmsg - contador + 1

        for i in range(int(len(msglst)-lop)):
            #Si ninguno de los dos items de la lista es un espacio, lanza la función de desencriptado
            if msglst[k] != " ":
                if msglst[j] != " ":
                    var1 = int(msglst[k])
                    var2 = int(msglst[j])
                    decripter.find_num_list(var1, var2)
                    #Mueve indexador de lista un número par de casillas
                    k = k + 2
                    j = j + 2
            else:
                #Si el item es un espacio agrega el espacio y hace que el indexador se lo salte
                msglist.append(" ")
                k = k + 1
                j = j + 1

        opt = "".join([str(i) for i in msglist])
        print("---------------------------------------")
        print("")
        print("Desencriptado -> " + str(opt))
        print("")
        print("---------------------------------------")
        input("Pulse cualquier tecla para continuar ->")
        megaprint()
        msglist.clear()
        msglst.clear()
        main()


main()



