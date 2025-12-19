"""
EJERCICIO 1: Contar elementos
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método count(elem) en SLinkedList que cuente cuántas veces
aparece un elemento en la lista.

Ejemplo:
    lista = [1, 2, 3, 2, 4, 2]
    lista.count(2)  # Retorna: 3
    lista.count(5)  # Retorna: 0
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def count(self, elem):
        contador = 0
        actual = self.head

        while actual:
            if actual.dato == elem:
                contador += 1
            actual = actual.next

        return contador

lista = SLinkedList()
for x in [0, 2, 3, 2, 4, 2]:
    lista.agregar(x)

print(lista.count(2))  
print(lista.count(5))  

"""
EJERCICIO 2: Obtener elemento por índice
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

Implementa un método get(index) que retorne el elemento en la posición index.

Ejemplo:
    lista = ['A', 'B', 'C', 'D']
    lista.get(0)   # Retorna: 'A'
    lista.get(2)   # Retorna: 'C'
    lista.get(10)  # Lanza: IndexError
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def get(self, index):
        if index < 0:
            raise IndexError("Índice fuera de rango")

        actual = self.head
        contador = 0

        while actual:
            if contador == index:
                return actual.dato
            actual = actual.next
            contador += 1

        # Si se terminó la lista y no se encontró el índice
        raise IndexError("Índice fuera de rango")

lista = SLinkedList()
for x in ['A', 'B', 'C', 'D']:
    lista.agregar(x)

print(lista.get(0))   # 'A'
print(lista.get(2))   # 'C'
print(lista.get(10))  # IndexError

"""
EJERCICIO 3: Encontrar índice de elemento
Dificultad: 🟢 Básico
Tiempo estimado: 15 minutos

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
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def index_of(self, elem):
        actual = self.head
        indice = 0

        while actual:
            if actual.dato == elem:
                return indice
            actual = actual.next
            indice += 1

        return -1

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

lista = SLinkedList()
for x in ['A', 'B', 'C', 'B', 'D']:
    lista.agregar(x)

print(lista.index_of('B'))  # 1
print(lista.index_of('D'))  # 4
print(lista.index_of('Z'))  # -1

"""
EJERCICIO 4: Lista a array
Dificultad: 🟢 Básico
Tiempo estimado: 10 minutos

Implementa un método to_list() que convierta la lista enlazada a una
lista de Python (array).

Ejemplo:
    linked_list = SLinkedList con [1, 2, 3, 4]
    linked_list.to_list()  # Retorna: [1, 2, 3, 4]
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def to_list(self):
        resultado = []
        actual = self.head

        while actual:
            resultado.append(actual.dato)
            actual = actual.next

        return resultado

linked_list = SLinkedList()
for x in [1, 2, 3, 4]:
    linked_list.agregar(x)

print(linked_list.to_list())  # [1, 2, 3, 4]

"""
EJERCICIO 5: Limpiar lista
Dificultad: 🟢 Básico
Tiempo estimado: 5 minutos

Implementa un método clear() que elimine todos los elementos de la lista.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.clear()
    len(lista)  # Retorna: 0
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0   # opcional, pero útil

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def clear(self):
        self.head = None
        self.size = 0

lista = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista.agregar(x)

lista.clear()

print(lista.size)  # 0

"""
EJERCICIO 6: Invertir lista
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

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
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def reverse(self):
        anterior = None
        actual = self.head

        while actual:
            siguiente = actual.next   # guardar referencia
            actual.next = anterior    # invertir puntero
            anterior = actual         # avanzar anterior
            actual = siguiente        # avanzar actual

        self.head = anterior

lista = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista.agregar(x)

lista.reverse()
print(lista)

"""
EJERCICIO 7: Detectar ciclo
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

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
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def has_cycle(self):
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next           # 1 paso
            rapido = rapido.next.next    # 2 pasos

            if lento == rapido:
                return True

        return False

# Lista normal
lista1 = SLinkedList()
for x in [1, 2, 3]:
    lista1.agregar(x)

print(lista1.has_cycle())  # False


# Lista con ciclo
lista2 = SLinkedList()
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

lista2.head = n1
n1.next = n2
n2.next = n3
n3.next = n2   # ciclo

print(lista2.has_cycle())  # True

"""
EJERCICIO 8: Encontrar el medio
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

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
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def get_middle(self):
        lento = self.head
        rapido = self.head

        if not self.head:  # Si la lista está vacía
            return None

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento.dato  # Cuando el rápido llega al final, el lento está en el medio

