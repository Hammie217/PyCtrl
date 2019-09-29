def cursorUp(val):
    if(isinstance(val, int)):
        if((val)>0):
            print(u"\u001b[" + str(val) + "A",end='')
            return 0
        return -1
    return -1
def cursorDown(val):
    if(isinstance(val, int)):
        if((val)>0):
            print(u"\u001b[" + str(val) + "B",end='')
            return 0
        return -1
    return -1

def cursorRight(val):
    if(isinstance(val, int)):
        if((val)>0):
            print(u"\u001b["+str(val)+"C",end='')
            return 0
        return -1
    return -1

def cursorLeft(val):
    if(isinstance(val, int)):
        if((val)>0):
            print(u"\u001b["+str(val)+"D",end='')
            return 0
        return -1
    return -1

def setColor(val):
    if(isinstance(val, str)):
        val=val.upper()
        if(val=="BLACK"):
            print("\u001b[30m",end="")
        elif(val=="RED"):
            print("\u001b[31m",end="")
        elif(val=="GREEN"):
            print("\u001b[32m",end="")
        elif(val=="YELLOW"):
            print("\u001b[33m",end="")
        elif(val=="BLUE"):
            print("\u001b[34m",end="")
        elif(val=="MAGENTA"):
            print("\u001b[35m",end="")
        elif(val=="CYAN"):
            print("\u001b[36m",end="")
        elif(val=="WHITE"):
            print("\u001b[37m",end="")
        elif(val=="RESET"):
            print("\u001b[0m",end="")
        else:
            return -1
        return 0
    return -1




