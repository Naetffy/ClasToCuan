from matplotlib import pyplot
import math
##Experimento de las canicas con coeficientes booleanos##
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
def states(grafo,state):
    res=[]
    for i in range(len(grafo)):
        for j in range(len(state[0])):
            val=0
            for k in range(len(grafo[0])):
                val+=grafo[i][k]*state[k][j]
        res.append(val)
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
    print(f"El grafo a los {Tiempo} time clicks es:")
    print(Time_c(Grafo,Tiempo))
    print(f"El estado inicial de las canicas es:")
    print(Canicas)
    print(f"El estado despues de {Tiempo} time click es:")
    print(states(Time_c(Grafo,Tiempo),Canicas))

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
    print("El estado del sistema al inicio es :")
    print(State)
    for i in grafo:
        print(i)
    print("El estado final del sistema es: ")
    print(states(mult_m(grafo,grafo),State))

##Experimento de las multiples rendijas##

def Create_GC(N_Nodes,Slits):
    Grafo=[]
    for i in range(N_Nodes):
        Fila=[]
        for j in range(N_Nodes):
            if i == 0:
                k=(0,0)
                Fila.append(k)
            elif i<=Slits:
                if j==0:
                    k=(round((1/math.sqrt(Slits)),4),0)
                else:
                    k=(0,0)
                Fila.append(k)
            else:
                if j>0 and j<=Slits:
                    print("Con que probabilidad da la bala en el objetivo ",i-Slits," desde la rendija ",j,)
                    Rp=float(input("Real part of the probability"))
                    Ip=float(input("Imagin part of the probability"))
                    prob=(Rp,Ip)
                    Fila.append(prob)    
                elif j==i:
                    Fila.append((1,0))
                else:
                    Fila.append((0,0))
        Grafo.append(Fila)
    return Grafo

def MC(Data1,Data2):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data2[0])):
            Rp=0
            Ip=0
            for k in range(len(Data1[0])):
                Rp+=Data1[i][k][0]*Data2[k][j][0]-Data1[i][k][1]*Data2[k][j][1]
                Ip+=Data1[i][k][0]*Data2[k][j][1]+Data2[k][j][0]*Data1[i][k][1]
            columna.append((round(Rp,4),round(Ip,4)))
        res.append(columna)
    return res
def probs(Matrix):
    res=[]
    for i in Matrix:
        Fila=[]
        for j in i:
            Fila.append(round((j[0]**2),4)+round((j[1]**2),4))
        res.append(Fila)
    return res
def MultRC():
    Slits=int(input("Dame el numero de rendijas que quieres usar: "))
    Targets=int(input("Dame el numero de objetivos que quieres usar: "))
    N_Nodes=Slits+Targets+1
    State=[[1]]
    for i in range(N_Nodes-1):
        State.append([0])
    grafo=Create_GC(N_Nodes,Slits)
    print("El estado del sitema al inicio es:\n")
    print(State)
    print("El estado del grafo con numeros complejos es: \n")
    for i in grafo:
        print(i)
    print("El estado del grafo en probabilidad es: \n")
    for i in probs(grafo):
        print(i)
    print("El estado del grafo despues de 2 time clicks es: \n")
    Ttik=MC(grafo,grafo)
    for i in Ttik:
        print(i)
    print("El estado del grafo en probabilidad en 2 time clicks es:\n ")
    for i in probs(Ttik):
        print(i)
    print("El estado del sistema despues de 2 time cliks es:\n ")
    resul=states(probs(Ttik),State)
    print(resul)
    for i in range(len(resul)):
        resul[i]=resul[i]*100
    Names=[]
    for i in range(N_Nodes):
        Names.append(str(i))
    co=["blue","red","green","black","purple"]
    pyplot.title("Probabilidades en el segundo time click: ")
    pyplot.bar(Names,height=resul,color=co,width=0.5)
    pyplot.xlabel("Vertices")
    pyplot.ylabel("Porcentajes (%)")
    pyplot.show()
MultRC()
