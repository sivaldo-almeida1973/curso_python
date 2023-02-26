"""
listas de lista e seus indices
"""

salas =  [
    
    # 0............1
    ['Maria', 'Helena'],  #  0
    # 0............1
    ['Elaine','Alice'] , # 1
    # 0.......   1............2
    ['Lucas', 'João', 'Eduarda',(10,20,30,40,50,)], # 2




]

#print(salas[1][0])
#print(salas[0][1])
#print(salas[0][1])
#print(salas[2][3][2])

#for salas in salas:
 #   print(salas)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)