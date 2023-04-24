import os

class MenuCuota:
    #constructor
    def __init__(self):
        self.cuota = None

    def mostrarMenu(self):
        while True:
            print("\t---GESTIONAR CUOTA DE COBRO---\n")
            print("1. Establecer cuota por hora")
            print("2. Regresar")
            #ingresar opcion
            opc = self.validarMenu(input("\nPor favor, elige una opcion: "))
            #regresar a menu principal si opc = 2
            if opc == 2:
                os.system('cls')
                break
            #switch de opciones
            self.switch(opc)

    def switch(self,opc):
        if opc == 1:
            os.system('cls')
            regresar = True
            while regresar:
                print("\t---ESTABLECER CUOTA POR HORA---\n")
                cuota1 = "Indefinido" if self.cuota == None else self.cuota
                print("\nValor actual de la cuota: ",cuota1,"\n")
                cuota = self.validarNumero(input("Ingresar valor de cuota: "))
                print("\n")
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
                    if numero >=1 and numero <=2:
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
    
    def validarNumero(self,dato):
        while True: 
            try:
                numero = float(dato)
                self.cuota = numero
                print("\nLa cuota a cobrar sera: ",self.cuota)
                return numero
            except ValueError:
                print("\nPor favor, ingresa un valor numérico válido.")
                break