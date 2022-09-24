import Cuantico
##Los experimentos de la canicas con coeficiente booleanos
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

def MarbleE():
    N_vertices=int(input("Dame el numero de vertices que quieres usar: "))
    Canicas=[]
    c=[]
    for i in range(N_vertices):
        print("Dame el numero de canicas en ", i)
        val=float(input())
        c.append(val)
        Canicas.append(c)
        c=[]
    Grafo=Crear_Matrix(N_vertices)
    print(f"\nEl estado del grafo inicial es: \n")
    print (Grafo)
    for i in Grafo:
        print(*i)
    Tiempo=int(input("\nDame el numero de clicks de tiempo en el cual quieres evaluar el estado del sistema:"))
    print(f"\nEl grafo a los {Tiempo} clicks de tiempo es:\n")
    Grafof=Cuantico.Time_c(Grafo,Tiempo)
    for i in Grafof:
        print(*i)
    print(f"\nEl estado inicial de las canicas es:\n")
    print(Canicas)
    print(f"\nEl estado despues de {Tiempo} clicks de tiempo es:\n")
    resul=Cuantico.states(Grafof,Canicas)
    print(resul)
    Cuantico.grafics(resul,N_vertices,Tiempo,"Cantidad canicas")
MarbleE()