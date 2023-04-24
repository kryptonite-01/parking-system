import os
import re #expresion regular
from tabulate import tabulate

class MenuLugar:
    #constructor
    def __init__(self,listaLugar):
        self.listaLugar = listaLugar

    # menu gestionar lugares de estacionamiento
    def mostrarMenu(self):
        while True: 
            print("\t---GESTIONAR LUGAR DE ESTACIONAMIENTO---\n")
            print("1. Agregar nuevo lugar")
            print("2. Mostrar todos los lugares")
            print("3. Buscar lugar")
            print("4. Eliminar lugar")
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
                print("\t---AGREGAR NUEVO LUGAR---\n")
                idLugar = self.validarAlfNum(input("Ingresar ID de lugar: "))
                #validar tipo de dato
                if idLugar == None:
                        os.system('cls')
                        print("\nPor favor, ingresa un valor alfanumérico.\n")
                        continue

                #verificar si existe el lugar
                lugar = self.listaLugar.buscar(idLugar)
                #verificar si lugar no esta registrado
                if  lugar != None:
                    os.system('cls')
                    print("\nEl lugar ",idLugar," ya existe, registrar otro\n")
                    continue

                #insertar lugar
                self.listaLugar.insertar(idLugar)
                regresar = self.regresarMenu()
            return
        elif opc == 2:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---MOSTRAR TODOS LOS LUGARES---\n")
                self.listaLugar.imprimir()
                regresar = self.regresarMenu()
            return
        elif opc == 3:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---BUSCAR LUGAR---\n")
                idLugar = self.validarAlfNum(input("Ingresar ID de lugar: "))
                if idLugar == None:
                    os.system('cls')
                    print("\nPor favor, ingresa un valor alfanumérico.\n")
                    continue
                lugar = self.listaLugar.buscar(idLugar)
                #si el lugar existe
                if lugar != None:
                    cabecera = ["ID Lugar","Estatus","ID Vehiculo Asignado"]
                    data = []

                    print("\nLugar encontrado. Mostrando detalles...\n")
                    estatus = 'Ocupado' if lugar.esOcupado else 'Desocupado'
                    idVehiculo = 'Indefinido' if (lugar.vehiculo == None) else lugar.vehiculo
                    fila = [lugar.idLugar,estatus,idVehiculo]
                    data.append(fila)
                    #imprimir tabla
                    print(tabulate(data, headers=cabecera, tablefmt="grid"))
                    print("\n")
                regresar = self.regresarMenu()
            return
        elif opc == 4:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---ELIMINAR LUGAR---\n")
                idLugar = self.validarAlfNum(input("Ingresar ID de lugar: "))
                if idLugar == None:
                    os.system('cls')
                    print("\nPor favor, ingresa un valor alfanumérico.\n")
                    continue
                self.listaLugar.eliminar(idLugar)
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