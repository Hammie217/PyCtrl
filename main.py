def cursorUp(val):
    if((val)>0 and (isinstance(val, int))):
        print(u"\u001b[" + str(val) + "A",end='')
        return 0
    return -1

def cursorLeft(val):
    if(val>0):
        print(u"\u001b["+str(val)+"D")
        return 0
    return -1
