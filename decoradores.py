def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # acciones adicionales
        print("Se realiza un cálculo")
        funcion_parametro()
        print("Se termina el cálculo")
    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)



suma()
resta()
