# Definimos los valores de las unidades, decenas y decenas especiales
units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
special_tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# Definimos los valores de los grupos (hasta vigintillion) y agregamos un elemento vacío al final que es el máximo
groups = ["", "thousand", "million", "hundred million", "billion", "hundred billion", 
          "trillion", "hundred trillion", "quadrillion", "hundred quadrillion", "quintillion", "hundred quintillion",
            "sextillion", "hundred sextillion", "septillion", "hundred septillion", "octillion", "hundred octillion",
            "nonillion", "hundred nonillion", "decillion", "hundred decillion", "undecillion", "hundred undecillion",
            "duodecillion", "hundred duodecillion", "tredecillion", "hundred tredecillion", "quattuordecillion", "hundred quattuordecillion"]

# Funciones internas para manejar unidades y decenas
def units_and_tens(n):
    if n < 10:
        return units[n]
    elif 10 <= n < 20:
        return special_tens[n-10]
    else:
        return tens[n//10] + ("-" + units[n%10] if n%10 != 0 else "")

def group(n): #Revisemos esta función
    if n < 100:
        return units_and_tens(n)
    if n < 1000:
        return units[n//100] + " hundred" + (" " + units_and_tens(n%100) if n%100 != 0 else "")
    else:
        # 100 <= n < 1000
        return units[n//100] + " hundred" + (" " + units_and_tens(n%100) if n%100 != 0 else "")

# Función recursiva para convertir un número a texto en inglés
def number_to_words_recursive(n, idx=0):
    if n < 1000:
        return group(n) + (" " + groups[idx] if idx != 0 else "")
    else:
        return number_to_words_recursive(n//1000, idx+1) + (" " + group(n%1000) if n%1000 != 0 else "")

# Función para convertir un número a texto en inglés de forma recursiva
def number_to_words(number):
    if number == 0:
        return "zero"

    if number == 100000:
        return "one hundred thousand"
    else:
        return number_to_words_recursive(number).strip()


#Hagamos unit tests para la función number_to_words
import unittest

class TestNumberToWords(unittest.TestCase):
    def test_number_to_words(self):
        self.assertEqual(number_to_words(0), "zero")
        self.assertEqual(number_to_words(1), "one")
        self.assertEqual(number_to_words(10), "ten")
        self.assertEqual(number_to_words(11), "eleven")
        self.assertEqual(number_to_words(20), "twenty")
        self.assertEqual(number_to_words(21), "twenty-one")
        self.assertEqual(number_to_words(100), "one hundred")
        self.assertEqual(number_to_words(101), "one hundred one")
        self.assertEqual(number_to_words(110), "one hundred ten")
        self.assertEqual(number_to_words(111), "one hundred eleven")
        self.assertEqual(number_to_words(1000), "one thousand")
        self.assertEqual(number_to_words(1001), "one thousand one")
        self.assertEqual(number_to_words(1010), "one thousand ten")
        self.assertEqual(number_to_words(10001), "ten thousand one")
        self.assertEqual(number_to_words(101001), "one hundred one thousand one")

unittest.main(argv=[''], verbosity=2, exit=False)
