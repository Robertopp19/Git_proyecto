class HistorialNavegador:
    def __init__(self):
        self.historial = []  # Usamos una lista como pila para el historial

    def agregar_url(self, url, fecha_hora):
        """Agrega una URL al historial junto con la fecha y hora."""
        self.historial.append((url, fecha_hora))  # Agregar tupla (url, fecha y hora) a la pila
        print(f"Se ha agregado: {url} en la fecha y hora {fecha_hora} al historial")

    def eliminar_ultima_vista(self):
        """Elimina la última URL vista (el elemento más reciente) del historial."""
        if not self.historial_vacio():
            ultima_vista = self.historial.pop()  # Elimina el último elemento agregado (LIFO)
            print(f"Se ha eliminado: {ultima_vista[0]} del {ultima_vista[1]}")
        else:
            print("El historial está vacío")

    def historial_vacio(self):
        """Verifica si el historial está vacío."""
        return len(self.historial) == 0

    def mostrar_historial(self):
        """Muestra todo el historial de navegación."""
        if self.historial_vacio():
            print("El historial está vacío.")
        else:
            print("Historial de navegación:")
            for url, fecha_hora in reversed(self.historial):
                print(f"{url} - {fecha_hora}")


def menu():
    historial = HistorialNavegador()

    while True:
        print("\n--- Menú de Historial del Navegador ---")
        print("1. Agregar URL")
        print("2. Mostrar historial")
        print("3. Eliminar última URL")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            # Agregar URL
            url = input("Ingresa la URL: ")
            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            hora = input("Ingresa la hora (HH:MM): ")
            fecha_hora = f"{fecha} {hora}"
            historial.agregar_url(url, fecha_hora)

        elif opcion == "2":
            # Mostrar historial
            historial.mostrar_historial()

        elif opcion == "3":
            # Eliminar la última página vista
            if not historial.historial_vacio():
                historial.eliminar_ultima_vista()
            else:
                print("No hay URLs para eliminar.")

        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar el menú
menu()
