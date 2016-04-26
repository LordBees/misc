####chr
####ord
##def xor(k,m):
##	temp = ''
##	for x in range(len(m)):
##		temp += chr((ord(k[(len(str(k))%int(x))]))^ord(m[x]))
##	#for x in range(len(temp)):
##            #temp[x] = chr(temp[x])
##	return temp
k = 'key'
m = 'test'
a = ['\x1f','\x00','\n','\x1f']
def xor(k,m):##normal txt
    temp = ''
    for x in range(len(m)):
        print('Mchar: '+str(m[x]))
        print('Kchar: '+str(k[x%len(k)]))
        print('Msg: '+str(temp))
        print('Result: '+str(ord(m[x])^ord(k[x%len(k)])))
        temp +=chr(ord(m[x])^ord(k[x%len(k)]))
        #temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
	#for x in range(len(temp)):
            #temp[x] = chr(temp[x])
    return temp





def xorA(k,m):#arrays
    tempa = []
    for part in m:
        tempa.append(xor(k,part))
    return tempa

#xorA(k,['this is a test line:0', 'this is a test line:1', 'this is a test line:2', 'this is a test line:3', 'this is a test line:4', 'this is a test line:5', 'this is a test line:6', 'this is a test line:7', 'this is a test line:8', 'this is a test line:9'])
##def xorA(k,m):#arrays
##    tempa = [] ##=k
##    tempb = ''
##    tempc = []
##    for x in m:##was k
##        for y in range(len(x)):
##            print('Kchar: '+str(x))
##            print('Mchar: '+str(k[m.index(x)]))
##            #chr(x)
##            print(ord(x[y]),'::::',ord(k[m.index(x)%len(k)]))#x shouldbe m.index thing
##            print(tempa)
##            tempb =ord(x[y])^ord(k[m.index(x)%len(k)])
##            tempa.append(chr(tempb))
##            print(tempb)
##            tempb = ''
##        print(tempa)
##        tempc.append(tempa)
##        tempa = ''
##    print(tempc)
##    return tempa


def ktst(k,m):
    for x in range(len(k)):
        print(k[x%len(k)])
        
def arrtst(k,a):
    for x in a:
        print(ord(x))
        
def arriotst():
    f = open('testX','w')
    for x in range(0,10):
        f.write('this is a test line:'+str(x)+'\n')
    f.close()
    f=open('testX','r')
    x = f.readlines()
    f.close()
    return x

def strarray(array,strippt):##array strippart##
    tempa = []
    for x in array:
        tempa.append(x.strip(strippt))
    return tempa

def tst():
    xor(k,m)
    xorA(k,['\x1f','\x00','\n','\x1f'])
    xorA(k,['this is a test line:0', 'this is a test line:1', 'this is a test line:2', 'this is a test line:3', 'this is a test line:4', 'this is a test line:5', 'this is a test line:6', 'this is a test line:7', 'this is a test line:8', 'this is a test line:9'])
    
def cryptotest():
    k = 'teststring'##key
    m1 = 'exclusive or test!'
    m2 = ['array','tests','work','complete']
    x1 = xor(k,m1)
    x2 = xorA(k,m2)
    print('========')
    print('M1 = '+str(m1))
    print('========\nm2 array =\n')
    for x in range(len(m2)):
        print('|'+str(m2[x])+'|')
    print('\n\n\n\nxortest\nResult = :'+str(x1))
    print('\n\n\n\nxorAtest\nResult = :')
    for x in x2:
        print('|'+str(x)+'|')



















##
##
##def xorz(k,m):
##    temp = ''
##    for x in range(len(m)):
##        print(m[x])
##        print(temp)
##        temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
##	#for x in range(len(temp)):
##            #temp[x] = chr(temp[x])
##    return temp
##
##def xort(k,m):
##    temp = ''
##    for x in range(len(m)):
##        print(m[x])
##        print(temp)
##        temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
##	#for x in range(len(temp)):
##            #temp[x] = chr(temp[x])
##    return temp
##
##
##def xor2(k,m):
##    temp = ''
##    for x in range(len(m)):
##        print(m[x])
##        print(temp)
##        lettrky = (ord(k[(len(str(k))%int(x+1))]))
##        
##        temp += chr(lettrky^ord(m[x]))
##        
##	#for x in range(len(temp)):
##            #temp[x] = chr(temp[x])
##    return temp
##
##
##def xora(k,m):
##    tempa = []
##    tempb = ''
##    for x in range(len(m)):
##        keyitem = ord(k[(x+1)%len(m)])
##        tempb += chr(keyitem^ord(m[x]))
##    return tempb
##        
##        
##
