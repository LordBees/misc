#http://mathinsight.org/vectors_cartesian_coordinates_2d_3d
import math
class lib2DVect:
    vector1 = (0,0)
    vector2 = (0,0)
    def __init__(self):#,vec1,vec2):
        #self.vector1 = vec1
        #self.vector2 = vec2
        pass
    def add(self,vec1,vec2):
        print(vec1,vec2)
        #print(vec2[0]+'-'+vec1[0]+','+vec2[1]+'-'+vec1[1])

##        result = ((vec2[0]-vec1[0]),(vec2[1]-vec1[1]))
##        return result #((vec2[0]-vec1[0]),(vec2[1]-vec1[1]))
        return ((vec2[0]-vec1[0]),(vec2[1]-vec1[1]))
    def length(self,vec1,vec2):
        vect = self.add(vec1,vec2)
        return math.sqrt((vect[0]**2)+(vect[1]**2))##len
    def split(self,vectotal,vecn):
        pass #=sub
    def vecsum(self,vec1,vec2):
        return (vec1[0]+vec2[0],vec1[1]+vec2[1])
    def vecsums(self,vecarr):
        sumvec = [0,0]
        for x in range(len(vecarr)):
            sumvec[0]+=vecarr[x][0]#xaddition
            sumvec[1]+=vecarr[x][1]#yaddition
        return sumvec

class lib3DVect:
    vector1 = (0,0)
    vector2 = (0,0)
    vector3 = (0,0)
    def __init__(self):#,vec1,vec2):
        #self.vector1 = vec1
        #self.vector2 = vec2
        pass
    def add(self,vec1,vec2):#,vec3):
        print(vec1,vec2)
        #print(vec2[0]+'-'+vec1[0]+','+vec2[1]+'-'+vec1[1])

##        result = ((vec2[0]-vec1[0]),(vec2[1]-vec1[1]))
##        return result #((vec2[0]-vec1[0]),(vec2[1]-vec1[1]))
        #return ((vec2[0]-vec1[0])-vec3[0],(vec2[1]-vec1[1])-vec3[1],(vec2[2]-vec1[2])-vec3[2])#may not be correct
        return ((vec2[0]-vec1[0]),(vec2[1]-vec1[1]),(vec2[2]-vec1[2]))
    def length(self,vec1,vec2,vec3):
        vect = self.add(vec1,vec2,vec3)
        return math.sqrt((vect[0]**2)+(vect[1]**2)+(vect[2]**2))##len
    def split(self,vectotal,vecn):
        pass #=sub
    def vecsum(self,vec1,vec23):
        return (vec1[0]+vec2[0]+vec3[0],vec1[1]+vec2[1]+vec3[1])
    def vecsums(self,vecarr):
        sumvec = [0,0,0]
        for x in range(len(vecarr)):
            sumvec[0]+=vecarr[x][0]#xaddition
            sumvec[1]+=vecarr[x][1]#yaddition
            sumvec[2]+=vecarr[x][2]#yaddition 
        return sumvec
        
##class 2DVect:
##    vector1 = (0,0)
##    vector2 = (0,0)
##    def __init__(self,vec1,vec2):
##        self.vector1 = vec1
##        self.vector2 = vec2
##    def add():
        
        
#vector = lib2DVect()
#vector.add((1,2),(4,6))

##>>> veclist = [(0,3),(4,1)]
##>>> vector = lib2DVect()
##>>> vector.vecsums(veclist)

##>>> vector = lib3DVect()
##>>> vector.length((4,0),(0,4),(2,2))

##vector.length(((4,0),(0,4),(2,2)))
##KeyboardInterrupt
##>>> vector.length(((0,4),(4,0),(2,2)),((4,0),(0,4),(2,2)))

    
def t():
    vector = lib2DVect()
    return vector.add((1,2),(4,6))
