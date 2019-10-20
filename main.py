import sys,tty,termios

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
def printList(arr):
    for i in range(len(arr)):
        print("  " + arr[i],end="\n\r")
def hideCursor():
    print("\u001b[?25l",end='')
def resetCursor():
    print("\u001b[?0l",end='')
def singleChoice(arr,cursorColor="Blue",textOrVal="Val"):
    #save terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    #set terminal to raw mode
    tty.setraw(sys.stdin)
    #read output
    charIn=0
    printList(arr)
    hideCursor()
    cursorUp(len(arr))
    position=0
    setColor(cursorColor)
    print(">",end="")
    setColor("Reset")
    cursorLeft(1)
    while charIn!=13: #whilst enter not pressed
        sys.stdout.flush()
        charIn=ord(sys.stdin.read(1))#Get input
        if(charIn==27):#ESC pressed
            charIn=ord(sys.stdin.read(1))
            if(charIn==91):#[ pressed
                charIn=ord(sys.stdin.read(1))#Get input
                if(charIn==65):#Up
                    if(position>0):
                        print(" ",end="")
                        cursorLeft(1)
                        cursorUp(1)
                        setColor(cursorColor)
                        print(">",end="")
                        setColor("Reset")
                        cursorLeft(1)
                        position -=1
                elif(charIn==66):#Down
                    if(position<len(arr)-1):
                        print(" ",end="")
                        cursorLeft(1)
                        cursorDown(1)
                        setColor(cursorColor)
                        print(">",end="")
                        setColor("Reset")
                        cursorLeft(1)
                        position+=1
    cursorDown(len(arr)-position)
    #Set terminal style back to normal
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    resetCursor()
    if(textOrVal.upper()=="TEXT"):
        return arr[position]
    else:
        return position
def multiChoice(arr,cursorColor="Blue",textOrVal="Val",tickOrCross="T",otherColor="Green"):
    if (len(tickOrCross)>1):
        print("Error: character " +tickOrCross +" Too long")
        return -1
    #save terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    #set terminal to raw mode
    tty.setraw(sys.stdin)
    #read output
    charIn=0
    printList(arr)
    print("  Done",end="\n\r")
    hideCursor()
    cursorUp(len(arr)+1)
    position=0
    setColor(cursorColor)
    print(">",end="")
    setColor("Reset")
    cursorLeft(1)
    positionList=[]
    ended=False
    while ended!=True: #whilst enter not pressed
        #draw arrows at selected positions
        currpos=position
        cursorUp(position)
        for i in range(0, len(arr)):
            if(i in positionList):
                cursorRight(1)
                if tickOrCross =='X':
                    setColor("Red")
                    print("✗",end="\r\n")
                elif tickOrCross =='T':
                    setColor("Green")
                    print("✓",end="\r\n")       
                else:
                    setColor(otherColor)
                    print(tickOrCross,end="\r\n")
                setColor("Reset")
            else:
                cursorRight(1)
                print(" ",end="\r\n")
        cursorUp(len(arr)-currpos)

        sys.stdout.flush()
        charIn=ord(sys.stdin.read(1))#Get input
        if (charIn==13):
            if(position==len(arr)):
                ended=True
                break
            if(position not in positionList):
                positionList.append(position)
            else:
                positionList.remove(position)
            

        elif(charIn==27):#ESC pressed
            charIn=ord(sys.stdin.read(1))
            if(charIn==91):#[ pressed
                charIn=ord(sys.stdin.read(1))#Get input
                if(charIn==65):#Up
                    if(position>0):
                        print(" ",end="")
                        cursorLeft(1)
                        cursorUp(1)
                        setColor(cursorColor)
                        print(">",end="")
                        setColor("Reset")
                        cursorLeft(1)
                        position -=1
                elif(charIn==66):#Down
                    if(position<len(arr)):
                        print(" ",end="")
                        cursorLeft(1)
                        cursorDown(1)
                        setColor(cursorColor)
                        print(">",end="")
                        setColor("Reset")
                        cursorLeft(1)
                        position+=1
    cursorDown(len(arr)-position)
    print("",end='\n\r')
    #Set terminal style back to normal
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if textOrVal.upper() =="TEXT":
        posListText = []
        for i in positionList:
            posListText.append(arr[i])
        return posListText
    else: 
        return positionList

#valArray=["Choice1","Choice2","Choice3"]
#print(*multiChoice(valArray,"Red","Text","f","Magenta"), sep='\n')
#valArray=["Choice1","Choice2","Choice3"]
#print(singleChoice(valArray,"Magenta","Text"),)#
