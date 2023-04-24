import os
from listaLugar import ListaLugar
from listaVehiculo import ListaVehiculo
from menuLugar import MenuLugar
from menuVehiculo import MenuVehiculo
from menuCuota import MenuCuota

class Menu:
    #constructor
    def __init__(self):
        self.listaLugar = ListaLugar()
        self.listaVehiculo = ListaVehiculo()
        self.menuLugar = MenuLugar(self.listaLugar)
        self.menuCuota = MenuCuota()
        self.menuVehiculo = MenuVehiculo(self.listaLugar,self.listaVehiculo)
        
    # menu principal
    def mostrarMenu(self):
        while True: 
            print("\t---MENU PRINCIPAL---\n")
            print("1. Gestionar lugares de estacionamiento")
            print("2. Gestionar vehiculos")
            print("3. Gestionar cuota de cobro")
            print("4. Salir")
            #ingresar opcion
            opc = self.validarMenu(input("\nPor favor, elige una opcion: "))
            #salir del programa si opc = 4
            if opc == 4:
                os.system('cls')
                break
            #switch de opciones
            self.switch(opc)

    # opciones menu principal
    def switch(self,opc):
        if opc == 1:
            os.system('cls')
            self.menuLugar.mostrarMenu()
            return
        elif opc == 2:
            os.system('cls')
            self.menuVehiculo.cuota = self.menuCuota.cuota
            self.menuVehiculo.mostrarMenu()
            return
        elif opc == 3:
            os.system('cls')
            self.menuCuota.mostrarMenu()
            return
    
    #validar entrda de opciones de menu
    def validarMenu(self,opc):
        os.system('cls')
        while True: 
            if len(opc) == 1: 
                if opc.isdigit():
                    numero = int(opc)
                    if numero >= 1 and numero <= 4:
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