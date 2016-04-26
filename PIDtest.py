##import os
##
##pids = []
##pidl = []
##pnames = []
##a = os.popen("tasklist").readlines()#.split('\n')
##for x in range(len(a)):
##    a[x] = a[x].strip('\n')
##    
##for x in a:
##      try:
##         pids.append(str(x[0:26]).strip(' '))#pids.append(int(x[29:34]))
##         print(int(x[0:26]))
##      except:
##          #print('failed')
##          pass
##for each in pids:
##         pidl.append(each)
##
##for x in range(len(pidl)):
##    if x<5:
##        pass
##    else:
##        pnames.append(pidl[x])
        

import os

pids = []
pidl = []
pnames = []
prcids = []
procids = []
a = os.popen("tasklist").readlines()#.split('\n')
for x in range(len(a)):
    a[x] = a[x].strip('\n')
    
for x in a:
      try:
         pids.append(str(x[0:26]).strip(' '))#pids.append(int(x[29:34]))
         prcids.append(int(x[29:34]))
         print(int(x[0:26]))
      except:
          #print('failed')
          pass
for each in pids:
         pidl.append(each)

print('pidl:'+str(len(pidl)))
print('prcids:'+str(len(prcids)))

for x in range(len(pidl)):
    if x<5:
        pass
    else:
        #procids.append(prcids[x])
        pnames.append(pidl[x])
        
for x in range (len(prcids)):##lenchk as pids and names are not aligned in array
    if x<5:
        pass
    else:
        procids.append(prcids[x])

print(procids)
print('\n\n\n\n',pnames)