# Lista con número impar de elementos
lista1 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista1.agregar(x)

print(lista1.get_middle())  # 3


# Lista con número par de elementos
lista2 = SLinkedList()
for x in [1, 2, 3, 4]:
    lista2.agregar(x)

print(lista2.get_middle())  # 3 (el segundo del medio)

"""
EJERCICIO 9: Eliminar duplicados
Dificultad: 🟡 Intermedio
Tiempo estimado: 25 minutos

Implementa un método remove_duplicates() que elimine todos los elementos
duplicados de la lista, dejando solo la primera ocurrencia de cada elemento.

Ejemplo:
    [1, 2, 3, 2, 4, 1, 5] → [1, 2, 3, 4, 5]

Versión 1: Puedes usar un conjunto (set) auxiliar - O(n) tiempo, O(n) espacio
Versión 2: Sin espacio adicional (más difícil) - O(n²) tiempo, O(1) espacio
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    # 👇 ESTE MÉTODO ES CLAVE PARA VER EL RESULTADO
    def __str__(self):
        actual = self.head
        resultado = ""
        while actual:
            resultado += str(actual.dato) + " → "
            actual = actual.next
        return resultado + "None"

    # Versión con set (O(n))
    def remove_duplicates(self):
        vistos = set()
        actual = self.head
        anterior = None

        while actual:
            if actual.dato in vistos:
                anterior.next = actual.next
            else:
                vistos.add(actual.dato)
                anterior = actual
            actual = actual.next

lista = SLinkedList()
for x in [1, 2, 3, 2, 4, 1, 5]:
    lista.agregar(x)

print("Antes:")
print(lista)

lista.remove_duplicates()

print("Después:")
print(lista)

"""
EJERCICIO 10: Fusionar dos listas ordenadas
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

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
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        actual = self.head
        resultado = ""
        while actual:
            resultado += str(actual.dato) + " → "
            actual = actual.next
        return resultado + "None"

def merge_sorted(list1, list2):
    nueva_lista = SLinkedList()

    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.dato <= p2.dato:
            nueva_lista.agregar(p1.dato)
            p1 = p1.next
        else:
            nueva_lista.agregar(p2.dato)
            p2 = p2.next

    # Agregar los elementos restantes
    while p1:
        nueva_lista.agregar(p1.dato)
        p1 = p1.next

    while p2:
        nueva_lista.agregar(p2.dato)
        p2 = p2.next

    return nueva_lista

list1 = SLinkedList()
for x in [1, 3, 5, 7]:
    list1.agregar(x)

list2 = SLinkedList()
for x in [2, 4, 6, 8]:
    list2.agregar(x)

resultado = merge_sorted(list1, list2)
print(resultado)

"""
EJERCICIO 11: Palíndromo
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos

Implementa un método is_palindrome() que determine si la lista es un palíndromo
(se lee igual de adelante hacia atrás).

Ejemplo:
    [1, 2, 3, 2, 1] → True
    [1, 2, 3, 4, 5] → False

Solución eficiente:
1. Encuentra el medio (algoritmo dos punteros)
2. Invierte la segunda mitad
3. Compara primera mitad con segunda mitad invertida
4. Restaura la segunda mitad (opcional)

Complejidad: O(n) tiempo, O(1) espacio
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        actual = self.head
        res = ""
        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next
        return res + "None"

    # 🔥 MÉTODO PALÍNDROMO
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # 1️⃣ Encontrar el medio
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        # 2️⃣ Invertir la segunda mitad
        prev = None
        actual = lento

        while actual:
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        # 3️⃣ Comparar mitades
        p1 = self.head
        p2 = prev   # cabeza de la mitad invertida

        es_palindromo = True
        while p2:
            if p1.dato != p2.dato:
                es_palindromo = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4️⃣ Restaurar la lista (opcional)
        actual = prev
        prev = None
        while actual:
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig

        return es_palindromo

lista1 = SLinkedList()
for x in [1, 2, 3, 2, 1]:
    lista1.agregar(x)

print(lista1)
print(lista1.is_palindrome())  # True


lista2 = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista2.agregar(x)

print(lista2)
print(lista2.is_palindrome())  # False

"""
EJERCICIO 12: Rotar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 30 minutos

