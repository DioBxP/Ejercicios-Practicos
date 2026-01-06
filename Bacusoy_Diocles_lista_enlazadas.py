"""

Materia: Estructura de Datos
Tema: LISTA SIMPLEMENTE ENLAZADA
Estudiante: Diocles Miguel Bacusoy Piguave
Curso: " C " 3er
Fecha: 19/12/2025

"""

"""
EJERCICIO 1: Contar elementos
Dificultad: Básico

Implementa un método count(elem) en SLinkedList que cuente cuántas veces
aparece un elemento en la lista.

Ejemplo:
    lista = [1, 2, 3, 2, 4, 2]
    lista.count(2)  # Retorna: 3
    lista.count(5)  # Retorna: 0
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        El head apunta a None cuando la lista no tiene elementos.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo de la lista.
            """
            self.head = nuevo
        else:
            """
            Si la lista no está vacía, se recorre la lista
            hasta llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo creado.
            """
            actual.next = nuevo

    def count(self, elem):
        """
        Cuenta cuántas veces aparece un elemento en la lista.

        Se recorre la lista nodo por nodo comparando el dato
        de cada nodo con el elemento buscado. Cada coincidencia
        incrementa el contador.
        """
        contador = 0
        actual = self.head

        while actual:
            """
            Se verifica si el dato del nodo actual coincide
            con el elemento que se desea contar.
            """
            if actual.dato == elem:
                contador += 1

            """
            Se avanza al siguiente nodo de la lista.
            """
            actual = actual.next

        """
        Se retorna el número total de ocurrencias encontradas.
        """
        return contador


