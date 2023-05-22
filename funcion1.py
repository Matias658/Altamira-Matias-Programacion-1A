#1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto 
#y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.


try:
    precio = float(input("Ingrese el precio: "))
except ValueError:
    print("Ese no es un número")

def aplicar_aumento(precio:float):
    aumento = precio * 5 / 100
    precio = precio + aumento
    return precio

precio_final = aplicar_aumento(precio)
print(precio_final)