Implementa un método rotate(k) que rote la lista k posiciones a la derecha.

Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.rotate(2)
    print(lista)  # Output: 4 → 5 → 1 → 2 → 3 → None

Pasos:
1. Conectar el último nodo con el primero (hacer circular)
2. Encontrar el nuevo head (en posición size - k)
3. Romper el círculo

Complejidad esperada: O(n)
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def __str__(self):
        actual = self.head
        res = ""
        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next
        return res + "None"

    # 🔄 ROTAR A LA DERECHA
    def rotate(self, k):
        if not self.head or self.size <= 1:
            return

        k = k % self.size
        if k == 0:
            return

        # 1️⃣ Encontrar último nodo
        tail = self.head
        while tail.next:
            tail = tail.next

        # 2️⃣ Hacer la lista circular
        tail.next = self.head

        # 3️⃣ Encontrar nuevo tail (size - k - 1)
        pasos = self.size - k
        nuevo_tail = self.head
        for _ in range(pasos - 1):
            nuevo_tail = nuevo_tail.next

        # 4️⃣ Romper el círculo
        self.head = nuevo_tail.next
        nuevo_tail.next = None

lista = SLinkedList()
for x in [1, 2, 3, 4, 5]:
    lista.agregar(x)

print("Antes:")
print(lista)

lista.rotate(2)

print("Después:")
print(lista)

"""
EJERCICIO 13: Particionar lista
Dificultad: 🔴 Avanzado
Tiempo estimado: 35 minutos

Implementa un método partition(x) que reorganice la lista de modo que
todos los elementos menores que x aparezcan antes que los elementos
mayores o iguales a x. El orden relativo dentro de cada grupo debe preservarse.

Ejemplo:
    lista = [3, 5, 8, 5, 10, 2, 1]
    lista.partition(5)
    # Resultado: [3, 2, 1] + [5, 8, 5, 10]
    # O cualquier permutación donde menores a 5 estén primero

Pista: Crea dos listas auxiliares (menores y mayores) y luego únelas.
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        actual = self.head
        res = ""
        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next
        return res + "None"

    # 🔀 PARTITION
    def partition(self, x):
        # Cabezas y colas de las dos listas
        menores_head = menores_tail = None
        mayores_head = mayores_tail = None

        actual = self.head

        while actual:
            siguiente = actual.next
            actual.next = None   # desconectar nodo

            if actual.dato < x:
                if not menores_head:
                    menores_head = menores_tail = actual
                else:
                    menores_tail.next = actual
                    menores_tail = actual
            else:
                if not mayores_head:
                    mayores_head = mayores_tail = actual
                else:
                    mayores_tail.next = actual
                    mayores_tail = actual

            actual = siguiente

        # Unir las dos listas
        if menores_tail:
            menores_tail.next = mayores_head
            self.head = menores_head
        else:
            self.head = mayores_head

lista = SLinkedList()
for x in [3, 5, 8, 5, 10, 2, 1]:
    lista.agregar(x)

print("Antes:")
print(lista)

lista.partition(5)

print("Después:")
print(lista)

"""
EJERCICIO 14: Suma de dos listas (números)
Dificultad: 🔴 Avanzado
Tiempo estimado: 40 minutos

Tienes dos listas enlazadas que representan números (cada nodo es un dígito).
Los dígitos están almacenados en ORDEN INVERSO (el primer nodo es la unidad).

Implementa una función add_numbers(list1, list2) que sume ambos números
y retorne el resultado como una nueva lista enlazada.

Ejemplo:
    list1 = [2, 4, 3] representa 342
    list2 = [5, 6, 4] representa 465
    add_numbers(list1, list2) = [7, 0, 8] representa 807

Pista: Es como sumar manualmente, llevando el "carry".
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        actual = self.head
        res = ""
        while actual:
            res += str(actual.dato) + " → "
            actual = actual.next
        return res + "None"

def add_numbers(list1, list2):
    resultado = SLinkedList()

    p1 = list1.head
    p2 = list2.head
    carry = 0

    while p1 or p2 or carry:
        suma = carry

        if p1:
            suma += p1.dato
            p1 = p1.next

        if p2:
            suma += p2.dato
            p2 = p2.next

        carry = suma // 10
        resultado.agregar(suma % 10)

    return resultado

