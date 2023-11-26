"""
Desarrollaremos una función que reciba un número entero y retorne el monto escrito en letras en inglés.
"""


# Definimos los valores de las unidades
unidades = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Definimos los valores de las decenas
decenas = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
# Definimos los valores de las decenas especiales
decenas_especiales = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                        "seventeen", "eighteen", "nineteen"]
# Definimos los valores de los grupos
grupos = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", 
            "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", 
            "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", 
            "septendecillion", "octodecillion", "novemdecillion", "vigintillion"]

# Definimos la función
def monto(numero):
    # Si el número es cero
    if numero == 0:
        return "zero"
    # Definimos la función que convierte un grupo de 3 dígitos en letras
    def grupo(numero):
        # Definimos la función que convierte un número de 2 dígitos en letras
        def decena(numero):
            # Si el número es menor a 10
            if numero < 10:
                # Retornamos el valor de las unidades
                return unidades[numero]
            # Si el número es menor a 20
            elif numero < 20:
                # Retornamos el valor de las decenas especiales
                return decenas_especiales[numero % 10]
            # Si el número es menor a 100
            elif numero < 100:
                # Retornamos el valor de las decenas
                return decenas[numero // 10] + (" " + unidades[numero % 10] if numero % 10 != 0 else "")
        
        # Si el número es menor a 100
        if numero < 100:
            # Retornamos el valor de las decenas
            return decena(numero)
        # Si el número es menor a 1000
        elif numero < 1000:
            # Retornamos el valor de las unidades
            return unidades[numero // 100] + " hundred" + (" " + decena(numero % 100) if numero % 100 != 0 else "")

    # Ahora debemos aplicar la función de manera recursiva para cada grupo de 3 dígitos
    # Convertimos el número a una cadena de texto
    numero = str(numero)
    # Definimos la lista de grupos
    grupos_numero = []
    # Definimos el contador de grupos
    contador = 0
    # Definimos el ciclo
    while numero:
        # Agregamos el grupo a la lista
        grupos_numero.append(grupo(int(numero[-3:])))
        # Eliminamos el grupo de la cadena de texto
        numero = numero[:-3]
        # Aumentamos el contador
        contador += 1
    # Definimos la lista de grupos en letras
    grupos_letras = []
    # Definimos el ciclo
    for i in range(len(grupos_numero)):
        # Si el grupo es diferente de cero
        if grupos_numero[i] != "":
            # Agregamos el grupo a la lista
            grupos_letras.append(grupos_numero[i] + " " + grupos[i])
    return ", ".join(grupos_letras[::-1]) # El uso de [::-1] es para invertir la lista y .join() para unir los elementos de la lista con una coma y un espacio

#Pruebas
print(monto(123456712))
print(monto(1000000000))
print(monto(1000000000000))
print(monto(0))
