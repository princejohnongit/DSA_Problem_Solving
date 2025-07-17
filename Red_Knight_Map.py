#!/bin/python3

import math
import os
import random
import re
import sys
import math as m
import collections
#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start

    
    
def printShortestPath(n, i_start, j_start, i_end, j_end):
    moves=[
        (-2,-1,'UL'),
        (-2,1,'UR'),
        (0,2,'R'),
        (2,1,'LR'),
        (2,-1,'LL'),
        (0,-2,'L')]
    
    queue=collections.deque([(i_start,j_start,0,[])])
    visited=[[False for _ in range(n)]for _ in range(n)]
    visited[i_start][j_start]=True
    #print(queue)
    while queue:
        r,c,dist,path=queue.popleft()
        
        if r==i_end and c==j_end:
            print(dist)
            print(" ".join(path))
            return
        for dr,dc,move in moves:
            new_c,new_r=c+dc,r+dr
            
            if 0<=new_c<n and 0<=new_r<n and not visited[new_r][new_c]:
                visited[new_r][new_c]=True
                newpath=path + [move]
                queue.append((new_r,new_c,dist+1,newpath))
                
    print("Impossible")
        
        
    
    

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
