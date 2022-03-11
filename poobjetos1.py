def main():
    class persona():
        def _init_(self):
            self.nombre = input ("digite su nombre:")
            self.apellido = input ("digite su apellido:")
            self.direccion = input ("digite su direccion:")
        def mostrarPersona(self):
         print(f"nombre: {self.nombre}   {self.apellido}")

    #persona1=persona()
    #persona1.mostrarPersona()
    #persona2=persona()
    #persona2.mostrarPersona()



    class empleado(persona):
        def _init_(self):
            super()._init_()
            #guion bajo sirve para proteger los datos 
            self.__sueldo=float(input("ingrese el sueldo"))
            self.alimentacion=0
            self.transporte=0
            self.pension=0

        def mostrarempleado(self):
            super() .mostrarpersona()
            print(f"sueldo:{self.sueldo}") 
            print(f"transporte:{self.transporte}") 
            print(f"alimentacion:{self.alimentacion}") 
            print(f"pension:{self.pension}")
            
               
    empleado1 = empleado() 
    empleado1.mostrarempleado()










if __name__ == "__main__":
        main()