print("\n================ EJERCICIO 1 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [0, 2, 3, 2, 4, 2]:
    lista1.agregar(x)
print(lista1.count(2))  # Esperado: 3

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [5, 5, 5, 5]:
    lista2.agregar(x)
print(lista2.count(5))  # Esperado: 4

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in [1, 3, 4, 6]:
    lista3.agregar(x)
print(lista3.count(2))  # Esperado: 0



"""
EJERCICIO 2: Obtener elemento por índice
Dificultad: Básico

Implementa un método get(index) que retorne el elemento en la posición index.

Ejemplo:
    lista = ['A', 'B', 'C', 'D']
    lista.get(0)   # Retorna: 'A'
    lista.get(2)   # Retorna: 'C'
    lista.get(10)  # Lanza: IndexError
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo de la lista.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo creado.
            """
            actual.next = nuevo

    def get(self, index):
        """
        Retorna el elemento ubicado en la posición indicada
        por el índice.

        Lanza IndexError si el índice es negativo o si está
        fuera del rango de la lista.
        """
        if index < 0:
            """
            Un índice negativo no es válido.
            """
            raise IndexError("Índice fuera de rango")

        actual = self.head
        contador = 0

        while actual:
            """
            Se recorre la lista comparando el contador con
            el índice solicitado.
            """
            if contador == index:
                return actual.dato

            """
            Se avanza al siguiente nodo e incrementa el contador.
            """
            actual = actual.next
            contador += 1

        """
        Si se recorre toda la lista sin encontrar el índice,
        se lanza la excepción correspondiente.
        """
        raise IndexError("Índice fuera de rango")


print("\n================ EJERCICIO 2 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in ['A', 'B', 'C', 'D']:
    lista1.agregar(x)
print(lista1.get(0))   # Esperado: 'A'

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in ['A', 'B', 'C', 'D']:
    lista2.agregar(x)
print(lista2.get(2))   # Esperado: 'C'

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in ['A', 'B', 'C', 'D']:
    lista3.agregar(x)
try:
    print(lista3.get(10))
except IndexError as e:
    print(e)



"""
EJERCICIO 3: Encontrar índice de elemento
Dificultad: Básico

Implementa un método index_of(elem) que retorne el índice de la primera
ocurrencia del elemento, o -1 si no existe.

Ejemplo:
    lista = ['A', 'B', 'C', 'B', 'D']
    lista.index_of('B')  # Retorna: 1 (primera ocurrencia)
    lista.index_of('D')  # Retorna: 4
    lista.index_of('Z')  # Retorna: -1
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Guarda el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo de la lista.
            """
            self.head = nuevo
        else:
            """
            Si la lista tiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo creado.
            """
            actual.next = nuevo

    def index_of(self, elem):
        """
        Retorna el índice de la primera ocurrencia del elemento
        buscado dentro de la lista.

        Si el elemento no existe, retorna -1.
        """
        actual = self.head
        indice = 0

        while actual:
            """
            Se compara el dato del nodo actual con el elemento
            buscado. Si coinciden, se retorna el índice actual.
            """
            if actual.dato == elem:
                return indice

            """
            Se avanza al siguiente nodo y se incrementa el índice.
            """
            actual = actual.next
            indice += 1

        """
        Si se recorre toda la lista y no se encuentra el elemento,
        se retorna -1.
        """
        return -1


print("\n================ EJERCICIO 3 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in ['A', 'B', 'C', 'B', 'D']:
    lista1.agregar(x)
print(lista1.index_of('B'))   # Resultado esperado: 1

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in ['A', 'B', 'C', 'B', 'D']:
    lista2.agregar(x)
print(lista2.index_of('D'))   # Resultado esperado: 4

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in ['A', 'B', 'C', 'B', 'D']:
    lista3.agregar(x)
print(lista3.index_of('Z'))   # Resultado esperado: -1



"""
EJERCICIO 4: Lista a array
Dificultad: Básico

Implementa un método to_list() que convierta la lista enlazada a una
lista de Python (array).

Ejemplo:
    linked_list = SLinkedList con [1, 2, 3, 4]
    linked_list.to_list()  # Retorna: [1, 2, 3, 4]
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo de la lista.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo creado.
            """
            actual.next = nuevo

    def to_list(self):
        """
        Convierte la lista enlazada en una lista de Python.

        Recorre la lista nodo por nodo y agrega cada dato
        al arreglo resultante.
        """
        resultado = []
        actual = self.head

        while actual:
            """
            Se añade el dato del nodo actual a la lista
            y se avanza al siguiente nodo.
            """
            resultado.append(actual.dato)
            actual = actual.next

        """
        Se retorna la lista de Python con todos los elementos.
        """
        return resultado


print("\n================ EJERCICIO 4 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 4]:
    lista1.agregar(x)
print(lista1.to_list())

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [10, 20]:
    lista2.agregar(x)
print(lista2.to_list())

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
print(lista3.to_list())

 

"""
EJERCICIO 5: Limpiar lista
Dificultad: Básico

Implementa un método clear() que elimine todos los elementos de la lista.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.clear()
    len(lista)  # Retorna: 0
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Guarda el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        El atributo size permite conocer la cantidad de elementos.
        """
        self.head = None
        self.size = 0

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada
        y actualiza el tamaño de la lista.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            el último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

        """
        Se incrementa el tamaño de la lista.
        """
        self.size += 1

    def clear(self):
        """
        Elimina todos los elementos de la lista enlazada.

        Para lograrlo, se elimina la referencia al primer nodo
        y se reinicia el tamaño de la lista.
        """
        self.head = None
        self.size = 0


print("\n================ EJERCICIO 5 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista1.agregar(x)
lista1.clear()
print(lista1.size)   # Resultado esperado: 0

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [10, 20]:
    lista2.agregar(x)
lista2.clear()
print(lista2.size)   # Resultado esperado: 0

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
lista3.clear()
print(lista3.size)   # Resultado esperado: 0




"""
EJERCICIO 6: Invertir lista
Dificultad: Intermedio

Implementa un método reverse() que invierta el orden de los elementos
EN LA MISMA LISTA (no crear una nueva).

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.reverse()
    print(lista)  # Output: 5 → 4 → 3 → 2 → 1 → None

Pista: Necesitas cambiar los punteros next de cada nodo.
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None
        self.size = 0

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

        """
        Se incrementa el tamaño de la lista.
        """
        self.size += 1

    def reverse(self):
        """
        Invierte el orden de los nodos de la lista enlazada
        modificando los punteros next de cada nodo.

        No se crea una nueva lista, la inversión se realiza
        directamente sobre la lista original.
        """
        anterior = None
        actual = self.head

        while actual:
            """
            Se guarda la referencia al siguiente nodo para
            no perder la lista original.
            """
            siguiente = actual.next

            """
            Se invierte el puntero del nodo actual para que
            apunte al nodo anterior.
            """
            actual.next = anterior

            """
            Se avanza el puntero anterior al nodo actual.
            """
            anterior = actual

            """
            Se avanza al siguiente nodo de la lista original.
            """
            actual = siguiente

        """
        Al finalizar el recorrido, el puntero 'anterior'
        queda apuntando al nuevo primer nodo de la lista,
        por lo que se actualiza el head.
        """
        self.head = anterior


print("\n================ EJERCICIO 6 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista1.agregar(x)
lista1.reverse()

actual = lista1.head
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.next
print("None")

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [10, 20]:
    lista2.agregar(x)
lista2.reverse()

actual = lista2.head
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.next
print("None")

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
lista3.reverse()

actual = lista3.head
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.next
print("None")



"""
EJERCICIO 7: Detectar ciclo
Dificultad: Intermedio

Implementa un método has_cycle() que detecte si la lista tiene un ciclo
(un nodo apunta a un nodo anterior, creando un bucle infinito).

Usa el algoritmo de Floyd (tortuga y liebre):
- Dos punteros: uno avanza 1 paso, otro avanza 2 pasos
- Si se encuentran, hay ciclo
- Si el rápido llega a None, no hay ciclo

Ejemplo:
    lista normal: 1 → 2 → 3 → None (retorna False)
    lista con ciclo: 1 → 2 → 3 → (vuelve a 2) (retorna True)
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

    def has_cycle(self):
        """
        Detecta si la lista enlazada contiene un ciclo
        utilizando el algoritmo de Floyd (tortuga y liebre).

        Retorna True si existe un ciclo, False en caso contrario.
        """
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            """
            El puntero lento avanza un nodo a la vez.
            """
            lento = lento.next

            """
            El puntero rápido avanza dos nodos a la vez.
            """
            rapido = rapido.next.next

            """
            Si ambos punteros se encuentran, existe un ciclo.
            """
            if lento == rapido:
                return True

        """
        Si el puntero rápido llega a None, no existe un ciclo.
        """
        return False


print("\n================ EJERCICIO 7 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3]:
    lista1.agregar(x)
print(lista1.has_cycle())   # Resultado esperado: False

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()

n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

lista2.head = n1
n1.next = n2
n2.next = n3
n3.next = n2   # Se crea el ciclo

print(lista2.has_cycle())   # Resultado esperado: True

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
print(lista3.has_cycle())   # Resultado esperado: False



"""
EJERCICIO 8: Encontrar el medio
Dificultad: Intermedio

Implementa un método get_middle() que retorne el elemento del medio de la lista.
Si hay número par de elementos, retorna el segundo del medio.

Usa el algoritmo de dos punteros:
- Un puntero lento (avanza 1 paso)
- Un puntero rápido (avanza 2 pasos)
- Cuando el rápido llega al final, el lento está en el medio

Ejemplo:
    [1, 2, 3, 4, 5] → retorna 3
    [1, 2, 3, 4] → retorna 3 (segundo del medio)
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

    def get_middle(self):
        """
        Retorna el elemento que se encuentra en la mitad
        de la lista enlazada.

        Si la lista tiene un número par de elementos,
        se retorna el segundo elemento del medio.
        """
        if not self.head:
            """
            Si la lista está vacía, no existe elemento medio.
            """
            return None

        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            """
            El puntero lento avanza un nodo.
            """
            lento = lento.next

            """
            El puntero rápido avanza dos nodos.
            """
            rapido = rapido.next.next

        """
        Cuando el puntero rápido llega al final de la lista,
        el puntero lento se encuentra en el nodo medio.
        """
        return lento.dato


print("\n================ EJERCICIO 8 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista1.agregar(x)
print(lista1.get_middle())   # Resultado esperado: 3

"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [1, 2, 3, 4]:
    lista2.agregar(x)
print(lista2.get_middle())   # Resultado esperado: 3

"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
print(lista3.get_middle())   # Resultado esperado: None
 



"""
EJERCICIO 9: Eliminar duplicados
Dificultad: Intermedio

Implementa un método remove_duplicates() que elimine todos los elementos
duplicados de la lista, dejando solo la primera ocurrencia de cada elemento.

Ejemplo:
    [1, 2, 3, 2, 4, 1, 5] → [1, 2, 3, 4, 5]

Versión 1: Usando un conjunto (set) auxiliar
Complejidad: O(n) tiempo, O(n) espacio
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista contiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

    def __str__(self):
        """
        Retorna una representación en forma de cadena
        de la lista enlazada para facilitar su visualización.
        """
        actual = self.head
        resultado = ""

        while actual:
            resultado += str(actual.dato) + " → "
            actual = actual.next

        return resultado + "None"

    def remove_duplicates(self):
        """
        Elimina los elementos duplicados de la lista enlazada,
        conservando únicamente la primera ocurrencia de cada valor.

        Se utiliza un conjunto (set) para almacenar los elementos
        que ya han sido vistos durante el recorrido.
        """
        vistos = set()
        actual = self.head
        anterior = None

        while actual:
            """
            Si el dato del nodo actual ya fue visto,
            se elimina el nodo ajustando el puntero del nodo anterior.
            """
            if actual.dato in vistos:
                anterior.next = actual.next
            else:
                """
                Si el dato no ha sido visto, se agrega al conjunto
                y se avanza el puntero anterior.
                """
                vistos.add(actual.dato)
                anterior = actual

            """
            Se avanza al siguiente nodo.
            """
            actual = actual.next


print("\n================ EJERCICIO 9 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 2, 4, 1, 5]:
    lista1.agregar(x)

print("Antes:")
print(lista1)

lista1.remove_duplicates()

print("Después:")
print(lista1)


"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [10, 10, 10, 10]:
    lista2.agregar(x)

print("Antes:")
print(lista2)

lista2.remove_duplicates()

print("Después:")
print(lista2)


"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in [1, 2, 3, 4]:
    lista3.agregar(x)

print("Antes:")
print(lista3)

lista3.remove_duplicates()

print("Después:")
print(lista3)



"""
EJERCICIO 10: Fusionar dos listas ordenadas
Dificultad: Intermedio

Implementa una función merge_sorted(list1, list2) que tome dos listas
enlazadas ORDENADAS y retorne una nueva lista enlazada también ordenada
con todos los elementos de ambas.

Ejemplo:
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merge_sorted(list1, list2) → [1, 2, 3, 4, 5, 6, 7, 8]

Pista: Usa dos punteros, uno para cada lista, y compara elementos.
"""

class Nodo:
    """
    Representa un nodo de una lista simplemente enlazada.
    Contiene un dato y una referencia al siguiente nodo.
    """
    def __init__(self, dato):
        """
        Inicializa el nodo con un valor y apunta al siguiente como None.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    """
    Implementación de una lista simplemente enlazada.
    Mantiene una referencia al primer nodo (head).
    """
    def __init__(self):
        """
        Crea una lista vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo con el dato recibido al final de la lista.
        """
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        """
        Devuelve una representación en texto de la lista enlazada.
        """
        actual = self.head
        resultado = ""
        while actual:
            resultado += str(actual.dato) + " → "
            actual = actual.next
        return resultado + "None"


def merge_sorted(list1, list2):
    """
    Combina dos listas simplemente enlazadas ordenadas
    en una nueva lista también ordenada.
    """
    nueva_lista = SLinkedList()

    p1 = list1.head
    p2 = list2.head

    """
    Recorre ambas listas comparando los valores
    y agregando el menor a la nueva lista.
    """
    while p1 and p2:
        if p1.dato <= p2.dato:
            nueva_lista.agregar(p1.dato)
            p1 = p1.next
        else:
            nueva_lista.agregar(p2.dato)
            p2 = p2.next

    """
    Agrega los elementos restantes de la primera lista,
    si aún quedan nodos.
    """
    while p1:
        nueva_lista.agregar(p1.dato)
        p1 = p1.next

    """
    Agrega los elementos restantes de la segunda lista,
    si aún quedan nodos.
    """
    while p2:
        nueva_lista.agregar(p2.dato)
        p2 = p2.next

    return nueva_lista


print("\n================ EJERCICIO 10 ================\n")

"""Caso 1"""
print("Caso 1:")
list1 = SLinkedList()
for x in [1, 3, 5, 7]:
    list1.agregar(x)

list2 = SLinkedList()
for x in [2, 4, 6, 8]:
    list2.agregar(x)

resultado = merge_sorted(list1, list2)
print(resultado)   # Esperado: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → None


"""Caso 2"""
print("\nCaso 2:")
list3 = SLinkedList()
for x in [1, 2, 3]:
    list3.agregar(x)

list4 = SLinkedList()
for x in [4, 5, 6]:
    list4.agregar(x)

resultado = merge_sorted(list3, list4)
print(resultado)   # Esperado: 1 → 2 → 3 → 4 → 5 → 6 → None


"""Caso 3"""
print("\nCaso 3:")
list5 = SLinkedList()

list6 = SLinkedList()
for x in [10, 20, 30]:
    list6.agregar(x)

resultado = merge_sorted(list5, list6)
print(resultado)   # Esperado: 10 → 20 → 30 → None




"""
EJERCICIO 11: Palíndromo
Dificultad: Avanzado

Implementa un método is_palindrome() que determine si la lista es un palíndromo
(se lee igual de adelante hacia atrás).

Ejemplo:
    [1, 2, 3, 2, 1] → True
    [1, 2, 3, 4, 5] → False

Solución eficiente:
1. Encuentra el medio (algoritmo de dos punteros)
2. Invierte la segunda mitad
3. Compara la primera mitad con la segunda mitad invertida
4. Restaura la segunda mitad (opcional)

Complejidad:
- Tiempo: O(n)
- Espacio: O(1)
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor de la clase Nodo.
        Guarda el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo se convierte
            en el primer nodo.
            """
            self.head = nuevo
        else:
            """
            Si la lista tiene elementos, se recorre hasta
            llegar al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            """
            Se enlaza el último nodo con el nuevo nodo.
            """
            actual.next = nuevo

    def __str__(self):
        """
        Retorna una representación en cadena de la lista
        enlazada para facilitar su visualización.
        """
        actual = self.head
        res = ""

        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next

        return res + "None"

    def is_palindrome(self):
        """
        Determina si la lista enlazada es un palíndromo.

        Retorna True si la lista se lee igual de adelante
        hacia atrás, False en caso contrario.
        """
        if not self.head or not self.head.next:
            """
            Una lista vacía o con un solo elemento
            siempre es un palíndromo.
            """
            return True

        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            """
            El puntero lento avanza un nodo.
            El puntero rápido avanza dos nodos.
            """
            lento = lento.next
            rapido = rapido.next.next

        prev = None
        actual = lento

        while actual:
            """
            Se invierte el puntero next de cada nodo
            de la segunda mitad.
            """
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        p1 = self.head
        p2 = prev   

        es_palindromo = True

        while p2:
            """
            Se comparan los datos de ambas mitades.
            """
            if p1.dato != p2.dato:
                es_palindromo = False
                break

            p1 = p1.next
            p2 = p2.next

        actual = prev
        prev = None

        while actual:
            """
            Se vuelve a invertir la segunda mitad
            para restaurar la lista original.
            """
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        return es_palindromo


print("\n================ EJERCICIO 11 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 2, 1]:
    lista1.agregar(x)

print(lista1)
print(lista1.is_palindrome())   # Resultado esperado: True


"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista2.agregar(x)

print(lista2)
print(lista2.is_palindrome())   # Resultado esperado: False


"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in [7]:
    lista3.agregar(x)

print(lista3)
print(lista3.is_palindrome())   # Resultado esperado: True



"""
EJERCICIO 12: Rotar lista
Dificultad: Avanzado

Implementa un método rotate(k) que rote la lista enlazada
k posiciones a la derecha.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.rotate(2)
    Resultado:
        4 → 5 → 1 → 2 → 3 → None

Pasos del algoritmo:
1. Conectar el último nodo con el primero (hacer la lista circular)
2. Encontrar el nuevo nodo cabeza en la posición (size - k)
3. Romper el enlace circular

Complejidad esperada:
- Tiempo: O(n)
- Espacio: O(1)
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor del nodo.
        Contiene el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None
        self.size = 0

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo
            se convierte en la cabeza.
            """
            self.head = nuevo
        else:
            """
            Si la lista tiene elementos, se recorre
            hasta el último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            actual.next = nuevo

        self.size += 1

    def __str__(self):
        """
        Retorna una representación visual de la lista.
        """
        actual = self.head
        res = ""

        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next

        return res + "None"

    def rotate(self, k):
        """
        Rota la lista k posiciones a la derecha.
        """
        if not self.head or self.size <= 1:
            """
            Si la lista está vacía o tiene un solo elemento,
            no es necesario rotar.
            """
            return

        """
        Se ajusta k en caso de que sea mayor
        que el tamaño de la lista.
        """
        k = k % self.size
        if k == 0:
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = self.head

        """
        El nuevo tail estará en la posición (size - k - 1)
        """
        pasos = self.size - k
        nuevo_tail = self.head

        for _ in range(pasos - 1):
            nuevo_tail = nuevo_tail.next

        self.head = nuevo_tail.next
        nuevo_tail.next = None


print("\n================ EJERCICIO 12 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista1.agregar(x)

print("Antes:")
print(lista1)

lista1.rotate(2)

print("Después:")
print(lista1)
# Esperado: 4 → 5 → 1 → 2 → 3 → None


"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [10, 20, 30, 40]:
    lista2.agregar(x)

print("Antes:")
print(lista2)

lista2.rotate(1)

print("Después:")
print(lista2)
# Esperado: 40 → 10 → 20 → 30 → None


"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in [7]:
    lista3.agregar(x)

print("Antes:")
print(lista3)

lista3.rotate(3)

print("Después:")
print(lista3)
# Esperado: 7 → None



"""
EJERCICIO 13: Particionar lista
Dificultad: Avanzado

Implementa un método partition(x) que reorganice la lista enlazada de modo que
todos los elementos menores que x aparezcan antes que los elementos mayores
o iguales a x.

El orden relativo de los elementos dentro de cada grupo debe preservarse.

Ejemplo:
    lista = [3, 5, 8, 5, 10, 2, 1]
    lista.partition(5)

    Resultado:
        [3, 2, 1] → [5, 8, 5, 10]
    (Cualquier resultado donde los menores a 5 estén primero es válido)

Pista:
- Crear dos listas auxiliares:
  una para los elementos menores a x
  y otra para los elementos mayores o iguales a x.
- Finalmente unir ambas listas.
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor del nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo
            se convierte en la cabeza.
            """
            self.head = nuevo
        else:
            """
            Se recorre la lista hasta llegar
            al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            actual.next = nuevo

    def __str__(self):
        """
        Retorna una representación visual de la lista.
        """
        actual = self.head
        res = ""

        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next

        return res + "None"

    def partition(self, x):
        """
        Reorganiza la lista de modo que todos los elementos
        menores que x aparezcan antes que los elementos
        mayores o iguales a x.
        """

        """
        Se crean las cabezas y colas de dos listas auxiliares:
        - menores: elementos < x
        - mayores: elementos >= x
        """
        menores_head = menores_tail = None
        mayores_head = mayores_tail = None

        actual = self.head

        while actual:
            """
            Se guarda la referencia al siguiente nodo
            antes de modificar enlaces.
            """
            siguiente = actual.next
            actual.next = None  # Desconectar el nodo actual

            if actual.dato < x:
                """
                Si el dato es menor que x,
                se agrega a la lista de menores.
                """
                if not menores_head:
                    menores_head = menores_tail = actual
                else:
                    menores_tail.next = actual
                    menores_tail = actual
            else:
                """
                Si el dato es mayor o igual que x,
                se agrega a la lista de mayores.
                """
                if not mayores_head:
                    mayores_head = mayores_tail = actual
                else:
                    mayores_tail.next = actual
                    mayores_tail = actual

            actual = siguiente

        """
        Se unen ambas listas.
        Si existen elementos menores, ellos serán la nueva cabeza.
        """
        if menores_tail:
            menores_tail.next = mayores_head
            self.head = menores_head
        else:
            """
            Si no hay elementos menores,
            la cabeza será la lista de mayores.
            """
            self.head = mayores_head


print("\n================ EJERCICIO 13 ================\n")

"""Caso 1"""
print("Caso 1:")
lista1 = SLinkedList()
for x in [3, 5, 8, 5, 10, 2, 1]:
    lista1.agregar(x)

print("Antes:")
print(lista1)

lista1.partition(5)

print("Después:")
print(lista1)
# Esperado: 3 → 2 → 1 → 5 → 8 → 5 → 10 → None


"""Caso 2"""
print("\nCaso 2:")
lista2 = SLinkedList()
for x in [1, 2, 3, 4]:
    lista2.agregar(x)

print("Antes:")
print(lista2)

lista2.partition(3)

print("Después:")
print(lista2)
# Esperado: 1 → 2 → 3 → 4 → None


"""Caso 3"""
print("\nCaso 3:")
lista3 = SLinkedList()
for x in [6, 7, 8]:
    lista3.agregar(x)

print("Antes:")
print(lista3)

lista3.partition(5)

print("Después:")
print(lista3)
# Esperado: 6 → 7 → 8 → None



"""
EJERCICIO 14: Suma de dos listas (números)
Dificultad: Avanzado

Se tienen dos listas enlazadas que representan números,
donde cada nodo contiene un solo dígito.

Los dígitos están almacenados en ORDEN INVERSO:
- El primer nodo representa la unidad.
- El segundo nodo representa las decenas, etc.

Implementa una función add_numbers(list1, list2) que sume ambos números
y retorne el resultado como una nueva lista enlazada.

Ejemplo:
    list1 = [2, 4, 3] representa el número 342
    list2 = [5, 6, 4] representa el número 465

    Resultado:
        [7, 0, 8] representa el número 807

Pista:
- Simula la suma manual dígito por dígito.
- Usa una variable "carry" para manejar el acarreo.
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor del nodo.
        Contiene un dígito y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista.
        """
        nuevo = Nodo(dato)

        if not self.head:
            """
            Si la lista está vacía, el nuevo nodo
            se convierte en la cabeza.
            """
            self.head = nuevo
        else:
            """
            Se recorre la lista hasta llegar
            al último nodo.
            """
            actual = self.head
            while actual.next:
                actual = actual.next

            actual.next = nuevo

    def __str__(self):
        """
        Retorna una representación visual de la lista.
        """
        actual = self.head
        res = ""

        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next

        return res + "None"


def add_numbers(list1, list2):
    """
    Suma dos números representados por listas enlazadas
    y retorna el resultado como una nueva lista enlazada.
    """
    resultado = SLinkedList()

    p1 = list1.head
    p2 = list2.head
    carry = 0

    while p1 or p2 or carry:
        """
        Se suma el acarreo junto con los dígitos actuales.
        """
        suma = carry

        if p1:
            suma += p1.dato
            p1 = p1.next

        if p2:
            suma += p2.dato
            p2 = p2.next

        """
        Se actualiza el acarreo y se guarda el dígito resultante.
        """
        carry = suma // 10
        resultado.agregar(suma % 10)

    return resultado


print("\n================ EJERCICIO 14 ================\n")

"""Caso 1"""
print("Caso 1:")
list1 = SLinkedList()
for x in [2, 4, 3]:   # 342
    list1.agregar(x)

list2 = SLinkedList()
for x in [5, 6, 4]:   # 465
    list2.agregar(x)

resultado = add_numbers(list1, list2)
print("Resultado:")
print(resultado)
# Esperado: 7 → 0 → 8 → None  (807)


"""Caso 2"""
print("\nCaso 2:")
list3 = SLinkedList()
for x in [9, 9, 9]:   # 999
    list3.agregar(x)

list4 = SLinkedList()
for x in [1]:         # 1
    list4.agregar(x)

resultado = add_numbers(list3, list4)
print("Resultado:")
print(resultado)
# Esperado: 0 → 0 → 0 → 1 → None  (1000)


"""Caso 3"""
print("\nCaso 3:")
list5 = SLinkedList()
for x in [0]:
    list5.agregar(x)

list6 = SLinkedList()
for x in [0]:
    list6.agregar(x)

resultado = add_numbers(list5, list6)
print("Resultado:")
print(resultado)
# Esperado: 0 → None



"""
EJERCICIO 15: Intersección de dos listas
Dificultad: Avanzado

Dadas dos listas enlazadas, se debe determinar si ambas se intersectan,
es decir, si comparten uno o más nodos en memoria, y encontrar el primer
nodo donde ocurre dicha intersección.

Ejemplo:
    list1: 1 → 2 → 3 ↘
                      7 → 8 → 9
    list2: 4 → 5 → 6 ↗

    Resultado:
        Nodo con valor 7 (primer nodo compartido)

Solución eficiente:
1. Calcular la longitud de ambas listas
2. Alinear los punteros de inicio avanzando en la lista más larga
3. Avanzar ambas listas simultáneamente hasta encontrar el nodo común

Complejidad:
- Tiempo: O(n + m)
- Espacio: O(1)
"""

class Nodo:
    def __init__(self, dato):
        """
        Constructor del nodo.
        Almacena el dato y la referencia al siguiente nodo.
        """
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        """
        Inicializa una lista simplemente enlazada vacía.
        """
        self.head = None

    def agregar(self, dato):
        """
        Agrega un nuevo nodo al final de la lista.
        """
        nuevo = Nodo(dato)

        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo


def longitud(lista):
    """
    Calcula y retorna la longitud de una lista enlazada.
    """
    actual = lista.head
    count = 0

    while actual:
        count += 1
        actual = actual.next

    return count


def get_intersection_node(list1, list2):
    """
    Retorna el nodo donde dos listas enlazadas se intersectan.
    Si no existe intersección, retorna None.
    """
    len1 = longitud(list1)
    len2 = longitud(list2)

    p1 = list1.head
    p2 = list2.head

    """
    Alinear los punteros de inicio.
    Se avanza en la lista más larga para que ambas
    tengan la misma cantidad de nodos restantes.
    """
    if len1 > len2:
        for _ in range(len1 - len2):
            p1 = p1.next
    else:
        for _ in range(len2 - len1):
            p2 = p2.next

    """
    Avanzar simultáneamente ambas listas.
    Se compara la referencia de los nodos (no el valor).
    """
    while p1 and p2:
        if p1 is p2:
            return p1
        p1 = p1.next
        p2 = p2.next

    return None


print("\n================ EJERCICIO 15 ================\n")

"""Caso 1"""
print("Caso 1: Listas con intersección")

# Nodos compartidos
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)

n7.next = n8
n8.next = n9

# Lista 1: 1 → 2 → 3 → 7 → 8 → 9
list1 = SLinkedList()
list1.head = Nodo(1)
list1.head.next = Nodo(2)
list1.head.next.next = Nodo(3)
list1.head.next.next.next = n7

# Lista 2: 4 → 5 → 6 → 7 → 8 → 9
list2 = SLinkedList()
list2.head = Nodo(4)
list2.head.next = Nodo(5)
list2.head.next.next = Nodo(6)
list2.head.next.next.next = n7

interseccion = get_intersection_node(list1, list2)

if interseccion:
    print("Nodo de intersección:", interseccion.dato)
else:
    print("No hay intersección")


"""Caso 2"""
print("\nCaso 2: Listas sin intersección")

list3 = SLinkedList()
for x in [1, 2, 3]:
    list3.agregar(x)

list4 = SLinkedList()
for x in [4, 5, 6]:
    list4.agregar(x)

interseccion = get_intersection_node(list3, list4)

if interseccion:
    print("Nodo de intersección:", interseccion.dato)
else:
    print("No hay intersección")


"""Caso 3"""
print("\nCaso 3: Una lista vacía")

list5 = SLinkedList()
list6 = SLinkedList()
list6.agregar(1)
list6.agregar(2)

interseccion = get_intersection_node(list5, list6)

if interseccion:
    print("Nodo de intersección:", interseccion.dato)
else:
    print("No hay intersección")



"""
EJERCICIO 16: Navegador Web
Dificultad: Intermedio

Se debe implementar una clase BrowserHistory que simule el historial
de navegación de un navegador web utilizando una lista doblemente enlazada.

Cada nodo representa una página web y mantiene referencias a:
- la página anterior (prev)
- la página siguiente (next)

Métodos requeridos:
- __init__(homepage): Inicializa el navegador con la página de inicio
- visit(url): Visita una nueva URL y elimina el historial futuro
- back(steps): Retrocede 'steps' páginas (hasta el inicio)
- forward(steps): Avanza 'steps' páginas (hasta el final)
- get_current(): Retorna la URL actual

Ejemplo:
    browser = BrowserHistory("google.com")
    browser.visit("youtube.com")
    browser.visit("facebook.com")
    browser.back(1)       # youtube.com
    browser.forward(1)    # facebook.com
"""

class Nodo:
    def __init__(self, url):
        """
        Nodo de la lista doblemente enlazada.
        Contiene la URL y referencias al nodo anterior y siguiente.
        """
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        """
        Inicializa el historial del navegador
        con la página de inicio.
        """
        self.current = Nodo(homepage)

    def visit(self, url):
        """
        Visita una nueva URL.
        Elimina todo el historial futuro y
        agrega la nueva página al final.
        """
        nuevo = Nodo(url)

        """
        Al visitar una nueva página, se elimina
        el historial futuro.
        """
        self.current.next = None

        """
        Se enlaza el nuevo nodo con el nodo actual.
        """
        nuevo.prev = self.current
        self.current.next = nuevo

        """
        Se actualiza la página actual.
        """
        self.current = nuevo

    def back(self, steps):
        """
        Retrocede 'steps' páginas en el historial.
        No puede retroceder más allá del inicio.
        """
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1

        return self.current.url

    def forward(self, steps):
        """
        Avanza 'steps' páginas en el historial.
        No puede avanzar más allá del final.
        """
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1

        return self.current.url

    def get_current(self):
        """
        Retorna la URL de la página actual.
        """
        return self.current.url


print("\n================ EJERCICIO 16 ================\n")

"""Caso 1"""
print("Caso 1: Navegación básica")

browser = BrowserHistory("google.com")

browser.visit("youtube.com")
browser.visit("facebook.com")
browser.back(1)
browser.forward(1)

print("Página actual:", browser.get_current())


"""Caso 2"""
print("\nCaso 2: Retroceder más pasos de los disponibles")

browser = BrowserHistory("inicio.com")

browser.visit("pagina1.com")
browser.visit("pagina2.com")
browser.visit("pagina3.com")

browser.back(10)   # intenta retroceder más de lo posible

print("Página actual:", browser.get_current())


"""Caso 3"""
print("\nCaso 3: Eliminar historial futuro al visitar nueva página")

browser = BrowserHistory("home.com")

browser.visit("a.com")
browser.visit("b.com")
browser.visit("c.com")

browser.back(2)     # vuelve a a.com
browser.visit("nueva.com")  # elimina historial futuro

browser.forward(1)  # no debería avanzar

print("Página actual:", browser.get_current())



"""
EJERCICIO 17: LRU Cache
Dificultad: Avanzado

Se debe implementar una estructura de datos LRU Cache (Least Recently Used),
la cual almacena pares clave–valor con una capacidad limitada.

Cuando el cache alcanza su capacidad máxima y se inserta un nuevo elemento,
se elimina el elemento menos recientemente utilizado.

Requisitos:
- get(key): O(1)
- put(key, value): O(1)

Estructuras usadas:
- Diccionario (hash map): acceso directo O(1)
- Lista doblemente enlazada: control del orden de uso

Reglas:
- El nodo más recientemente usado (MRU) se ubica al final de la lista
- El nodo menos recientemente usado (LRU) se ubica al inicio de la lista
"""

class Nodo:
    def __init__(self, key, value):
        """
        Nodo de la lista doblemente enlazada.
        Almacena clave, valor y referencias
        al nodo anterior y siguiente.
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        Inicializa el cache con una capacidad máxima.
        """
        self.capacity = capacity
        self.cache = {}   # Diccionario: key → nodo

        """
        Nodos ficticios (dummy) para simplificar operaciones.
        head.next  → LRU
        tail.prev  → MRU
        """
        self.head = Nodo(0, 0)
        self.tail = Nodo(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, nodo):
        """
        Elimina un nodo de la lista doblemente enlazada.
        """
        prev = nodo.prev
        next = nodo.next
        prev.next = next
        next.prev = prev

    def _add_to_end(self, nodo):
        """
        Agrega un nodo al final de la lista
        (marca como más recientemente usado).
        """
        prev = self.tail.prev
        prev.next = nodo
        nodo.prev = prev
        nodo.next = self.tail
        self.tail.prev = nodo

    def get(self, key):
        """
        Retorna el valor asociado a la clave.
        Si existe, el nodo se mueve al final (MRU).
        """
        if key not in self.cache:
            return -1

        nodo = self.cache[key]

        """
        Se mueve el nodo al final
        para marcarlo como usado recientemente.
        """
        self._remove(nodo)
        self._add_to_end(nodo)

        return nodo.value

    def put(self, key, value):
        """
        Inserta o actualiza un valor en el cache.
        Si el cache está lleno, elimina el LRU.
        """
        if key in self.cache:
            """
            Si la clave ya existe, se actualiza
            el valor y se mueve a MRU.
            """
            nodo = self.cache[key]
            nodo.value = value
            self._remove(nodo)
            self._add_to_end(nodo)
        else:
            """
            Si el cache está lleno, se elimina
            el nodo menos recientemente usado.
            """
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            """
            Se agrega el nuevo nodo.
            """
            nuevo = Nodo(key, value)
            self.cache[key] = nuevo
            self._add_to_end(nuevo)


print("\n================ EJERCICIO 17 ================\n")

"""Caso 1"""
print("Caso 1: Operaciones básicas")

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print("get(1):", cache.get(1))   # 10


"""Caso 2"""
print("\nCaso 2: Eliminación del menos usado (LRU)")

cache.put(3, 30)   # elimina la clave 2

print("get(2):", cache.get(2))   # -1
print("get(3):", cache.get(3))   # 30


"""Caso 3"""
print("\nCaso 3: Actualización y prioridad de uso")

cache.put(1, 100)  # actualiza valor y lo marca como MRU
cache.put(4, 40)   # elimina el LRU

print("get(1):", cache.get(1))   # 100
print("get(3):", cache.get(3))   # -1
print("get(4):", cache.get(4))   # 40
 


"""
EJERCICIO 18: Editor Multi-cursor
Dificultad: Avanzado

Se debe implementar un editor de texto que soporte múltiples cursores,
similar a editores modernos como VS Code.

Cada cursor puede estar en una posición distinta del documento y
realizar inserciones independientes.

Funcionalidades requeridas:
- add_cursor(position): Agrega un cursor en una posición dada
- remove_cursor(cursor_id): Elimina un cursor existente
- type_at_cursor(cursor_id, text): Inserta texto en la posición del cursor
- undo_all(): Deshace la última acción realizada
- redo_all(): Rehace la última acción deshecha

Requisitos clave:
- Mantener sincronizadas las posiciones de todos los cursores
- Gestionar correctamente undo / redo
"""

class Action:
    def __init__(self, cursor_id, position, text):
        """
        Representa una acción de edición realizada por un cursor.
        Guarda el cursor, la posición y el texto insertado.
        """
        self.cursor_id = cursor_id
        self.position = position
        self.text = text


class MultiCursorEditor:
    def __init__(self):
        """
        Inicializa el editor con:
        - Documento vacío
        - Diccionario de cursores
        - Pilas de undo y redo
        """
        self.document = ""
        self.cursors = {}          
        self.next_cursor_id = 1
        self.undo_stack = []
        self.redo_stack = []

    def add_cursor(self, position):
        """
        Agrega un nuevo cursor en la posición indicada
        y retorna su identificador.
        """
        cursor_id = self.next_cursor_id
        self.next_cursor_id += 1
        self.cursors[cursor_id] = position
        return cursor_id

    def remove_cursor(self, cursor_id):
        """
        Elimina un cursor existente.
        """
        if cursor_id in self.cursors:
            del self.cursors[cursor_id]

    def type_at_cursor(self, cursor_id, text):
        """
        Inserta texto en la posición del cursor especificado.
        Ajusta las posiciones de los demás cursores
        y guarda la acción para undo.
        """
        if cursor_id not in self.cursors:
            return

        pos = self.cursors[cursor_id]

        """
        Inserción del texto en el documento.
        """
        self.document = (
            self.document[:pos] + text + self.document[pos:]
        )

        """
        Actualización de las posiciones de los cursores.
        Los cursores a la derecha del punto de inserción
        se desplazan.
        """
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        """
        Mover el cursor actual al final del texto insertado.
        """
        self.cursors[cursor_id] += len(text)

        """
        Guardar la acción y limpiar el redo stack.
        """
        self.undo_stack.append(Action(cursor_id, pos, text))
        self.redo_stack.clear()

    def undo_all(self):
        """
        Deshace la última acción realizada.
        """
        if not self.undo_stack:
            return

        action = self.undo_stack.pop()
        pos = action.position
        length = len(action.text)

        """
        Eliminar el texto insertado.
        """
        self.document = (
            self.document[:pos] + self.document[pos + length:]
        )

        """
        Ajustar las posiciones de los cursores.
        """
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] -= length

        """
        Guardar la acción en el redo stack.
        """
        self.redo_stack.append(action)

    def redo_all(self):
        """
        Rehace la última acción deshecha.
        """
        if not self.redo_stack:
            return

        action = self.redo_stack.pop()
        pos = action.position
        text = action.text

        """
        Reinsertar el texto.
        """
        self.document = (
            self.document[:pos] + text + self.document[pos:]
        )

        """
        Ajustar las posiciones de los cursores.
        """
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        """
        Volver a guardar la acción en undo.
        """
        self.undo_stack.append(action)


print("\n================ EJERCICIO 18 ================\n")

editor = MultiCursorEditor()

"""Caso 1: Inserción con múltiples cursores"""
print("Caso 1: Escritura con dos cursores")

c1 = editor.add_cursor(0)
c2 = editor.add_cursor(0)

editor.type_at_cursor(c1, "Hola")
editor.type_at_cursor(c2, "Hey ")

print("Documento:", editor.document)   # Esperado: "Hey Hola"


"""Caso 2: Undo de la última acción"""
print("\nCaso 2: Undo")

editor.undo_all()
print("Documento:", editor.document)   # Esperado: "Hola"


"""Caso 3: Redo de la acción deshecha"""
print("\nCaso 3: Redo")

editor.redo_all()
print("Documento:", editor.document)   # Esperado: "Hey Hola"
 


"""
EJERCICIO 19: Benchmark de operaciones
Dificultad: Intermedio

Se debe comparar el rendimiento de tres estructuras de datos:
- Arrays (listas nativas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para las siguientes operaciones:
1. Inserción al inicio (1000 elementos)
2. Inserción al final (1000 elementos)
3. Eliminación al inicio (1000 elementos)
4. Eliminación al final (1000 elementos)
5. Acceso por índice (1000 accesos aleatorios)

Se utilizará el módulo 'time' para medir el tiempo de ejecución
y se mostrarán los resultados en una tabla comparativa.
"""

import time
import random


class Node:
    def __init__(self, data):
        """
        Nodo base para listas enlazadas.
        Contiene el dato y referencias al siguiente
        y anterior nodo (si aplica).
        """
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """
    Implementación de lista simplemente enlazada.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        """
        Inserta un elemento al inicio de la lista.
        """
        node = Node(value)
        node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = node

    def insert_end(self, value):
        """
        Inserta un elemento al final de la lista.
        """
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_start(self):
        """
        Elimina el elemento del inicio de la lista.
        """
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def remove_end(self):
        """
        Elimina el elemento del final de la lista.
        """
        if not self.head:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = None
        self.tail = current

    def get(self, index):
        """
        Retorna el elemento en la posición index.
        """
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


class DoublyLinkedList:
    """
    Implementación de lista doblemente enlazada.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        """
        Inserta un elemento al inicio de la lista.
        """
        node = Node(value)

        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def insert_end(self, value):
        """
        Inserta un elemento al final de la lista.
        """
        node = Node(value)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node

        self.tail = node

    def remove_start(self):
        """
        Elimina el elemento del inicio de la lista.
        """
        if not self.head:
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_end(self):
        """
        Elimina el elemento del final de la lista.
        """
        if not self.tail:
            return

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def get(self, index):
        """
        Retorna el elemento en la posición index.
        """
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


def benchmark():
    """
    Ejecuta el benchmark comparativo entre:
    - Array
    - Lista simplemente enlazada
    - Lista doblemente enlazada
    """
    
    print("\n================ EJERCICIO 19 ================\n")
    print("Comparación de rendimiento entre:")
    print("1) Array (list de Python)")
    print("2) Lista Simplemente Enlazada (SLL)")
    print("3) Lista Doblemente Enlazada (DLL)")


    N = 1000
    indices = [random.randint(0, N - 1) for _ in range(N)]
    results = {}
    arr = []
    start = time.time()
    for i in range(N):
        arr.insert(0, i)
    results["Array insert start"] = time.time() - start

    arr = []
    start = time.time()
    for i in range(N):
        arr.append(i)
    results["Array insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        arr.pop(0)
    results["Array remove start"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for _ in range(N):
        arr.pop()
    results["Array remove end"] = time.time() - start

    arr = list(range(N))
    start = time.time()
    for i in indices:
        _ = arr[i]
    results["Array access"] = time.time() - start

    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_start(i)
    results["SLL insert start"] = time.time() - start

    sll = SinglyLinkedList()
    start = time.time()
    for i in range(N):
        sll.insert_end(i)
    results["SLL insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        sll.remove_start()
    results["SLL remove start"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for _ in range(N):
        sll.remove_end()
    results["SLL remove end"] = time.time() - start

    sll = SinglyLinkedList()
    for i in range(N):
        sll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = sll.get(i)
    results["SLL access"] = time.time() - start

    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_start(i)
    results["DLL insert start"] = time.time() - start

    dll = DoublyLinkedList()
    start = time.time()
    for i in range(N):
        dll.insert_end(i)
    results["DLL insert end"] = time.time() - start

    start = time.time()
    for _ in range(N):
        dll.remove_start()
    results["DLL remove start"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for _ in range(N):
        dll.remove_end()
    results["DLL remove end"] = time.time() - start

    dll = DoublyLinkedList()
    for i in range(N):
        dll.insert_end(i)
    start = time.time()
    for i in indices:
        _ = dll.get(i)
    results["DLL access"] = time.time() - start
    
    print("\n--- BENCHMARK (1000 operaciones) ---")
    for k, v in results.items():
        print(f"{k:25} {v:.6f} s")

benchmark()



"""
EJERCICIO 20: Análisis de casos de uso
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Para cada uno de los siguientes escenarios, se determina la estructura
de datos más apropiada (Array, Lista Simple, Lista Doble) y se justifica
la elección según su uso y complejidad.
"""

"""
1. Sistema de colas de impresión (FIFO estricto)
Estructura: Lista simplemente enlazada
Justificación: El sistema funciona como una cola FIFO.
Permite insertar al final y eliminar al inicio en O(1)
manteniendo referencias a head y tail.
No se requiere acceso por índice.
"""

"""
2. Historial de navegación de un navegador
Estructura: Lista doblemente enlazada
Justificación: Permite navegar hacia atrás y adelante en O(1),
ya que cada nodo mantiene referencia al anterior y al siguiente.
"""

"""
3. Sistema de undo/redo con límite de 100 acciones
Estructura: Lista doblemente enlazada
Justificación: Facilita moverse entre acciones anteriores y posteriores.
El límite se controla eliminando nodos antiguos.
Las operaciones undo y redo son O(1).
"""

"""
4. Base de datos que necesita acceso rápido por ID
Estructura: Array (lista de Python)
Justificación: Permite acceso directo por índice en O(1).
Es ideal cuando el ID corresponde a una posición específica.
"""

"""
5. Playlist de música con navegación adelante/atrás
Estructura: Lista doblemente enlazada
Justificación: Permite avanzar y retroceder entre canciones fácilmente
sin recorrer toda la estructura.
"""

"""
6. Sistema de gestión de memoria del sistema operativo
Estructura: Lista simplemente enlazada
Justificación: Se usan listas de bloques libres donde se insertan y eliminan
elementos frecuentemente sin necesidad de acceso aleatorio.
"""

"""
7. Editor de texto que solo permite append al final
Estructura: Array (lista de Python)
Justificación: La operación append es O(1) amortizado.
La memoria contigua facilita la lectura secuencial del texto.
"""

"""
8. Implementación de una pila (Stack)
Estructura: Array (lista de Python)
Justificación: Las operaciones push y pop al final son O(1) amortizado.
Es una implementación simple y eficiente.
"""

"""
9. Juego que necesita insertar y eliminar enemigos frecuentemente
Estructura: Lista simplemente enlazada
Justificación: Permite inserciones y eliminaciones en O(1)
sin desplazar elementos como en un array.
"""

"""
10. Sistema de logs que solo escribe al final y lee todo
Estructura: Array (lista de Python)
Justificación: Las escrituras al final con append y la lectura secuencial
hacen que el array sea la opción más eficiente.
"""