list1 = SLinkedList()
for x in [2, 4, 3]:
    list1.agregar(x)

list2 = SLinkedList()
for x in [5, 6, 4]:
    list2.agregar(x)

resultado = add_numbers(list1, list2)

print("Resultado:")
print(resultado)

"""
EJERCICIO 15: Intersección de dos listas
Dificultad: 🔴 Avanzado
Tiempo estimado: 45 minutos

Dadas dos listas enlazadas, determina si se intersectan (comparten nodos)
y encuentra el nodo donde se intersectan.

Ejemplo:
    list1: 1 → 2 → 3 ↘
                      7 → 8 → 9
    list2: 4 → 5 → 6 ↗
    
    Retorna el nodo con valor 7 (primer nodo compartido)

Solución eficiente:
1. Calcula la longitud de ambas listas
2. Alinea los inicios (avanza en la lista más larga)
3. Avanza simultáneamente hasta encontrar el nodo común

Complejidad: O(n + m) tiempo, O(1) espacio
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

def longitud(lista):
    actual = lista.head
    count = 0
    while actual:
        count += 1
        actual = actual.next
    return count

def get_intersection_node(list1, list2):
    len1 = longitud(list1)
    len2 = longitud(list2)

    p1 = list1.head
    p2 = list2.head

    # 1️⃣ Alinear inicios
    if len1 > len2:
        for _ in range(len1 - len2):
            p1 = p1.next
    else:
        for _ in range(len2 - len1):
            p2 = p2.next

    # 2️⃣ Avanzar simultáneamente
    while p1 and p2:
        if p1 is p2:   # COMPARACIÓN DE NODOS, no de valores
            return p1
        p1 = p1.next
        p2 = p2.next

    return None

# Crear nodos compartidos
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

# Buscar intersección
interseccion = get_intersection_node(list1, list2)

if interseccion:
    print("Nodo de intersección:", interseccion.dato)
else:
    print("No hay intersección")

"""
EJERCICIO 16: Navegador Web
Dificultad: 🟡 Intermedio
Tiempo estimado: 40 minutos

Implementa una clase BrowserHistory que simule el historial de un navegador
usando una lista doblemente enlazada.

Métodos requeridos:
- __init__(homepage): Inicia con la página de inicio
- visit(url): Visita una nueva URL (elimina historial futuro)
- back(steps): Retrocede 'steps' páginas (máximo hasta el inicio)
- forward(steps): Avanza 'steps' páginas (máximo hasta el final)
- get_current(): Retorna la URL actual

Ejemplo:
    browser = BrowserHistory("google.com")
    browser.visit("youtube.com")    # google.com → youtube.com
    browser.visit("facebook.com")   # ... → facebook.com
    browser.back(1)                 # Vuelve a youtube.com
    browser.forward(1)              # Regresa a facebook.com
"""

class Nodo:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.current = Nodo(homepage)

    def visit(self, url):
        nuevo = Nodo(url)

        # eliminar historial futuro
        self.current.next = None

        # enlazar nuevo nodo
        nuevo.prev = self.current
        self.current.next = nuevo

        # mover actual
        self.current = nuevo

    def back(self, steps):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def get_current(self):
        return self.current.url

browser = BrowserHistory("google.com")

browser.visit("youtube.com")
browser.visit("facebook.com")

browser.back(1)        # youtube.com
browser.forward(1)     # facebook.com

print(browser.get_current())

"""
EJERCICIO 17: LRU Cache
Dificultad: 🔴 Avanzado
Tiempo estimado: 60 minutos

Implementa una estructura de datos LRU Cache (Least Recently Used Cache)
usando una lista doblemente enlazada + diccionario.

El cache tiene capacidad limitada. Cuando se llena, elimina el elemento
usado menos recientemente.

Métodos:
- __init__(capacity): Crea cache con capacidad dada
- get(key): Obtiene el valor (marca como usado recientemente)
- put(key, value): Inserta/actualiza (elimina LRU si está lleno)

Ambos métodos deben ser O(1).

