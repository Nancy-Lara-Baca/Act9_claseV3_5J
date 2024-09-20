print("Act 9 clases v2")
print("Nancy Lara Mat: 22308051281225")
# Zona de class

class Operadores1225:
    #Zona de funciones
    def suma1225(self, N, L):
        s1225=N+L
        print(f"La suma de {N} + {L} = {s1225}")
        
    def resta1225(self, N, L):
        s1225=N-L
        print(f"La resta de {N} - {L} = {s1225}")
        
    def multiplicacion1225(self, N, L):
        s1225=N*L
        print(f"La multiplicacion de {N} * {L} = {s1225}")
        
    def division1225(self, N, L):
        s1225=N/L
        print(f"La division de {N} / {L} = {s1225}")
        
    def modulo1225(self, N, L):
        s1225=N%L
        print(f"La modulo de {N} % {L} = {s1225}")
        
    def exponente1225(self, N, L):
        s1225=N**L
        print(f"La exponente de {N} ** {L} = {s1225}")
        
    def cociente1225(self, N, L):
        s1225=N//L
        print(f"La cociente de {N} // {L} = {s1225}")
        
# Zona de creacion de objeto
operanancy=Operadores1225()

# Zona de uso de objetos
print(" Funcion suma")
operanancy.suma1225(5,4)

print(" Funcion resta")
operanancy.resta1225(5,4)

print(" Funcion multiplicacion")
operanancy.multiplicacion1225(5,4)

print(" Funcion division")
operanancy.division1225(5,4)

print(" Funcion modulo")
operanancy.modulo1225(5,4)

print(" Funcion exponente")
operanancy.exponente1225(5,4)

print(" Funcion cociente")
operanancy.cociente1225(5,4)