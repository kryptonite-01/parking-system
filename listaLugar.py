from tabulate import tabulate

class NodoLugar:
    #constructor
    def __init__(self,idLugar):
        self.idLugar = idLugar
        self.esOcupado = False
        self.vehiculo = None
        self.siguiente = None

class ListaLugar:
    #constructor
    def __init__(self):
        self.frente = None

    #comprueba si la lista esta vacia
    def esta_vacia(self):
        return self.frente is None
    
    #comprueba existencia de lugares vacios
    def lugaresVacios(self):
        if self.esta_vacia():
            return False
        else:
            actual = self.frente
            while actual is not None:
                if actual.esOcupado == False:
                    return True
                actual = actual.siguiente

    #insertar nodo lugar en lista
    def insertar(self, idLugar):
        nuevo_nodo = NodoLugar(idLugar)
        if self.esta_vacia(): #lista vacia
            self.frente = nuevo_nodo
            print("\nLugar con ID ", idLugar, "insertado con éxito\n")
        else: #lista no vacia
            actual = self.frente
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            print("\nLugar con ID ", idLugar, "insertado con éxito\n")

    #imprime todos los elementos de la lista comenzando por el frente
    def imprimir(self):
        cabecera = ["ID Lugar","Estatus","ID Vehiculo"] #cabecera de tabla
        data = [] #datos de tabla
        if self.esta_vacia():
            print("\nLa lista está vacía\n")
        else:
            actual = self.frente
            while actual is not None:
                estatus = "Ocupado" if actual.esOcupado else "Disponible"
                vehiculo = "N/A" if actual.vehiculo == None else actual.vehiculo
                fila = [actual.idLugar,estatus,vehiculo]
                data.append(fila)
                actual = actual.siguiente
            #imprimir tabla
            print(tabulate(data, headers=cabecera, tablefmt="grid"))
            print("\n")
    
    def imprimirVacios(self):
        cabecera = ["ID Lugar","Estatus","ID Vehiculo"]
        data = []
        if self.esta_vacia():
            print("\nLa lista está vacía\n")
        else:
            actual = self.frente
            while actual is not None:
                if actual.esOcupado == False:
                    estatus = "Ocupado" if actual.esOcupado else "Disponible"
                    vehiculo = "N/A" if actual.vehiculo == None else actual.vehiculo
                    fila = [actual.idLugar,estatus,vehiculo]
                    data.append(fila)
                actual = actual.siguiente
            #imprimir tabla
            print(tabulate(data, headers=cabecera, tablefmt="grid"))
            print("\n")

    #busca un nodo en particular dentro de la lista
    def buscar(self, idLugar):
        if self.esta_vacia():
            print("\nLa lista está vacía\n")
            return None
        else:
            actual = self.frente
            while actual is not None:
                if actual.idLugar == idLugar:
                    return actual
                actual = actual.siguiente
            print("\nNo se encontró ningún lugar con ID ", idLugar, " en la lista\n")
            return None

    #elimina un nodo en particular de la lista
    def eliminar(self, idLugar):
        if self.esta_vacia():
            return
        if self.frente.idLugar == idLugar:
            self.frente = self.frente.siguiente
            print("\nEl lugar con ID ", idLugar, " fue eliminado con éxito\n")
            return
        anterior = self.frente
        actual = self.frente.siguiente
        while actual is not None:
            if actual.idLugar == idLugar:
                anterior.siguiente = actual.siguiente
                print("\nEl lugar con ID ", idLugar, " fue eliminado con éxito\n")
                return
            anterior = actual
            actual = actual.siguiente
        print("\nNo se encontró ningún lugar con ID ", idLugar, " en la lista\n")