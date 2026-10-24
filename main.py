import os

# Códigos de colores ANSI para la consola de Pydroid 3
# Nota: La consola de texto simula el fondo rojo y el logo A+ al inicio
ROJO_BG = "\033[41m"
AZUL_VIVO = "\033[94m"
AZUL_OSCURO = "\033[34m"
TURQUESA = "\033[96m"
BLANCO = "\033[97m"
NEGRO = "\033[30m"
RESET = "\033[0m"


def limpiar_pantalla():
  os.system("cls" if os.name == "nt" else "clear")


def mostrar_logo_y_bienvenida():
  # Simulamos el logo con fondo rojo, A azul vivo y + blanco
  print(f"{ROJO_BG}{BLANCO}======================================{RESET}")
  print(
      f"{ROJO_BG}      {AZUL_VIVO}  A  {BLANCO}+  {ROJO_BG}                   "
      f"   {RESET}"
  )
  print(f"{ROJO_BG}{BLANCO}======================================{RESET}")
  print(f"{AZUL_ELECTRIC}%s+CLASSNOTE+{RESET}" % TURQUESA)
  print(
      f"{BLANCO}Adelante, esto es +CLASSNOTE+ una calculadora hecha por"
      f" Ángel.{RESET}\n"
  )


# Definimos azul eléctrico usando turquesa brillante/azul
AZUL_ELECTRIC = "\033[1;96m"


def calculadora():
  while True:
    limpiar_pantalla()
    mostrar_logo_y_bienvenida()

    print(f"{AZUL_OSCURO}--- MENÚ DE OPERACIONES ---{RESET}")
    print(f"{TURQUESA}1.{RESET} Suma (+)")
    print(f"{TURQUESA}2.{RESET} Resta (-)")
    print(
        f"{TURQUESA}3.{RESET} Multiplicación (Estilo (8)(8) o normal)"
    )
    print(f"{TURQUESA}4.{RESET} División (/)")
    print(f"{TURQUESA}5.{RESET} Porcentaje (%)")
    print(f"{TURQUESA}6.{RESET} Promedio")
    print(f"{TURQUESA}7.{RESET} Lógica booleana avanzada")
    print(f"{TURQUESA}8.{RESET} Salir")

    opcion = input(f"\n{BLANCO}Ingresa amablemente el número:{RESET} ")

    if opcion == "1":
      print(f"\n{AZUL_ELECTRIC}=== SUMA ==={RESET}")
      a = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      b = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      print(f"{TURQUESA}Resultado: {a} + {b} = {a + b}{RESET}")

    elif opcion == "2":
      print(f"\n{AZUL_ELECTRIC}=== RESTA ==={RESET}")
      a = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      b = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      print(f"{TURQUESA}Resultado: {a} - {b} = {a - b}{RESET}")

    elif opcion == "3":
      print(f"\n{AZUL_ELECTRIC}=== MULTIPLICACIÓN ==={RESET}")
      print(
          f"{BLANCO}Puedes simular formato tipo (8)(8) ingresando dos"
          f" valores:{RESET}"
      )
      a = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      b = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      print(f"{TURQUESA}Resultado: ({a})({b}) = {a * b}{RESET}")

    elif opcion == "4":
      print(f"\n{AZUL_ELECTRIC}=== DIVISIÓN ==={RESET}")
      a = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      b = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      if b != 0:
        print(f"{TURQUESA}Resultado: {a} / {b} = {a / b}{RESET}")
      else:
        print(f"{ROJO_BG}{BLANCO}Error: No se puede dividir entre cero.{RESET}")

    elif opcion == "5":
      print(f"\n{AZUL_ELECTRIC}=== PORCENTAJE ==={RESET}")
      cantidad = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      porcentaje = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
      res = (cantidad * porcentaje) / 100
      print(
          f"{TURQUESA}El {porcentaje}% de {cantidad} es: {res}{RESET}"
      )

    elif opcion == "6":
      print(f"\n{AZUL_ELECTRIC}=== PROMEDIO ==={RESET}")
      n = int(
          input(
              f"{BLANCO}Ingresa amablemente el número (de elementos):{RESET} "
          )
      )
      suma_total = 0
      for i in range(n):
        val = float(input(f"{BLANCO}Ingresa amablemente el número:{RESET} "))
        suma_total += val
      prom = suma_total / n if n > 0 else 0
      print(f"{TURQUESA}El promedio es: {prom}{RESET}")

    elif opcion == "7":
      print(f"\n{AZUL_ELECTRIC}=== LÓGICA (Ejemplo: not((34 > 56 or 23 < 24) and 45)) ==={RESET}")
      print(f"{BLANCO}Evaluando expresión por defecto solicitada:{RESET}")
      # En Python, un número entero como 45 se evalúa como True en contextos booleanos
      expresion = not ((34 > 56 or 23 < 24) and 45)
      print(f"{TURQUESA}Expresión: not((34 > 56 or 23 < 24) and 45){RESET}")
      print(f"{TURQUESA}Resultado lógico: {expresion}{RESET}")

    elif opcion == "8":
      print(f"\n{AZUL_ELECTRIC}¡Gracias por usar +CLASSNOTE+! Hasta pronto.{RESET}")
      break
    else:
      print(f"{ROJO_BG}{BLANCO}Opción no válida. Inténtalo de nuevo.{RESET}")

    input(f"\n{BLANCO}Presiona Enter para continuar...{RESET}")


if __name__ == "__main__":
  calculadora()
