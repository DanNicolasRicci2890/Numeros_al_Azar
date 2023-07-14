import msvcrt
from OUT import *

class IN:
    def Strinput(fr, posx, posy):
        rl = OUT.gotox(posx)
        tb = OUT.gotoy(posy)
        rf = input("{}{}{}".format(tb, rl, fr))        
        return rf
    
    def Getchimput(fr, posx, posy):
        rl = OUT.gotox(posx)
        tb = OUT.gotoy(posy)
        print("{}{}{}".format(tb, rl, fr))     
        p = msvcrt.getche()   
        return p
    

            
