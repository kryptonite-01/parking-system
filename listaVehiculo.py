from tabulate import tabulate

class NodoVehiculo:
    #constructor
    def __init__(self, idVehiculo, idLugar, horaEntrada):
        self.idVehiculo = idVehiculo
        self.horaEntrada = horaEntrada 
        self.horaSalida = None
        self.idLugar = idLugar
        self.siguiente = None
    
    def calcularTiempo(self):
        if self.horaEntrada != None and self.horaSalida != None:
            #transformar horas en minutos y sumar
            inicio = self.horaEntrada.split(":")
            fin = self.horaSalida.split(":")

            minutosInicio = (float(inicio[0])*60)+float(inicio[1])
            minutosFin = ((float(fin[0]))*60)+float(fin[1])

            #calcular tiempo
            tiempo = minutosFin - minutosInicio
            #transformacion a decimal
            tiempoDecimal = float(tiempo/60)
            
            return tiempoDecimal

class ListaVehiculo:
     #constructor
    def __init__(self):
        self.frente = None
    
   #comprueba si la lista esta vacia
    def esta_vacia(self):
        return self.frente is None

    #insertar nodo vehiculo en lista
    def insertar(self, idVehiculo, idLugar, horaEntrada):
        nuevo_nodo = NodoVehiculo(idVehiculo, idLugar, horaEntrada)
        if self.esta_vacia(): #lista vacia
            self.frente = nuevo_nodo
            print("\nVehiculo con ID ", idVehiculo, "insertado con éxito\n")
        else: #lista no vacia
            actual = self.frente
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            print("\nVehiculo con ID ", idVehiculo, "insertado con éxito\n")

    #imprime todos los elementos de la lista comenzando por el frente
    def imprimir(self):
        cabecera = ["ID Vehiculo","Hora Entrada","ID Lugar Asignado"]
        data = []
        if self.esta_vacia():
            print("\nLa lista está vacía\n")
        else:
            actual = self.frente
            while actual is not None:
                fila = [actual.idVehiculo,actual.horaEntrada,actual.idLugar]
                data.append(fila)
                actual = actual.siguiente
            #imprimir tabla
            print(tabulate(data, headers=cabecera, tablefmt="grid"))
            print("\n")

    #busca un nodo en particular dentro de la lista
    def buscar(self, idVehiculo):
        if self.esta_vacia():
            print("\nLa lista está vacía\n")
            return None
        else:
            actual = self.frente
            while actual is not None:
                if actual.idVehiculo == idVehiculo:
                    return actual
                actual = actual.siguiente
            print("\nNo se encontró ningún vehiculo con ID ", idVehiculo, " en la lista\n")
            return None

    #elimina un nodo en particular de la lista
    def eliminar(self, idVehiculo):
        if self.esta_vacia():
            return
        if self.frente.idVehiculo == idVehiculo:
            self.frente = self.frente.siguiente
            print("\nEl vehiculo con ID ", idVehiculo, " fue eliminado con éxito\n")
            return
        anterior = self.frente
        actual = self.frente.siguiente
        while actual is not None:
            if actual.idVehiculo == idVehiculo:
                anterior.siguiente = actual.siguiente
                print("\nEl vehiculo con ID ", idVehiculo, " fue eliminado con éxito\n")
                return
            anterior = actual
            actual = actual.siguiente
        print("\nNo se encontró ningún vehiculo con ID ", idVehiculo, " en la lista\n")