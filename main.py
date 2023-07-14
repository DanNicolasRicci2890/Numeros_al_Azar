from OUT import *
from IN import *
from Verificador import *
from Ruleta import *

b = True
cont = 0
inicio = 0
tope = 0
py = 0
p = Ruleta()
cant_intento = 0
        

while(b):
    #titulo del juego
    OUT.consoleclear()
    OUT.titlemain("Ruleta Rusa", 30, 2)
    OUT.printed("---------------------------------------------------------------------", 0, 1)

#---------------------------------------------------------------------------------
    if (cont == 8):
        OUT.printedtwo("cantidad de intentos realizados: ", str(cant_intento), 10, 1)
        vl = str(IN.Getchimput("¿desea volver a jugar devuelta?(s=SI/n=NO):", 10, 1))
        if (vl.__contains__("b's'")):
            cant_intento = 0
            cont = 9
        elif (vl.__contains__("b'n'")):            
            cont = 10
        else:
            print(vl)
            OUT.printed("error de opcion...", 10, 2)
            OUT.pause(2)
        
#---------------------------------------------------------------------------------
    if (cont == 7):
        OUT.printed(" Acerto !!!! el numero a la azar es {}".format(int(p.getazar())), 10, 1)
        OUT.pause(5)
        cont = 8
#---------------------------------------------------------------------------------
    if (cont == 6):
        g = "valores acotados de busqueda [{} : {}] ".format(str(inicio), str(tope))
        OUT.printed(g, 10, 1)
        OUT.printedtwo("cantidad de intentos: ", str(cant_intento + 1), 10, 1)
        q = verifdata(IN.Strinput("Ingrese un numero al azar: ", 10, 1))
        if ((q.ConfigState()) == "OK"):
            num_azar = int(q.getverif())
            if (num_azar < inicio) or (num_azar > tope):
                OUT.printed("el {} no esta acotado entre los valores [{} / {}]"
                            .format(str(num_azar), str(inicio), str(tope)), 10, 1)                
            elif (num_azar > int(p.getazar())):
                OUT.printed("el {} es mayor que el numero azar...".format(str(num_azar)), 10, 1)
            elif (num_azar < int(p.getazar())):
                OUT.printed("el {} es menor que el numero azar...".format(str(num_azar)), 10, 1)
            elif (num_azar == int(p.getazar())):
                cont = 7
            cant_intento += 1                                       
        else:
            OUT.printed(q.ConfigState(), 10, 1)
        if (cont == 6):
            OUT.pause(2)
        
        
#---------------------------------------------------------------------------------
    if (cont == 5):
        OUT.printed("Comienza el juego....", 10, 1)
        OUT.pause(5)
        cont = 6

#---------------------------------------------------------------------------------
    if (cont == 4):
        g = "[{} : {}] en proceso de Azar....".format(str(inicio), str(tope))
        OUT.printed(g, 10, 1)
        OUT.pause(5)
        cont = 5
        
#---------------------------------------------------------------------------------    
    if (cont == 2):
        OUT.printedtwo("numero INICIO: ", str(inicio), 10, 1)
        OUT.printedtwo("  numero TOPE: ", str(tope), 10, 0)
        p.setinicio(inicio)
        p.setfinal(tope)
        if ((p.verificaring()) == "OK"):
            cont = 4
        else:
            OUT.printed(p.verificaring(), 10, 2)
            OUT.pause(2)
            cont = 3
        
#---------------------------------------------------------------------------------    
    if (cont == 0) or (cont == 1):
        frase = ""
        if (cont == 0):
            frase = "ingrese el numero de Inicio: "
            py = 1
        if (cont == 1):
            OUT.printedtwo("numero INICIO: ", str(inicio), 10, 1)
            frase = "ingrese el numero de Tope: "
            py = 2
        k = verifdata(IN.Strinput(frase, 10, py))
        
        if ((k.ConfigState()) == "OK"):
            if (cont == 0):
                inicio = int(k.getverif())
            if (cont == 1):
                tope = int(k.getverif())
            cont+=1        
        else:
            OUT.printed(k.ConfigState(), 10, py)
            OUT.pause(2)
#-----------------------------------------------------------------------------------
    if (cont == 3) or (cont == 9):
        cont = 0
    if (cont == 10):
        b = False
OUT.consoleclear()
OUT.printed("Adios....", 10, 5)
OUT.pause(4)