##xorcrypt



k='key'
m='test'

def tf():
    k='key'
    m='test'
    return xor_t(k,xor_t(k,m),decrypt = True)

def tfa():
    k='key'
    x = xor_t(k,['this','should','work','and','return'],arrayform = True)
    return xor_t(k,x,arrayform = True,decrypt = True)
    
def xor_t(k,m,decrypt = False,arrayform=False):
    print([k,m,decrypt,arrayform])
    datb = ''##databuffer
    datab = []##dataarraybuffer
    if arrayform:##decrypts line by line 
        tempa = []
        for part in m:
            tempa.append(xor_t(k,part,decrypt))
        return tempa

    
    if decrypt:##decrypt xor prep
        for x in range(0,len(m),2):
            datab.append(int(m[x]+m[x+1],16))## changes the hex pair to base 10 int redy for xor'ing
        print('d')
    else:##encrypt xor prep
        for x in range(len(m)):
            datab.append(ord(m[x]))

            
    ##actual xor code
    print('passed:',datab)
    for item in range(len(datab)):
        print('\n\n========'+str(item))
        print('XOR:'+str(datab[item])+'|'+str(ord(k[item%(len(k)-1)]))+' = '+str(datab[item]^ord(k[item%(len(k)-1)])))
        datab[item] = datab[item]^ord(k[item%(len(k)-1)])##xor rotating the -1 as the array starts at zero
        
    print(datab)
    ##end xor code

    #hex prefix stripper and formatter(rtrn string)
    if decrypt:
        for x in datab:
            datb +=chr(x)
    else:
        for x in datab:
            print('~~~~~~~~ PAIR|'+str(x)+'\nLEN = '+str(len(str(x)))+'\n')
            if len(str(hex(x)[2:])) == 1:
                print('padding:',x)
                datb += '0' +str(hex(x)[2:].upper())
            else:
                datb += str(hex(x)[2:].upper())
    print(datb)
    print('DONE')
    return datb
            













##def xxt():
##    kxtst()
##    xt()
##    
##def xt():
##    k='key'
##    m='test'
##    #m = 'test String'
##    t = xor(k,xor(k,m),forward = False)
##    print('\n\n\n\nRESULT:\n\n')
##    return t
#####THE % MUST BE -1 as key not rotating completely!!
##def xor(k,m,forward=True):##forward  is encrypt, backwards is decrypt
##    print('key = '+str(k))
##    print('m = '+str(m))
##    cryptbuff = ''
##    cryptbuff2 = []
##    out = ''
##    if forward:##xor
##        for x in range(len(m)):
##            print('\n\n========'+str(x))
##            print(str(ord(m[x]))+'^'+str(ord(k[x%len(k)])))
##            print(hex(ord(m[x])^ord(k[x%len(k)])))
##
##            if len(hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper())<2:
##                cryptbuff +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()
##                cryptbuff = '0' + cryptbuff##swapped zero as pos was causing prob with 3rd lttr for some reason  old = cryptbuff+='0'
##            else:
##                cryptbuff +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()##ascii values turned into hex and 0x chopped
##            print('cb:'+cryptbuff)
##        print('encrypted out:\n'+str(cryptbuff))
##        out = cryptbuff
##        cryptbuff = ''
##        cryptbuff2 = []
##            
##    else:##decrypting
##        ##int(hexthing,0) for guessing prefix
##        ##decrypting and converts to ascii code for xoring then rtns letterstream
##        for x in range(0,len(m)-1,2):
##            cryptbuff +=m[x]+m[x+1]
##            print('cryptoval_hexbayte_raw = '+str(cryptbuff))
##            if str(cryptbuff) == '0' or str(cryptbuff) == '00':
##                cryptbuff == 0#'00'#
##            else:
##                cryptbuff = (int(cryptbuff,16))
##            cryptbuff2.append(cryptbuff)#('0x' + cryptbuff)
##            print('cryptovalint = '+str(cryptbuff))
##            cryptbuff=''
####            if len(cryptbuff) == 2:
####                cryptbuff2.append('0x' + cryptbuff)
####                cryptbuff = ''
####                cryptbuff+=m[x]
####            else:
####                cryptbuff+=m[x]
####            cryptbuff2.append('0x' + cryptbuff)
####
##            print('cryptobuffer_STR = :',cryptbuff,'\n crypto array\n',cryptbuff2)
##            #out = cryptbuff2
##            
##        cryptbuff = ''
##        for x in range(len(cryptbuff2)):##stitcher code for concat msg as cryptbuff = output str
##            cryptbuff2[x] = int(cryptbuff2[x])^ord(k[x%len(k)])##xoring byte pair intified with key
##            print('XOR:'+str(cryptbuff2[x])+'^'+str(ord(k[x%len(k)]))+'|'       +chr(cryptbuff2[x])+'^'+str(k[x%len(k)]))
##            cryptbuff += chr(cryptbuff2[x])
##
##        out = cryptbuff
##        cryptbuff = ''
##        cryptbuff2 = []
##            
##    return out
##
##
##def kxtst():
##    for x in range(4):
##        t = 'test'
##        print(ord(t[x]))
##    print('\n')
##    for x in range(3):
##        k = 'key'
##        print(ord(k[x]))
##            
##            
##        

