import time, os

class OUT:
    def gotox(posx):
        rl = ""
        for i in range(posx):
            rl += " "
        return ("{}".format(rl))

    def gotoy(posy):
        tb = ""
        for i in range(posy):
            tb += "\n"
        return ("{}".format(tb))       
    
    def printed(nom, posx, posy):
        rl = OUT.gotox(posx)
        tb = OUT.gotoy(posy)
        print("{}{}{}".format(tb, rl, nom))
        
    def printedtwo(fr1, fr2, posx, posy):
        rl = OUT.gotox(posx)
        tb = OUT.gotoy(posy)
        print("{}{}{}{}".format(tb, rl, fr1, fr2))
        
    def titlemain(fr1, posx, posy):
        rl = OUT.gotox(posx)
        tb = OUT.gotoy(posy)
        g = ""
        for c in fr1:
            if (c != ' '):
                g += "="
            else: 
                g += " "
        print("{}{}{}".format(tb, rl, fr1))
        print("{}{}".format(rl, g))
        
    def consoleclear():
        os.system("cls")
        
    def pause(tiempo):
        time.sleep(tiempo)
        

