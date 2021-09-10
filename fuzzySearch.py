import numpy as np
def hammingDist(p,t):
    #returns hamming distance
    ds=0
    for w in range(len(p)):
        if p[w] != t[w]:
            ds += 1
        
    return ds

def editDistRecur(a,b):
    #Returns edit distance between strings
    #Extremely slow do not use
    if len(a) == 0:
        return len(a)
    if len(b) == 0:
        return len(b)
    delta = 1 if a[-1] != b[-1] else 0
    return min(editDistRecur(a[:-1],b[:-1])+ delta,
               editDistRecur(a[:-1],b) + 1,
               editDistRecur(a,b[:-1]) + 1
            )

def editDistOptm(a,b):
    #Returns edit distance between strings
    lenA=len(a)
    lenB=len(b)
    matrix= np.ones((lenA+1, lenB+1))*-1
    matrix[0]= [y for y in range(lenB+1)]
    matrix[:,0]= [x for x in range(lenA+1)]
    for y in range(lenB):
        for x in range(lenA):
            delta = 1 if a[x] != b[y] else 0
            matrix[x+1][y+1] = min(matrix[x][y]+delta,
                                   matrix[x+1][y]+1,
                                   matrix[x][y+1]+1
                                    
                                )
    return matrix[-1][-1]

def funzzyEditDist(a,b):
    #Return minimun index of edit distance of sub-string a in b
    lenA=len(a)
    lenB=len(b)
    matrix= np.zeros((lenA+1, lenB+1))
    matrix[:,0]= [x for x in range(lenA+1)]
    for y in range(lenB):
        for x in range(lenA):
            delta = 1 if a[x] != b[y] else 0
            matrix[x+1][y+1] = min(matrix[x][y]+delta,
                                   matrix[x+1][y]+1,
                                   matrix[x][y+1]+1
                                    
                                )
            
    #traceback
    minIndey= np.argmin(matrix[-1])
    minIndex = lenA
    while minIndex > 0:
        delta = 1 if a[minIndex-1] != b[minIndey-1] else 0
        minIn = np.argmin([matrix[minIndex-1][minIndey-1]+delta,matrix[minIndex][minIndey-1]+1,matrix[minIndex-1][minIndey]+1])
        if minIn == 0:
            minIndex += -1 
            minIndey += -1
        elif minIn == 1:
            minIndey += -1
            
        else:
            minIndex += -1
        
    
    return minIndey -1