Pista: 
- Diccionario: para acceso O(1) por key
- Lista doble: para mantener orden de uso (más reciente al final)
"""

class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> nodo

        # Nodos ficticios (dummy) para simplificar
        self.head = Nodo(0, 0)  # LRU
        self.tail = Nodo(0, 0)  # MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, nodo):
        prev = nodo.prev
        next = nodo.next
        prev.next = next
        next.prev = prev

    def _add_to_end(self, nodo):
        prev = self.tail.prev
        prev.next = nodo
        nodo.prev = prev
        nodo.next = self.tail
        self.tail.prev = nodo

    def get(self, key):
        if key not in self.cache:
            return -1

        nodo = self.cache[key]

        # mover a más recientemente usado
        self._remove(nodo)
        self._add_to_end(nodo)

        return nodo.value

    def put(self, key, value):
        if key in self.cache:
            nodo = self.cache[key]
            nodo.value = value
            self._remove(nodo)
            self._add_to_end(nodo)
        else:
            if len(self.cache) == self.capacity:
                # eliminar LRU
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            nuevo = Nodo(key, value)
            self.cache[key] = nuevo
            self._add_to_end(nuevo)

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # 10 (1 es ahora el más reciente)

cache.put(3, 30)     # elimina key 2 (LRU)

print(cache.get(2))  # -1
print(cache.get(3))  # 30
print(cache.get(1))  # 10

"""
EJERCICIO 18: Editor Multi-cursor
Dificultad: 🔴 Avanzado
Tiempo estimado: 50 minutos

Extiende el TextEditor para soportar múltiples cursores (como en VS Code).
Cada cursor puede estar en una posición diferente del documento.

Funcionalidades:
- add_cursor(position): Agregar cursor en posición
- remove_cursor(cursor_id): Eliminar cursor
- type_at_cursor(cursor_id, text): Escribir en cursor específico
- undo_all(): Deshacer en todos los cursores
- redo_all(): Rehacer en todos los cursores

Esto requiere mantener múltiples historiales sincronizados.
"""


class Action:
    def __init__(self, cursor_id, position, text):
        self.cursor_id = cursor_id
        self.position = position
        self.text = text

class MultiCursorEditor:
    def __init__(self):
        self.document = ""
        self.cursors = {}          # cursor_id -> position
        self.next_cursor_id = 1
        self.undo_stack = []
        self.redo_stack = []

    def add_cursor(self, position):
        cursor_id = self.next_cursor_id
        self.next_cursor_id += 1
        self.cursors[cursor_id] = position
        return cursor_id

    def remove_cursor(self, cursor_id):
        if cursor_id in self.cursors:
            del self.cursors[cursor_id]

    def type_at_cursor(self, cursor_id, text):
        if cursor_id not in self.cursors:
            return

        pos = self.cursors[cursor_id]

        # insertar texto
        self.document = (
            self.document[:pos] + text + self.document[pos:]
        )

        # actualizar posiciones de cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        # mover cursor actual
        self.cursors[cursor_id] += len(text)

        # guardar acción
        self.undo_stack.append(Action(cursor_id, pos, text))
        self.redo_stack.clear()

    def undo_all(self):
        if not self.undo_stack:
            return

        action = self.undo_stack.pop()
        pos = action.position
        length = len(action.text)

        # eliminar texto
        self.document = (
            self.document[:pos] + self.document[pos + length:]
        )

        # ajustar cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] -= length

        self.redo_stack.append(action)

    def redo_all(self):
        if not self.redo_stack:
            return

        action = self.redo_stack.pop()
        pos = action.position
        text = action.text

        # reinsertar texto
        self.document = (
            self.document[:pos] + text + self.document[pos:]
        )

        # ajustar cursores
        for cid in self.cursors:
            if self.cursors[cid] > pos:
                self.cursors[cid] += len(text)

        self.undo_stack.append(action)

editor = MultiCursorEditor()

c1 = editor.add_cursor(0)
c2 = editor.add_cursor(0)

editor.type_at_cursor(c1, "Hola")
editor.type_at_cursor(c2, "Hey ")

print(editor.document)  # Hey Hola

editor.undo_all()
print(editor.document)  # Hola

editor.redo_all()
print(editor.document)  # Hey Hola

"""
EJERCICIO 19: Benchmark de operaciones
Dificultad: 🟡 Intermedio
Tiempo estimado: 30 minutos

