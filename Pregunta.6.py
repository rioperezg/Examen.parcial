from ast import While


def modificar(lista):
  pares = []
  impares = []
  for i in lista: 
       if i%2 == 0:
        pares.append(i)
       else:
        impares.append(i)
  pares.sort()
  impares.sort()
    