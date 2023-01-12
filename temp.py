import numpy as np
import random

s1="ACAAGATCAAGA"
s2="ATTGATTGATTA"

m1 = len(s1)+1
n = len(s2)+1

m = np.ones((m1,n)) * -100
parent = np.zeros((m1,n,2))
m[:,0] = 0
m[0,:] = 0

match = 5
mismatch = -2

gap_open = -3
gap_extension = -1

for j in range(1,n):
    for i in range(1,m1):
        
        if s1[i-1]==s2[j-1]:
            m[j][i] = m[j-1][i-1]+match
            parent[j][i] = [i-1,j-1]
        else:
            miss = m[j-1][i-1] + mismatch
            
            gap_seq2 = m[j][i-1] + gap_open + gap_extension
            gap_seq1 = m[j-1][i] + gap_open + gap_extension
            
            l = np.array()
            

# def allign(i,j):
   
#     global s1,s2,m,parent
   
#     if i>0 and j>0:
#         if m[j][i-1] == -100:
#             allign(i-1,j)
#         if m[j-1][i-1] == -100:
#             allign(i-1,j-1)
#         if m[j-1][i] == -100:
#             allign(i,j-1)
       
#         if s1[i-1] == s2[j-1]:
#             if m[j-1][i-1] != -100:
#                 m[j][i] = m[j-1][i-1]+match
#                 parent[j][i] = [i-1,j-1]
               
#         else:
#             l = np.array([m[j][i-1],m[j-1][i-1],m[j-1][i]])
#             l = l + mismatch
           
#             if l[1] >= l[0] and l[1]>=l[2]:
#                m[j][i] = l[1]
#                parent[j][i] = [i-1,j-1]
           
#             elif l[0]>=l[0] and l[0]>=l[2]:
#                 m[j][i] = l[0]
#                 parent[j][i] = [i-1,j]
           
#             else:
#                 m[j][i] = l[2]
#                 parent[j][i] = [i,j-1]

allign(len(s1),len(s2))

print(m)
pi,pj = len(s1),len(s2)

traceback=[]


while pi!=0 and pj!=0:
    print(pi,pj)
    traceback+=[[pi,pj]]
    pi,pj = int(parent[pj][pi][0]),int(parent[pj][pi][1])
   
traceback+=[[0,0]]
   
s_1 , s_2 = '',''
for i in range(len(traceback)-1):
    x,y = traceback[i][0],traceback[i][1]
    x_,y_ = traceback[i+1][0],traceback[i+1][1]
    if x_!=x and y_!=y:
        s_1 += s1[x-1]
        s_2 += s2[y-1]
    if y_==y:
        s_2 += '_'
        s_1 += s1[x-1]
    if x_==x:
        s_1 += '_'
        s_2 += s2[y-1]
       
s_1,s_2 = s_1[::-1],s_2[::-1]    
print(f"{s1}\n{s2}\n")
print(f"{s_1}\n{s_2}")