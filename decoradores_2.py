def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        # acciones adicionales
        print("Se realiza un cálculo")
        funcion_parametro(*args, **kwargs)
        print("Se termina el cálculo")
    return funcion_interior

@funcion_decoradora
def suma(a, b):
    print(a+b)

@funcion_decoradora
def resta(a, b):
    print(a-b)


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))




suma(15, 20)
resta(30,10)
potencia(base=5,exponente=3)
