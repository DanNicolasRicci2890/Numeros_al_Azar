
class strconfig:
    def IsNumeric(num):
        t = False
        i = 0
        while(i < len(num)) and (((ord(num[i]) >= 48) and (ord(num[i]) <= 57)) 
                                 or (num[i] == '.') or ((num[i] == '-') and (i == 0))):
            i+=1
        if (i == len(num)):
            t = True
        return t
    
    def IsIntero(num):
        t = False
        i = 0
        while(i < len(num)) and ((ord(num[i]) >= 48) and (ord(num[i]) <= 57) 
                                                    or ((num[i] == '-') and (i == 0))):
            i+=1
        if (i == len(num)):
            t = True
        return t
    
    def IsLetter(num):
        t = False
        i = 0
        while(i < len(num)) and ((((ord(num[i])) >= 65) and ((ord(num[i])) <= 90)) 
                                 or (((ord(num[i])) >= 97) and ((ord(num[i])) <= 122))):
            i+=1
        if (i == len(num)):
            t = True
        return t  
    
    