
# Sistema de Gestión de Contenedores en Puerto Marítimo
class Stack:
    def __init__(self):

        self.items = []

    def is_empty(self):

        return len(self.items) == 0

    def push(self, item):

        self.items.append(item)

    def pop(self):

        if self.is_empty():
            return None
        return self.items.pop()

    def top(self):

        if self.is_empty():
            return None
        return self.items[-1]

    def print_stack(self):

        if self.is_empty():
            print("\n[ El patio está vacío ]")
        else:
            print("\n--- Estado de la Pila (Arriba -> Abajo) ---")
            for item in reversed(self.items):
                print(f"| {item} |")
            print("-------------------------------------------")

# Programa Principal

def main():
    pila_puerto = Stack()

    while True:
        print("\n===== Sistema de Gestión de Contenedores =====")
        print("1. Cargar contenedor (Push)")
        print("2. Descargar contenedor (Pop)")
        print("3. Ver contenedor superior (Top)")
        print("4. Mostrar estado completo de la pila")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            codigo_contenedor = input("Ingrese el código del contenedor: ").strip()
            if codigo_contenedor == "":
                print("Código inválido.")
            else:
                pila_puerto.push(codigo_contenedor)
                print(f"Contenedor '{codigo_contenedor}' cargado correctamente.")

        elif opcion == "2":
            contenedor_retirado = pila_puerto.pop()
            if contenedor_retirado is None:
                print("Advertencia: No hay contenedores para descargar. El patio está vacío.")
            else:
                print(f"Contenedor '{contenedor_retirado}' descargado correctamente.")

        elif opcion == "3":
            contenedor_superior = pila_puerto.top()
            if contenedor_superior is None:
                print("El patio está vacío. No hay contenedor superior.")
            else:
                print(f"Contenedor superior: {contenedor_superior}")

        elif opcion == "4":
            pila_puerto.print_stack()

        elif opcion == "5":
            print("Saliendo del sistema. Hasta luego.")
            break

        else:
            print("Opción inválida. Por favor seleccione un número del 1 al 5.")


if __name__ == "__main__":
    main()
