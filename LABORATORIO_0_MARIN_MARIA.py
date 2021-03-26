#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 00:33:02 2021

@author: mariamarin
"""

from numpy import *
from numpy import random
from random import shuffle
from tabulate import tabulate
import random 
print ("BIENVENIDO A MEMORICE \n")
print('Ingrese el numero de cartas a jugar: ')
num_cards=int(input())
score_j1=0
score_j2=0



board=[[row for col in range(2)] for row in range(num_cards)]


def Generate_board(board,num_cards):
    k=[]
    i=0
    j=num_cards-1
    for col in range(num_cards):
        for row in range(2):
            if i!=num_cards:
                k.append([i,j])
                i+=1
                j=j-1
            elif i==num_cards:
                break
            
    return k
boardfinish=Generate_board(board, num_cards)
random.shuffle(boardfinish) 
for sublist in boardfinish:
    random.shuffle(sublist) 



boardx=[["*" for col in range(2)] for row in range(num_cards)]
coord=[]
for i in range(len(boardx)):
    c=0
    if c!=len(boardx):
        a=i,c
        b=i,c+1
        j=[a,b]
        coord.append(j)
        c+=1
    elif c==len(boardx)-1:
        c=0
        i=0
        
tab=boardx+coord





def Choice(coordinates):
    coordinat=[int(x) for x in coordinates.split(',')]    
    row_num=coordinat[0]
    col_num=coordinat[1]
    return coordinat



def revelation(choic):
    x=choic[0]
    y=choic[1]
    tab[x][y]=boardfinish[x][y]
    num=boardfinish[x][y]
    return tab, num

def verification(choic1, choic2,n1,n2):
    if n1==n2:
        x=choic1[0]
        y=choic1[1]
        tab[x][y]=" "
        boardfinish[x][y]=" "
        x=choic2[0]
        y=choic2[1]
        tab[x][y]=" "
        boardfinish[x][y]=" "
    elif n1!=n2:
        x=choic1[0]
        y=choic1[1]
        tab[x][y]="*"
        x=choic2[0]
        y=choic2[1]
        tab[x][y]="*"
        print("NO SON PARES")
       
    return tab, boardfinish


while len(boardfinish)!=0:
    i=1
    def game(i,tab, boardfinish,score_j1,score_j2):
        print("\nJUGADOR",i,"\n")
        print('El tablero se mostrará a continuación como: (carta - coordenada)')
        print(tabulate(tab),"\n")
        print("Ingrese la coordenada de la carta que desea ver en formato: 0,1 ")
        coordinates1=input()
        choic1=Choice(coordinates1)
        res1,n1=revelation(choic1)
        print(tabulate(res1))
        print("Ingrese la coordenada de la carta que desea ver en formato: 0,1 ")
        coordinates2=input()
        choic2=Choice(coordinates2)
        res2,n2=revelation(choic2)
        if i==1:
            if n1!=n2:
                i=2
            elif n1==n2:
                i=1
                score_j1+=1
        elif i!=1:
            if n1!=n2:
                i=1
            elif n1==n2:
                i=2
                score_j2+=1
        print(tabulate(res2))
        
        
        
        tab,boardfinish=verification(choic1, choic2, n1, n2)
        
    
        
        return "gana"
    
    juego=game(i,tab, boardfinish,score_j1,score_j2)
    
   

    
    
    
    
    
    