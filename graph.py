#what do i need for a mesh network
# some id system for the system 
# so let assume the following:
# 1. our nodes are the raspis /PC
# 2. we Syn-ack system that intializse the graph below
# 3. we assume that each syn-ack is diffent if client sends sync with the id 23 we get a syncack message of the same id (note this isnt meant for security just a learning platform
# 4. we assume that  the id are stored in a bin file
import numpy as np

if __name__=='__main__':
    V=4
    mat=[[0]*V for _ in range(V)]
    add_edge(mat,0,1)
    ## connet orogin to next node 
    add_edge(mat,0,2)
    add_edge(mat,1,2)
    add_edge(mat,2,3)
    #wwew
    print("Adjacency Matrix:")
    display_matrix(mat)

def add_edge(mat,i,j):
    mat[i][j]=1
    mat[j][i]=1
def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str,row)))
