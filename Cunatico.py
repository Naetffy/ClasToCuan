##Experimento de las canicas con coeficientes booleanos##
from ast import For


def Crear_Matrix(N_vertices):
    Grafo=[]
    Fila=[]
    for j in range(N_vertices):
        Fila.append(0)
    for i in range(N_vertices):
        cont=0
        while(cont!=N_vertices):
            print("Dame un vertice que se se dirija a ",i," ingresar -1 en caso de que no exista, o ya se hayan ingresado todos.")
            Data=int(input())
            if Data>=N_vertices:
                print("El vertice no sirve")
                continue
            if (Data==-1):
                break
            Fila[Data]=1
        Grafo.append(Fila)
        Fila=[]
        for j in range(N_vertices):
            Fila.append(0)
    return Grafo

def mult_m(Mat1,Mat2):
    res=[]
    for i in range(len(Mat1)):
        columna=[]
        for j in range(len(Mat2[0])):
            val=0
            for k in range(len(Mat1[0])):
                val+=Mat1[i][k]*Mat2[k][j]
            columna.append(val)
        res.append(columna)
    return res
        
def Time_c(Grafo,Tick):
    cont=1
    last=Grafo
    while cont!=Tick:
        last=mult_m(Grafo,last)
        cont+=1
    return last

def Marble():
    N_vertices=int(input("Dame el numero de vertices que quieres usar: "))
    Canicas=[]
    c=[]
    for i in range(N_vertices):
        print("Dame el numero de canicas en ", i)
        val=int(input())
        c.append(val)
        Canicas.append(c)
        c=[]
    Grafo=Crear_Matrix(N_vertices)
    Tiempo=int(input("Dame el numero de clicks de tiempo en el cual queires evalual el estado del sistema:"))
    print(Time_c(Grafo,Tiempo))
    print(Canicas)
    print(mult_m(Time_c(Grafo,Tiempo),Canicas))

##Experimento de las multiples rendijas##

def Create_G(N_Nodes,Slits):
    Grafo=[]
    for i in range(N_Nodes):
        Fila=[]
        for j in range(N_Nodes):
            if i == 0:
                j=0
                Fila.append(j)
            elif i<=Slits:
                if j==0:
                    j=round((1/Slits),4)
                else:
                    j=0
                Fila.append(j)
            else:
                if j>0 and j<=Slits:
                    print("Con que probabilidad da la bala en el objetivo ",i-Slits," desde la rendija ",j)
                    prob=float(input())
                    Fila.append(prob)    
                elif j==i:
                    Fila.append(1)
                else:
                    Fila.append(0)
        Grafo.append(Fila)
    return Grafo
def MultR():
    Slits=int(input("Dame el numero de rendijas que quieres usar: "))
    Targets=int(input("Dame el numero de objetivos que quieres usar: "))
    N_Nodes=Slits+Targets+1
    State=[[1]]
    for i in range(N_Nodes-1):
        State.append([0])
    grafo=Create_G(N_Nodes,Slits)
    print(State)
    for i in grafo:
        print(i)
    print(mult_m(mult_m(grafo,grafo),State))

MultR()
