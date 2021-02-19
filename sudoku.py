import random
import numpy as np
from random import randrange

l=0
sudokuh=[1,2,3,4,5,6,7,8,9]
sudoku=[['',3,5,2,9,'',8,6,4],['',8,2,4,1,'',7,'',3],[7,6,4,3,8,'','',9,''],[2,1,8,7,3,9,'',4,''],['','','',8,'',4,2,3,''],['',4,3,'',5,2,9,7,''],[4,'',6,5,7,1,'','',9],[3,5,9,'',2,8,4,1,7],[8,'','',9,'','',5,2,6]]

# print(sudoku)
def FuncionLista(lista1, lista2):
    sudokuNew=[elem for elem in lista1 if elem not in lista2]
    return sudokuNew

# x=sudoku[:,[1,8]]
# print(x)
# sudokuc=[["","",7,2,"","",4,3,8],[3,8,6,1,"",4,"",5,""],[5,2,4,8,"",3,6,9,""],[2,4,3,7,8,"",5,"",9],["","","",8,"",4,2,3,""],["",4,3,"",5,2,9,7,""],[4,"",6,5,7,1,"","",9],[3,5,9,"",2,8,4,1,7],[8,"","",9,"","",5,2,6]]

# print(sudoku[3][-1])
cont=0
cont1=0


# FILAS
# print('-------------------------------------------') 
for fila in range(9):
    for columna in range(9):
        if sudoku[fila][columna]==sudokuh:
            sudoku[fila][columna]=FuncionLista(sudokuh,sudoku[fila])
            # x='x'
        print(sudoku[fila][columna],end=('   '))
        cont+=1
        if cont==0 or  cont%3==0:
            print("|") 
    print(end=" \n")    
    cont1+=1
    if cont1%3==0:
        print('-------------------------------------------')    

# for i in range(0,5):
#     for j in range(i,5):
#         print (i,j)

# def filas(sudoku):
#     return sum(sudoku)
print()
print()
print()

# def main():
#     sudoku=[["",3,5,2,9,"",8,6,4],["",8,2,4,1,"",7,"",3],[7,6,4,3,8,"","",9,""],[2,1,8,7,3,9,"",4,""],["","","",8,"",4,2,3,""],["",4,3,"",5,2,9,7,""],[4,"",6,5,7,1,"","",9],[3,5,9,"",2,8,4,1,7],[8,"","",9,"","",5,2,6]]
#     hola=[1,3,6,7,3]
#     resultado=filas(hola)
#     print(resultado)
    

# main()

# COLUMNAS RARAS

sudokuc=[]

for l in range(9):
    for i in sudoku:
        # if i[l]==sudokuh:
    #     print(i[l],end=" ")
            # H=2
        sudokuc.append(i[l])
    # print()
# print(sudokuc)
col=0
sudokucol=[]
conta=0   
contr=0
while conta<len(sudokuc):
    sudokucol.append(sudokuc[conta:conta+9])
    conta+=9
print(sudokucol)   
print()
print()


for fila in range(9):
    for columna in range(9):
        if sudoku[fila][columna]==sudokuh:
            # sudoku[fila][columna]=[sudoku[fila][columna] for sudoku[fila][columna] in range(1,10) if sudoku[fila][columna] not in sudokucol[columna]]
            sudoku[fila][columna]=FuncionLista(sudokuh,sudokucol[fila])
        print(sudoku[fila][columna],end='   ')
        contr+=1
    print()

print()
print()
print(sudokucol[columna])    

print()
print()
array_square=[]
# CUADRITOS RAROS
contc=0
for fila in range(3):
    for columna in range(3):
        array_square.append(sudoku[fila][columna])
        contc+=1
        
    if contc%3==0:
        print()
print(array_square)
for fila in range(3):
    for columna in range(3,6):
        if sudoku[fila][columna]==sudokuh:
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print()      
for fila in range(3):
    for columna in range(6,9):
        if sudoku[fila][columna]==sudokuh:
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(3,6):
    for columna in range(3):
        if sudoku[fila][columna]==sudokuh:
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(3,6):
    for columna in range(3,6):
        if sudoku[fila][columna]=='':
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(3,6):
    for columna in range(6,9):
        if sudoku[fila][columna]=='':
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(6,9):
    for columna in range(3):
        if sudoku[fila][columna]=='':
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(6,9):
    for columna in range(3,6):
        if sudoku[fila][columna]=='':
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
for fila in range(6,9):
    for columna in range(6,9):
        if sudoku[fila][columna]=='':
            1
        print(sudoku[fila][columna], end=' ')
        contc+=1
        array_square.append(sudoku[fila][columna])
    if contc%3==0:
        print() 
print(array_square)

sudoku_square=[]
conta=0   
while conta<len(array_square):
    sudoku_square.append(array_square[conta:conta+9])
    conta+=9
print(sudoku_square) 
print()

print('\n'*4)

for filas in range(3):
    for columna in range(3):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[0] or sudokucol[0]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print() 
for filas in range(3):
    for columna in range(3,6):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[1]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()    
for filas in range(3):
    for columna in range(6,9):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[2]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(3,6):
    for columna in range(3):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[3]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(3,6):
    for columna in range(3,6):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[4]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(3,6):
    for columna in range(6,9):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[5]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(6,9):
    for columna in range(3):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[6]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(6,9):
    for columna in range(3,6):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[7]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()
for filas in range(6,9):
    for columna in range(6,9):
        if sudoku[filas][columna]=="s":
            sudoku[filas][columna]=[sudoku[filas][columna] for sudoku[filas][columna] in range(1,10) if sudoku[filas][columna] not in sudoku_square[8]]
        print(sudoku[filas][columna],end=(' '))
        cont+=1
        if cont%9==0:
            print()




 