from sys import stdin
import imaginar
import random
import calculadora_matrices
def tuplas(matrizValidar,vector):
         for x in range(len(matrizValidar)):
                for y in range(len(matrizValidar[0])):
                        if matrizValidar[x][y]>1 and matrizValidar[x][y]<0:
                                comprobar = False
                                break
                        else:
                                matrizValidar[x][y]=(matrizValidar[x][y],0)
                vector[x]=[(vector[x],0)]
         return (matrizValidar,vector)
def booleano(matrizValidar,vector,numero):
        comprobar=True
        matrizValidar,vector=tuplas(matrizValidar,vector)
        if comprobar:
                for x in range(numero):
                        vector=calculadora_matrices.multiplicacion_matriz(matrizValidar,vector)
                vector=[x[0][0] for x in vector]
                return vector
        else:
                return "No es una matriz booleana"
def booleanoFraccion(matrizValidar,vector,numero):
        validar=True
        suma3=0
        for x in range(len(matrizValidar)):
                suma3+=vector[x]
                suma=0
                suma2=0
                for y in range(len(matrizValidar[0])):
                        suma+=matrizValidar[x][y]
                        suma2 +=matrizValidar[y][x]
                if round(suma,2)!=1 or round(suma2,2)!=1:
                        validar=False
        if validar and round(suma3,2)==1:
                boolean=[x for x in booleano(matrizValidar,vector,numero)]
                return boolean
        else:
                return "No valido"
def multiRenijas(n1,n2):
        matriz=[]
        for x in range((n1*n2)+2):
                matriz.append([0 for x in range((n1*n2)+2)])
        s=n1+1
        for x in range(1,n1+1):
                matriz[x][0]=1/n1
                for y in range(n2):
                        matriz[s][x]=1/n2
                        matriz[s][s]=1
                        s+=1
                s-=1
        vector=[0 for x in range((n1*n2)+2)]
        vector[0]=1
        matriz,vector=tuplas(matriz,vector)
        matrizN=calculadora_matrices.multiplicacion_matriz(matriz,matriz)
        vector=calculadora_matrices.multiplicacion_matriz(matrizN,vector)
        for x in range(len(matrizN)):
                for y in range(len(matrizN)):
                        matrizN[x][y]=matrizN[x][y][0]
                vector[x][0]=vector[x][0][0]

        return (matrizN,vector)
def booleanoFraccionimaginarios(matrizValidar,vector,numero):
        suma1=0
        validar=True
        for x in range(len(vector)):
                suma2=0
                suma3=0
                vector[x]=[vector[x]]
                suma1+=imaginar.modulo(vector[x][0])**2
                for y in range(len(vector)):
                        suma2+=imaginar.modulo(matrizValidar[x][y])**2
                        suma3+=imaginar.modulo(matrizValidar[y][x])**2
                
                suma2=round(suma2,1)
                suma3=round(suma3,1)
                if suma2!=1 or suma3!=1:
                        validar=False
        suma1=round(suma1,1)
        if validar and suma1==1:
                for x in range(numero):
                        vector=calculadora_matrices.multiplicacion_matriz(matrizValidar,vector)
                return vector
        else:
                return "No valido"

def multiRenijasimaginarios(n1,n2):
        matriz=[]
        for x in range((n1*n2)+2):
                matriz.append([(0,0) for x in range((n1*n2)+2)])
        s=n1+1
        s2=[-1,-1,1]
        s3=[1,-1,-1]
        for x in range(1,n1+1):
                matriz[x][0]=(1/(n1**(1/2)),0)
                for y in range(n2):
                        matriz[s][x]=(s2[y]*1/(n2*2)**(1/2),(s3[y]*1/(n2*2)**(1/2)))
                        matriz[s][s]=(1,0)
                        s+=1
                s-=1
        vector=[[(0,0)] for x in range((n1*n2)+2)]
        vector[0][0]=(1,0)
        
        #for x in range(len(matriz)):
         #   for y in range(len(matriz)):
          #      matriz[x][y]=round(matriz[x][y][0]**2+matriz[x][y][1]**2,2)
        vector=calculadora_matrices.multiplicacion_matriz(matriz,matriz)
        #vector=calculadora_matrices.multiplicacion_matriz(matriz,vector)
        matriz=calculadora_matrices.multiplicacion_matriz(matriz,matriz)
        return (matriz)
