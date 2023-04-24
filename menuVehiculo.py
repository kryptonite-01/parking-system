import os
import re #expresion regular
from tabulate import tabulate

class MenuVehiculo:
    #constructor
    def __init__(self,listaLugar,listaVehiculo):
        self.listaLugar = listaLugar
        self.listaVehiculo = listaVehiculo
        self.cuota = None

    # menu gestionar lugares de estacionamiento
    def mostrarMenu(self):
        while True: 
            print("\t---GESTIONAR VEHICULOS DE ESTACIONAMIENTO---\n")
            print("1. Agregar nuevo vehiculo")
            print("2. Mostrar todos los vehiculos")
            print("3. Buscar vehiculo")
            print("4. Cobrar cuota por estacionamiento")
            print("5. Regresar")
            #ingresar opcion
            opc = self.validarMenu(input("\nPor favor, elige una opcion: "))
            #regresar a menu principal si opc = 5
            if opc == 5:
                os.system('cls')
                break
            #switch de opciones
            self.switch(opc)

    #opciones menu gestionar lugares de estacionamiento
    def switch(self,opc):
        if opc == 1:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---AGREGAR NUEVO VEHICULO---\n")
                if self.listaLugar.esta_vacia() != None and self.listaLugar.lugaresVacios(): #la lista de lugares no esta vacia y existen lugares disponibles
                    print("\nLugares Disponibles\n")
                    self.listaLugar.imprimirVacios()
                    
                    #Ingresar valores de nuevo vehiculo
                    idVehiculo = self.validarAlfNum(input("Ingresar ID de vehiculo: "))
                    if idVehiculo == None:
                        os.system('cls')
                        print("\nPor favor, ingresa un valor alfanumérico.\n")
                        continue
                    #verificar si existe el vehiculo
                    vehiculo = self.listaVehiculo.buscar(idVehiculo)
                    #verificar si vehiculo no esta registrado
                    if  vehiculo != None:
                        os.system('cls')
                        print("\nEl vehiculo ",idVehiculo," ya existe, registrar otro\n")
                        continue

                    idLugar = self.validarAlfNum(input("Asignar estacionamiento: "))
                    if idLugar == None:
                        os.system('cls')
                        print("\nPor favor, ingresa un valor alfanumérico.\n")
                        continue
                    #verificar que lista no este vacia
                    if self.listaLugar.esta_vacia() == None:
                        os.system('cls')
                        print("\nNo hay lugares registrados\n")
                        continue
                    #verificar si existe el lugar
                    lugar = self.listaLugar.buscar(idLugar)
                    if  lugar != None:
                        #verificar si lugar esta disponible
                        if lugar.esOcupado == True:
                            os.system('cls')
                            print("\nEl lugar esta ocupado, seleccionar otro\n")
                            continue
                    else:
                        os.system('cls')
                        print("\nEl lugar ",idLugar, " no existe, ingresa otro\n")
                        continue
                    
                    horaEntrada = self.validarHora(input("Ingresar hora de entrada (24hrs - HH:MM): "))
                    if horaEntrada == None:
                        os.system('cls')
                        print("\nPor favor, ingresa una hora válida en formato HH:MM.\n")
                        continue
                    #registrar nuevo vehiculo
                    self.listaVehiculo.insertar(idVehiculo,idLugar,horaEntrada)
                    #buscar lugar, cambiar estatus y asignar ID de vehiculo
                    lugar = self.listaLugar.buscar(idLugar)
                    lugar.esOcupado = True
                    lugar.vehiculo = idVehiculo
                else:
                    print("\nNo hay lugares disponibles para asignar a vehiculo\n")  
                regresar = self.regresarMenu()
            return
        elif opc == 2:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---MOSTRAR TODOS LOS VEHICULOS---\n")
                self.listaVehiculo.imprimir()
                regresar = self.regresarMenu()
            return
        elif opc == 3:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---BUSCAR VEHICULO---\n")
                #verificar si existen vehiculos en lista
                if self.listaVehiculo.esta_vacia() != None:
                    idVehiculo = self.validarAlfNum(input("Ingresar ID de vehiculo: "))
                    vehiculo = self.listaVehiculo.buscar(idVehiculo)
                    #si el vehiculo no existe en la lista
                    if vehiculo !=None:
                        cabecera = ["ID Vehiculo","Hora Entrada","ID Lugar Asignado"]
                        data = []
                        print("\nVehiculo encontrado. Mostrando detalles...\n")
                        fila = [vehiculo.idVehiculo,vehiculo.horaEntrada,vehiculo.idLugar]
                        data.append(fila)
                        #imprimir tabla
                        print(tabulate(data, headers=cabecera, tablefmt="grid"))
                        print("\n")
                else:
                    print("\nLista vacia, no existen vehiculos\n")
                regresar = self.regresarMenu()
            return
        elif opc == 4:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---COBRAR CUOTA POR ESTACIONAMIENTO---\n")
                #verificar si existen vehiculos en lista
                if self.listaVehiculo.esta_vacia() != None:
                    idVehiculo = self.validarAlfNum(input("Ingresar ID de vehiculo: "))
                    #buscar vehiculo
                    vehiculo = self.listaVehiculo.buscar(idVehiculo)
                    #comprobar existencia de vehiculo
                    if vehiculo != None:
                        horaSalida = self.validarHora(input("Ingresa la hora de salida (24hrs - HH:MM): "))
                        #asignar valor de hora de salida a vehiculo encontrado
                        vehiculo.horaSalida = horaSalida
                        #calcular tiempo
                        tiempo = vehiculo.calcularTiempo()
                        #calcular cuota
                        cuota = round(self.cuota*tiempo,3)
                        print("Total a pagar: ",cuota,"\n")
                        #eliminar vehiculo
                        self.listaVehiculo.eliminar(idVehiculo)
                        #actualizar estatus y id vehiculo de lugar
                        lugar = self.listaLugar.buscar(vehiculo.idLugar)
                        lugar.esOcupado = False
                        lugar.vehiculo = None
                else:
                    print("\nLista vacia, no existen vehiculos\n")
                regresar = self.regresarMenu()
            return
    
    #regresar al menu anterior
    def regresarMenu(self):
        opc = input("\tDesea regresar al menu? (s/n)  ")
        if len(opc) == 1: 
            opc_ascii = ord(opc)
            if opc_ascii == 83 or opc_ascii == 115: #si (s-S)
                os.system('cls')
                return False
            elif opc_ascii == 78 or opc_ascii == 110: #no (n-N)
                os.system('cls')
                return True
            else:
                print("\nOpcion invalida\n")
                self.regresarMenu()
                return 
        else:
            print("\nIngresa solo un carácter\n")
            self.regresarMenu()
            return
    
    #validar entrda de opciones de menu
    def validarMenu(self,opc):
        os.system('cls')
        while True: 
            if len(opc) == 1: 
                if opc.isdigit():
                    numero = int(opc)
                    if numero >=1 and numero <=5:
                        return numero
                    else: 
                        print("\nOpcion invalida\n")
                        break
                else:
                    print("\nOpcion invalida\n")
                    break
            else:
                print("\nIngresa solo un carácter\n")
                break

    #validar valores alfanumericos y algunos caracteres especiales
    def validarAlfNum(self,dato):
        while True:
            patron = r'^[a-zA-Z0-9-]+$' # Expresión regular para aceptar solo caracteres alfanuméricos y guiones
            if re.match(patron, dato): #expresion regular
                return dato
            else:
                return None

    #valida formato de la hora registrada
    def validarHora(self,dato):
        while True:
            patron = r'^\d{2}:\d{2}$'#expresion regular fomato de hora HH:MM
            if re.match(patron, dato):
                return dato
            else:
                return None