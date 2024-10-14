# Función para contar las veces que se repite un elemento en la lista
def contar_elemento(lista, elemento):
    return lista.count(elemento)


# Función para eliminar duplicados
def eliminar_duplicados(lista):
    return list(set(lista))


# Función principal
def main():
    # Ingresar elementos en la lista en una sola línea, separados por espacios
    lista = input("Ingresa los elementos de la lista separados por espacios: ").split()

    # Mostrar la lista original
    print("Lista:", lista)

    # Preguntar por el elemento a buscar
    elemento_buscar = input("¿Qué elemento deseas buscar?: ")

    # Contar cuántas veces se repite el elemento
    repeticiones = contar_elemento(lista, elemento_buscar)
    print(f"El elemento '{elemento_buscar}' se repite {repeticiones} veces.")

    # Eliminar duplicados
    lista_sin_duplicados = eliminar_duplicados(lista)
    print("Lista sin duplicados:", lista_sin_duplicados)


# Ejecutar el programa
if __name__ == "__main__":
    main()
