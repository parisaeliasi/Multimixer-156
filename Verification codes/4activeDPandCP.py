import math

def rotate(a,r,w):
    input = '{0:032b}'.format(a)
    rotated = input[-r:] + input[:-r]
    return(int(rotated,2))

def DP(a,b,n) :
    a_inv = 2**n-a
    b_inv = 2**n-b
    d1 = math.gcd(a,b_inv)
    d2 = math.gcd(a_inv,b)
    d3 = math.gcd(a,b)
    d4 = math.gcd(a_inv,b_inv)
    minII = math.ceil(min((d1*a_inv)/a,(d1*b)/b_inv))
    minIII = math.ceil(min((d2*a)/a_inv,(d2*b_inv)/b))
    minI = math.ceil(min((d3*a_inv)/a,(d3*b_inv)/b))
    minIV = math.ceil(min((d4*a)/a_inv,(d4*b)/b_inv))
    #res = max(minII+minIII,minI+minIV)
    res = minII+minIII
    return(res)

def DPuniA(a,w,r):
    arot0 = rotate(a,r,w)
    arot1 = (arot0+1)%(2**w)
    arot2 = (arot0-2**(w-r))%(2**w)
    arot3 = (arot1-2**(w-r)+1)%(2**w)
    
    DP0 = DP(a,arot0,w)
    if arot1 !=0:
        DP1 = DP(a,arot1,w)
    else:
        DP1 = 2**w
    if arot2 !=0:
        DP2 = DP(a,arot2,w)
    else:
        DP2 = 2**w
    if arot3 !=0:
        DP3 = DP(a,arot3,w)
    else:
        DP3 = 2**w
        
    #NP = DP0+DP1+DP2+DP3
    NP = DP0+DP2
    wt =2*w- math.log2(NP)
    return(wt)


def DPuniB(a,w,r1):
    brot = rotate(a,r1,w)
    brot0 = (a+brot)%(2**w)
    brot1 = (brot0+1)%(2**w)
    brot2 = (brot0-2**(w-r1))%(2**w)
    brot3 = (brot1-2**(w-r1))%(2**w)
    
    
    DPb0 = DP(a,brot0,w)
    
    if brot1 !=0:
        DPb1 = DP(a,brot1,w)
    else:
        DPb1 = 2**w
    
    if brot2 !=0:
        DPb2 = DP(a,brot2,w)
    else:
        DPb2 = 2**w
    
    if brot3 !=0:
        DPb3 = DP(a,brot3,w)
    else:
        DPb3 = 2**w
        
    #NPb = DPb0+DPb1+DPb2+DPb3
    NPb =  DPb0+DPb2
    wtb = 2*w-math.log2(NPb)
    return(wtb)

w = 32
Arr = [[2**(w-1)],[2**(w-1),2**(w-1)],[2**(w-3),5*(2**(w-3))], [2**(w-2),2**(w-2)],[2**(w-2),2**(w-2),3*(2**(w-2))],[3*(2**(w-3)),7*(2**(w-3))],[2**(w-1),2**(w-1)],[2**(w-1),2**(w-1),2**(w-1)],[3*(2**(w-2)),3*(2**(w-2))],[3*(2**(w-2)),3*(2**(w-2)),2**(w-2)]]
Listt=[]
Listtt= []
for el in Arr:
    wt = []
    wtt = []
    for i in range(len(el)):
        Weight1 = DPuniA(el[i],w,29)
        Weight2 = DPuniB(el[i],w,29)
        wt.append(Weight1)    
        wtt.append(Weight2)
    Listt.append(wt)
    Listtt.append(wtt)
#print(Listt,Listtt)

Final = []
for el in Listt:
    Weight = sum(el)+(4-len(el))*32
    Final.append(Weight)
print((Final))    

Final1 = []
for el in Listtt:
    Weight = sum(el)+(4-len(el))*32
    Final1.append(Weight)
print((Final1))    



