#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
#un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo 
#parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena


texto_prueba = "Hola soy Matias Altamira y hola estoy haciendo un parcial de programacion jaja".lower()

primera_caracter = input("Ingrese el primer caracter: ")
segundo_caracter = input("Ingrese el segundo caracter: ")


def reemplazar_caracteres(cadena:str, caracter1:str, caracter2:str):
    contador = 0
    cadena_separada = cadena.split()
    for i in cadena_separada:
        cadena = cadena.replace(primera_caracter, segundo_caracter)
        if i == caracter1:
            contador += 1
    print(cadena,"\n", contador)

reemplazar_caracteres(texto_prueba, primera_caracter, segundo_caracter)