##    temp = ''
##    for x in range(len(m)):
##        if len(hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper())<2:
##            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()
##            temp+='0'
##        else:
##            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()##ascii values turned into hex and 0x chopped
##    print(temp)
##    return temp

####def xorA(k,m):#arrays
####    tempa = []
####    for part in m:
####        tempa.append(xor(k,part))
####    return tempa
####
####def Dxor(k,m):
####    pass
####
####def DxorA(k,m):#arrays
####    tempa = []
####    for part in m:
####        tempa.append(Dxor(k,part))
####    return tempa
####




























































def txor(k,m):##normal txt custom
    ##process xor hexify ascii codes then strip 0x and pack
    temp = ''
    temphx = ''##for holding to check
    for x in range(len(m)):
        print('~~~~~~~~//')
        print('Mchar: '+str(m[x]))
        print('Kchar: '+str(k[x%len(k)]))
        print('Msg: '+str(temp))
        print('Result: '+str(ord(m[x])^ord(k[x%len(k)])))
        print(hex(ord(m[x])^ord(k[x%len(k)])).upper())#[2:].upper())
        if len(hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper())<2:
            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()
            temp+='0'
        else:
            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()##ascii values turned into hex and 0x chopped
        #temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
	#for x in range(len(temp)):
            #temp[x] = chr(temp[x])
    return temp

def xorA(k,m):#arrays
    tempa = []
    for part in m:
        tempa.append(xor(k,part))
    return tempa

def DExor(k,m):
    global hexchars
    tempa=[]##hex
    tempb=[]##ascii codes den
    hbyteb=[0,0]#hexbytebuffer
    buffer=''
    for x in range(len(m)):
        if (len(buffer))==2:
            tempa.append(buffer)
            buffer = ''
            buffer+=m[x]
        else:
            buffer+=m[x]
    tempa.append(buffer)
    print(tempa)
    for x in range(len(tempa)):
        hbyteb[0] = (hexchars.index(tempa[x][0].upper())+1)*16
        hbyteb[1] = (hexchars.index(tempa[x][1].upper())+1)
        tempb.append(int(hbyteb[0])+int(hbyteb[1]))
        print(hbyteb)
    print(tempb)
    for x in range(len(tempb)):#xordec
        #tempb[tempb.index(x)] = chr(str(int(x)^ord(k[x%len(k)])))
        print(chr((int(tempb[x])^ord(k[x%len(k)]))))
    print(tempb)
    return tempb


def DExorA(k,m):#arrays
    tempa = []
    for part in m:
        tempa.append(DExor(k,part))
    return tempa
