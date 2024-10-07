arreglo = []

def mostrar_arreglo():
    print("Arreglo actual:", arreglo)

def insertar_elemento():
    elemento = input("Ingresa el elemento a insertar: ")
    arreglo.append(elemento)
    print(f"Elemento '{elemento}' agregado.")
    mostrar_arreglo()

def modificar_elemento():
    if len(arreglo) == 0:
        print("El arreglo está vacío, no se puede modificar.")
    else:
        mostrar_arreglo()
        index = int(input("Ingresa el índice del elemento a modificar: "))
        if 0 <= index < len(arreglo):
            nuevo_elemento = input("Ingresa el nuevo valor: ")
            arreglo[index] = nuevo_elemento
            print("Elemento modificado.")
            mostrar_arreglo()
        else:
            print("Índice no válido.")

def eliminar_elemento():
    if len(arreglo) == 0:
        print("El arreglo está vacío, no se puede eliminar.")
    else:
        mostrar_arreglo()
        index = int(input("Ingresa el índice del elemento a eliminar: "))
        if 0 <= index < len(arreglo):
            eliminado = arreglo.pop(index)
            print(f"Elemento '{eliminado}' eliminado.")
            mostrar_arreglo()
        else:
            print("Índice no válido.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ver elementos")
        print("2. Agregar elemento")
        print("3. Modificar elemento")
        print("4. Eliminar elemento")
        print("5. Salir")

        opcion = input("Seleccionar opción: ")

        if opcion == '1':
            mostrar_arreglo()
        elif opcion == '2':
            insertar_elemento()
        elif opcion == '3':
            modificar_elemento()
        elif opcion == '4':
            eliminar_elemento()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción no existe. Por favor, selecciona una opción válida.")

menu()
