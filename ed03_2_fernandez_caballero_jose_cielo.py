"""Depuración de código de python."""
import math

import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
Logger = logging.getLogger('CalculadoraCientifica')
Logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('calculadora.log')
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
Logger.addHandler(file_handler)
Logger.addHandler(console_handler)

class CalculadoraCientifica:
    """Clase de calculadora científica"""
    def __init__(self):
        Logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Se esperaba un número, se recibió {type(num)}")
    # Operaciones básicas
    def sumar(self,a,b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        Logger.info("Sumando %d + %d", a, b)
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        Logger.info("Restando %d - %d", a, b)
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        Logger.info("Multiplicando %d * %d", a, b)
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            Logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        Logger.info("Dividiendo %d / %d", a, b)
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        Logger.info("Calculando %d ^ %d",base,exponente)
        return math.pow(base, exponente)
    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            Logger.error("Intento de calcular raíz cuadrada de número negativo: %d",numero)
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        Logger.info("Calculando raíz cuadrada de %d",numero)
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            Logger.error("Intento de calcular logaritmo de número no positivo: %d",numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        Logger.info("Calculando logaritmo natural de %d",numero)
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            Logger.error("Intento de calcular logaritmo base 10 de número no positivo: %d",numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        Logger.info("Calculando logaritmo base 10 de %d",numero)
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        Logger.info("Calculando seno de %d radianes",angulo)
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        Logger.info("Calculando coseno de %d radianes",angulo)
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        Logger.info("Calculando tangente de %d radianes",angulo)
        return math.tan(angulo)

def main():
    """Clase Main"""

    # Crear instancia de la calculadora
    calc = CalculadoraCientifica()

    try:
        print("\n=== Calculadora Científica ===")
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Logaritmo natural")
        print("8. Logaritmo base 10")
        print("9. Seno")
        print("10. Coseno")
        print("11. Tangente")

        opcion = int(input("Ingrese el número de la operación deseada: "))

        if opcion in [1, 2, 3, 4, 5]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if opcion == 1:
                print(f"Resultado: {calc.sumar(a, b)}")
            elif opcion == 2:
                print(f"Resultado: {calc.restar(a, b)}")
            elif opcion == 3:
                print(f"Resultado: {calc.multiplicar(a, b)}")
            elif opcion == 4:
                print(f"Resultado: {calc.dividir(a, b)}")
            elif opcion == 5:
                print(f"Resultado: {calc.potencia(a, b)}")
        elif opcion in [6, 7, 8]:
            numero = float(input("Ingrese el número: "))
            if opcion == 6:
                print(f"Resultado: {calc.raiz_cuadrada(numero)}")
            elif opcion == 7:
                print(f"Resultado: {calc.logaritmo_natural(numero)}")
            elif opcion == 8:
                print(f"Resultado: {calc.logaritmo_base_10(numero)}")
        elif opcion in [9, 10, 11]:
            angulo = float(input("Ingrese el ángulo en radianes: "))
            if opcion == 9:
                print(f"Resultado: {calc.seno(angulo)}")
            elif opcion == 10:
                print(f"Resultado: {calc.coseno(angulo)}")
            elif opcion == 11:
                print(f"Resultado: {calc.tangente(angulo)}")
        else:
            print("Opción no válida")

    except ValueError as e:
        Logger.error("Error de valor: %d",e)
        print("Error de valor: %d",e)
    except TypeError as e:
        Logger.error("Error de tipo: %d",e)
        print("Error de tipo: %d",e)
    except ImportError as e:
        Logger.error("Error inesperado: %d",e)
        print("Error inesperado: %d",e)

if __name__ == "__main__":

    main()