Escribe un programa que compare el rendimiento de:
- Arrays (listas de Python)
- Listas simplemente enlazadas
- Listas doblemente enlazadas

Para las siguientes operaciones:
1. Inserción al inicio (1000 elementos)
2. Inserción al final (1000 elementos)
3. Eliminación al inicio (1000 elementos)
4. Eliminación al final (1000 elementos)
5. Acceso por índice (1000 accesos aleatorios)

Usa el módulo 'time' para medir el tiempo.
Imprime los resultados en una tabla comparativa.
"""

import time
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_start(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None

    def remove_end(self):
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
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def remove_start(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_end(self):
        if not self.tail:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

def benchmark():
    N = 1000
    indices = [random.randint(0, N - 1) for _ in range(N)]

    results = {}

    # ===== ARRAY =====
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

    # ===== SINGLY LINKED LIST =====
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

    # ===== DOUBLY LINKED LIST =====
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

    # ===== PRINT TABLE =====
    print("\n--- BENCHMARK (1000 operaciones) ---")
    for k, v in results.items():
        print(f"{k:25} {v:.6f} s")

benchmark()

"""
EJERCICIO 20: Análisis de casos de uso
Dificultad: 🟡 Intermedio
Tiempo estimado: 20 minutos

Para cada uno de los siguientes escenarios, determina qué estructura
es más apropiada (Array, Lista Simple, Lista Doble) y justifica tu respuesta:

1. Sistema de colas de impresión (FIFO estricto)
2. Historial de navegación de un navegador
3. Sistema de undo/redo con límite de 100 acciones
4. Base de datos que necesita acceso rápido por ID
5. Playlist de música con navegación adelante/atrás
6. Sistema de gestión de memoria del OS
7. Editor de texto que solo permite append al final
8. Implementación de una pila (Stack)
9. Juego que necesita insertar/eliminar enemigos frecuentemente
10. Sistema de logs que solo escribe al final y lee todo

Escribe tus respuestas en comentarios con justificación.
"""

# 1. Sistema de colas de impresión (FIFO estricto)
# Estructura: Lista simplemente enlazada
# Justificación:
# Inserciones al final (enqueue) y eliminaciones al inicio (dequeue)
# se realizan en O(1). No se necesita acceso por índice.

# 2. Historial de navegación de un navegador
# Estructura: Lista doblemente enlazada
# Justificación:
# Permite navegar hacia atrás y adelante en O(1),
# ya que cada nodo tiene referencia al anterior y siguiente.

# 3. Sistema de undo/redo con límite de 100 acciones
# Estructura: Lista doblemente enlazada
# Justificación:
# Facilita moverse entre estados anteriores y siguientes.
# El límite se controla eliminando nodos antiguos.
# (Alternativamente dos stacks, pero DLL es más natural aquí).

# 4. Base de datos que necesita acceso rápido por ID
# Estructura: Array (lista de Python)
# Justificación:
# Permite acceso directo por índice en O(1),
# ideal cuando el ID corresponde a una posición.

# 5. Playlist de música con navegación adelante/atrás
# Estructura: Lista doblemente enlazada
# Justificación:
# Permite avanzar y retroceder fácilmente entre canciones
# sin recorrer toda la estructura.

# 6. Sistema de gestión de memoria del OS
# Estructura: Lista simplemente enlazada
# Justificación:
# Se usan listas de bloques libres donde se insertan y eliminan
# nodos frecuentemente, sin necesidad de acceso aleatorio.

# 7. Editor de texto que solo permite append al final
# Estructura: Array (lista de Python)
# Justificación:
# append() es O(1) amortizado y permite almacenar el texto
# de forma contigua, facilitando su recorrido completo.

# 8. Implementación de una pila (Stack)
# Estructura: Array (lista de Python)
# Justificación:
# push() y pop() al final son O(1) amortizado
# y la implementación es simple y eficiente.

# 9. Juego que necesita insertar/eliminar enemigos frecuentemente
# Estructura: Lista simplemente enlazada
# Justificación:
# Inserciones y eliminaciones frecuentes en posiciones variables
# se hacen en O(1) sin desplazar elementos como en un array.

# 10. Sistema de logs que solo escribe al final y lee todo
# Estructura: Array (lista de Python)
# Justificación:
# Escrituras solo al final (append) y lectura secuencial
# hacen al array la opción más eficiente y simple.
