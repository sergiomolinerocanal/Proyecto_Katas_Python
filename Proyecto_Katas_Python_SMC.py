# %% [markdown]
# #  PROYECTO LÓGICA: Katas de Python

# %% [markdown]
# 1.-Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.

# %%
def recuento_letras(cadena_texto): #Creamos una función que primero genera una lista de caracteres excluyendo espacios
    lista_letras = []
    for letra in cadena_texto.lower(): #Añadimos lower() para no distinguir may y min
        if letra != " ":
            lista_letras.append(letra)
    numero_letras = {} # Creamos un diccionario en el que las claves son los caracteres únicos de la lista anterior y los valores son el número de repeticiones
    for letra in lista_letras:
        if letra not in numero_letras:
            numero_letras[letra] = 1
        else:
            numero_letras[letra] += 1
    return numero_letras
             
Mi_cadena_texto = "Sergio Molinero Canal" # Introducimos cualquier cadena de texto y nos devuelve el número de repeticiones (frecuencias?) de cada letra
cuenta_letras = recuento_letras(Mi_cadena_texto)
print(f"Estas son las repeticiones de cada letra {cuenta_letras}")

# %% [markdown]
# 2.-Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# %%
def doblar(numero): #Creamos la función "doblar" para multiplicar por 2 cualquier valor
    return numero*2
lista_numeros = list(range(2,8)) #Generamos una lista de ejemplo
resultado = map(doblar,lista_numeros) #aplicamos la función doblar a nuestra lista
print(f"Esta es la lista original: {lista_numeros}") 
print(f"Y esta es la lista con los valores doblados: {list(resultado)}")


# %% [markdown]
# 3.-Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo

# %%
def lista_palabras (lista, letra): 
    lista_final = []    #Creamos una lista vacía
    for palabra in lista: #hacemos un bucle que evalúa si la palabra contiene la letra objetivo
        if letra in palabra:
            lista_final.append(palabra) #Si la contiene, la añade a la lista
    return lista_final

mis_palabras = ["perro", "flor", "playa", "murcielago", "python","guerra", "naranja"]
letra = "a"
lista_con = lista_palabras(mis_palabras,letra)
print(f"Esta es la lista de palabras que contienen la letra {letra} ---> {lista_con}")

#No entiendo bien el enunciado, he interpretado que se refiere a listar las palabras que contengan determinada letra ¿?

# %% [markdown]
# 4.- Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función  map()

# %%
def diferencia_listas(a,b): #una función que resta dos valores
    return a - b
lista1 = [15,8,9,3,6]
lista2 = [5,10,12,1,4]
resultado_diferencias = map(diferencia_listas, lista1, lista2) # map aplica la función a cada par de elementos de la lista
print(f"Esta es la primera lista ---> {lista1}")
print(f"Esta es la segunda lista---> {lista2}")
print(f"Y este es el resultado de comparar los elementos de cada lista ---> {list(resultado_diferencias)}")

# %% [markdown]
# 5.-Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
# una tupla que contenga la media y el estado.

# %%
def nota_media(notas,corte): # Esta función calcula el promedio de los valores de una lista
    suma = 0
    for nota in notas:
        suma += nota
    resultado = round(suma / len(notas),2)
    if resultado >= corte: #evalua si la media es mayor o igual que la nota de corte
       return  ("Aprobado", resultado)
    else:
        return ("Suspenso", resultado)

mis_calificaciones = [2,7,6,5,3,9]
nota_aprobado = 5

mi_nota_media = nota_media(mis_calificaciones, nota_aprobado)
print(mi_nota_media)

# %% [markdown]
# 6.-Escribe una función que calcule el factorial de un número de manera recursiva

# %%
def factorial (num):
    if num == 1:
       return 1
    else:
        return num * factorial (num-1)        
mi_numero = 5
print(f"El factorial de {mi_numero} es {factorial(mi_numero)}")


# %% [markdown]
# 7.-Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función  map()

# %%
def generar_lista(lista_tuplas):
    lista_strings = [] # Creamos una lista vacía
    for palabra in lista_tuplas:
        lista_strings.append(palabra) # agrega las palabras a la lista
    return lista_strings
mis_tuplas = [("hola","H"),("camello","C"), ("estadio","E")]
lista_strings = list(map(generar_lista, mis_tuplas))
print(type(mis_tuplas[0]), mis_tuplas)
print(type(lista_strings), lista_strings)

# %% [markdown]
# 8.-Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no

# %%
try:
    dividendo = int(input("introduzca el dividendo"))
    divisor = int(input("introduzca el divisor"))
    resultado = round(int(dividendo) / int(divisor),2)
    print(f"El resultado de dividir {dividendo} entre {divisor} es {resultado}")
except ValueError: #Controla el error si el dato introducido no es un número
    print("Por favor, solo se pueden dividir números, su dividendo o divisor no es un número")
except ZeroDivisionError: #controla el error si el dato introducido es 0
    print("No se puede dividir por 0")


# %% [markdown]
# 9.-Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función  filter()

# %%
def animales_permitidos(mascota): #Creamos una función que evalúa una lista de animales y los clasifica cmo TRUE o FALSE según estén o no en la lista de prohibidos
    animales_prohibidos = ["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"]
    if mascota not in animales_prohibidos:
            return True
    else:
          return False
           
mis_mascotas = ["Perro","Oso","Gato","Mapache","X"]
lista_definitiva = list(filter(animales_permitidos,mis_mascotas)) #Filtramos la lista original aplicando la nuva función
print(f"Esta es la lista de mascotas permitidas ---> {lista_definitiva}")



# %% [markdown]
# 10.-Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
# excepción personalizada y maneja el error adecuadamente.

# %%
def promedio(numeros): #Creamos una función que va sumando los números de una lista y calculando el promedio con un LEN
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)
   
mis_numeros = [2,5,9,4,8]
try: #Empezamos con TRY para que nos devuelva el promedio
    print(f"El promedio de esta lista de numeros {mis_numeros} es {promedio(mis_numeros)}")
except ZeroDivisionError: #Indicamos la excepción en caso de que la lista esté vacía
    print(f"La lista de numeros no puede estar vacía!")


# %% [markdown]
# 11.-Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones 
# adecuadamente.

# %%
try: #Comenzamos con el TRY
    edad = int(input("Introduzca su edad")) #Pedimos la edad al usuario
    if edad >120: #No nos creemos que tenga más de 120 años
        print("Es poco probable que usted tenga más de 120 años")
    elif edad < 0: #Ni menos de 0
        print("no es posible que usted tenga menos de 0 años")
    else:
        print(f"Su edad declarada es {edad} años")
except ValueError: # Y le avisamos si intruduce cualquier otro caracter que no sea un número
    print("Por favor, introduzca un valor correcto")   
    

# %% [markdown]
# 12.-Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función  map()

# %%
def cuenta_letras (palabra): #definimos una función que crea pares de palabra : longitud
    return palabra, len(palabra)
mi_cuentaletras = map(cuenta_letras,mis_palabras) #Aplicamos la función a la lista de palabras que definimos en otro ejercicio anterior
dic_palabra_letras = dict(mi_cuentaletras) #Convertimos este objeto en un diccionario
print(f"Esta es la lista de palabras ---> {mis_palabras}")
print(f"Y este es el diccionario con el numero de letras que tiene cada palabra ---> {dic_palabra_letras}")

# %% [markdown]
# 13.-Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función  map()

# %%
def may_min(letra): #Definimos la función que se va a ocupar de poner casa letra en mayúsculas y minúsculas
   return letra.upper(), letra.lower()      
mi_palabra ="ABbCCccDDDddd" 
palabra_min=set(mi_palabra.lower()) #convertimos la cadena de texto en un set en minúsculas para evitar repeticiones
mi_lista_tuplas = map(may_min,palabra_min) #aplicamos la función a nuestra palabra   
print(list(mi_lista_tuplas)) #Convertimos el objeto en lista y lo imprimimos por pantalla

# %% [markdown]
# 14.-Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
# función  filter()

# %%
mi_inicial= "p" #Declaramos la inicial que queremos utilizar, en este caso la "p"
def inicial(palabra):   
    if palabra[0].lower() == mi_inicial: #Evaluamos si la palabra empieza por p, nos aseguramos con lower() de que detecte también mayúsculas
        return True
    else:
        return False
palabras_filtradas = list(filter(inicial,mis_palabras)) # Aplicamos la función a la lista que declaramos anteriormente
print(f"Este es el listado inicial de palabras ---> {mis_palabras}")
if len(palabras_filtradas) == 0: # Ofrecemos una alternativa si la lista está vacía
    print(f"no hay ninguna palabra que empiece por {mi_inicial}")
else:
    print(f"Y estas son las palabras que empiezan por '{mi_inicial}'---> {palabras_filtradas}")

# %% [markdown]
# 15.-Crea una función  lambda  que  sume 3 a cada número de una lista dada.

# %%
lambda_mas3 = lambda n: n + 3 #Creamos la función lambda que suma 3 a cada valor de una lista
lista_mas_3 = list(map(lambda_mas3,mis_numeros)) 
print(f"Esta es mi lista INICIAL de números ---> {mis_numeros}")
print(f"Y esta es la lista sumando 3 a cada elemento --> {lista_mas_3}")    

# %% [markdown]
# 16.-Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
# todas las palabras que sean más largas que n. Usa la función  filter()

# %%
def len_palabras(palabra,n): #Definimos una función que evaluúa si la palabra tiene más de n letras
    return len(palabra) > n
n = 5 #definimos n
mis_palabras_largas = list(filter(lambda p: len_palabras(p,n),mis_palabras)) #filtramos la lista con un lambda que utiliza la función inicial
print(f"Esta es la lista de palabras ---> {mis_palabras}")
print(f"Y estas son las que tienen más de {n} letras ---> {(mis_palabras_largas)}")

# %% [markdown]
# 17.-Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, (5,7,2)
# corresponde al número quinientos setenta y dos (572). Usa la función  reduce()

# %%
from functools import reduce

def junta_numeros(n1,n2): #Creamos la función que encarga de concatenar cada dígito
    cifra = str(n1) + str(n2)
    return cifra    
numero_descompuesto = [5,7,2]
mi_cifra_texto = reduce(junta_numeros,numero_descompuesto) #esta función nos devuelve un texto
mi_cifra = int(mi_cifra_texto) #convertimos el resultado a número por si tenemos que operar con él

print(f"Este es el resultado en TEXTO: {mi_cifra_texto}")
print(type(mi_cifra_texto))
print(f"Esta es el resultado en NÚMERO: {mi_cifra}, se puede operar con él: Mi_cifra x 2 = {mi_cifra*2}")
print(type(mi_cifra))

# %%
#Solución alternativa sin reduce()
lista = [5,7,2]
def pasa_a_texto(n):
    return str(n)
lista_int = map(pasa_a_texto,lista)
cifra =("".join(lista_int))
print(cifra)
type(cifra)


# %% [markdown]
# 18.-Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
# 90. Usa la función  filter()

# %%
nota_corte = 90
alumnos = [ #Creamos la lista de alumnos con sus atributos
    {"nombre":"amaya", "edad": 17,"calificacion": 92},
    {"nombre":"daniel", "edad": 20,"calificacion": 83},
    {"nombre":"sara", "edad": 22,"calificacion": 99}, 
    {"nombre":"sergio", "edad": 49,"calificacion": 62},
    {"nombre":"paticia", "edad": 50,"calificacion": 90} #Creamos uno justo con 90 para verificar que lo incluye en la lista
]
alumnos_destacados = list(filter(lambda x: x["calificacion"] >= 90, alumnos)) #Filtramos los alumnos con calificaciones de 90 puntos o mayores
listar_alumnos = list(map(lambda n : n["nombre"], alumnos_destacados)) # Creamos una lista con los nombres
#print(alumnos_destacados) #Solo para verificar que funciona
if len(listar_alumnos) > 0: #Nos aseguramos de que la lista no esté vacía, por si ninguno ha superado la nota requerida...
    print(f"Estos son los {len(listar_alumnos)} alumnos que han superado la calificación de {nota_corte} puntos: {listar_alumnos}")
else:
    print("Ningún estudiante ha superado la calificación requerida 😯")


# %% [markdown]
# 19.-Crea una función  lambda  que filtre los números impares de una lista dada.

# %%
lambda_lista_impar = lambda lista : [x for x in lista if x % 2 != 0]
print(f"Esta es la lista original de numeros ---> {mis_numeros}")
print(f"Y estos son los impares de esa lista ---> {lambda_lista_impar(mis_numeros)}")

# %% [markdown]
# 20.-Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
# filter()

# %%
lista_mix = [1,"melocoton", 21, "trapecista", 5, 4.8]
lista_int = list(filter(lambda x: type(x) == int, lista_mix)) # si quisieramos que cogiera todo lo que sean "números", añadiríamos esto: type(x) == int or type(x) == float,
print(lista_int)

# %% [markdown]
# 21.-Crea una función que calcule el cubo de un número dado mediante una función  lambda

# %%
mi_numero_base = input("introducza un número")
cubo = lambda x :x **3
try:
    print(cubo(int(mi_numero_base)))
except ValueError:
    print("Por favor, introducza un número válido")


# %% [markdown]
# 22.-Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función  reduce() 

# %%
print(mis_numeros) # Reutilizamos la lista que ya definimos anteriormente
def calcula_producto(n1,n2):
    resultado = n1 * n2
    return resultado
producto = reduce(calcula_producto,mis_numeros)
print(producto)

# %% [markdown]
# 23.-Concatena una lista de palabras.Usa la función  reduce()
# 

# %%
#Reutilizamos la variable mis_palabras
print(mis_palabras)

def concat_palabras(p1, p2):
    resultado = p1 + " " + p2 #incluimos una espacio entre cada palabra, podría ser cualquier otro separador
    return resultado
frase = reduce(concat_palabras, mis_palabras)

print(frase)

# %% [markdown]
# 24.-Calcula la diferencia total en los valores de una lista. Usa la función  reduce() .

# %%
#Reutilizamos las variables lista1 y lista2
def suma_lista(n1,n2):
    resultado = n1+ n2
    return resultado
suma1=reduce(suma_lista,lista1)
suma2=reduce(suma_lista,lista2)
diferencia_de_listas= suma1 - suma2
print(f"Esta es la primera lista ---> {lista1} que suma {suma1}")
print(f"Esta es la primera lista ---> {lista2} que suma {suma2}")
print("La diferencia de las dos listas es", diferencia_de_listas)

# %% [markdown]
# 25.-Crea una función que cuente el número de caracteres en una cadena de texto dada.

# %%
#Reutilizamos la variable mi_palabra y la función cuenta_letras
mi_frase = "Esta es la frase que queremos contar"
numero_letras_palabra = cuenta_letras(mi_palabra)
print(f"La cadena '{numero_letras_palabra[0]}' tiene {numero_letras_palabra[1]} caracteres")
numero_letras_frase = cuenta_letras(mi_frase)
print(f"La cadena '{numero_letras_frase[0]}' tiene {numero_letras_frase[1]} caracteres (espacios incluidos)")

# %% [markdown]
# 26.-Crea una función  lambda  que calcule el resto de la división entre dos números dados

# %%
#Reutilizamos las variables dividendo y divisor
calcula_resto = lambda x,y : x % y
mi_resto = calcula_resto(dividendo, divisor)
print(f"El resto de dividir {dividendo} entre {divisor} es: {mi_resto}")

# %% [markdown]
# 27.-Crea una función que calcule el promedio de una lista de números.

# %%
#Reutilizamos la variable lista1
def calcula_promedio(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)
try:
    print(f"El promedio de esta lista de numeros {lista1} es {calcula_promedio(lista1)}")
except ZeroDivisionError:
    print(f"La lista de numeros no puede estar vacía!")

# %% [markdown]
# 28.-Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# %%
def duplicados(lista):
    control = [] #Iniciamos una lista vacía
    for x in lista:
        if x in control:       
            return x  #evaluamos si el primer elemento de la lista ya está en la lista (que inicialmente está vacía)         
        else: 
            control.append(x) #vamos añadiendo cada elemento a la lista, y volvemos a evaluar el siguiente
    return None         
lista_elementos = ["Avellana","Azul","Cielo", "melocoton", 8, 9,"Cielo"]    
elemento_duplicado= duplicados(lista_elementos)
if elemento_duplicado: #Si la lista contiene algún elemento, la imprimimos
    print(elemento_duplicado)
else:
    print("no hay duplicados en esta lista") # si no, mostramos un mensaje

# %% [markdown]
# 29.-Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
# carácter '#', excepto los últimos cuatro

# %%
def enmascarar(texto):
    palabra=str(texto)
    corte= len(palabra)-4 #Definimos en número de caracteres que vamos a enmascarar (todos menos los 4 últimos)
    inicio_palabra = "#" * corte +"_" #Añadimos un "_" para distinguir mejor las dos partes
    fin_palabra = palabra[corte:] #Recortamos el final de la cadena de texto 
    palabra_enmascarada = inicio_palabra + fin_palabra #concatenamos las # con el final de la cadena
    return palabra_enmascarada

mi_palabra = "murciélago"
mi_tlf = 609609609
mi_palabra_enmascarada= enmascarar(mi_palabra)
print(f"Esta es la palabra original ---> {mi_palabra} y así queda enmascarada ---> {mi_palabra_enmascarada}")
mi_tlf_enmascarado = enmascarar(mi_tlf)
print(f"Este es teléfono original ---> {mi_tlf} y así queda enmascarado ---> {mi_tlf_enmascarado}")
        

# %% [markdown]
# 30.-Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
# pero en diferente orden

# %%
def anagrama(p1,p2):
    if sorted(p1.lower()) == sorted(p2.lower()): #probé primero con SET() pero fallaba si había letras repetidas
        print(f"'{p1}' y '{p2}' SI son anagramas")
    else: 
        print(f"'{p1}' y '{p2}' NO son anagramas")
palabra1 = "SERGIO"
palabra2 = "RIESGO"
palabra3 = "MOLINERO"
palabra4 = "LIMONERO"
anagrama(palabra1,palabra2)
anagrama(palabra1,palabra3)
anagrama(palabra3,palabra4)

# %% [markdown]
# 31.-Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
# lanza una excepción

# %%
def nombres():
    numero_amigos =int(input("¿Cuántos amigos desea agregar a la lista?"))
    lista_nombres = []
    while len(lista_nombres) < numero_amigos:        
        nombre = input("Introduzca un nombre")
        lista_nombres.append(nombre)
        print(f"{nombre} añadido a la lista, añade el siguiente")
    print(f"Esta es su lista de amigos {lista_nombres}")
    print("Introduzca ahora el nombre que desea buscar")
    return lista_nombres   
try:
    mis_amigos = nombres()
    buscado= input("introduzca el nombre que desea buscar")
    if buscado in mis_amigos:
        print(f"su amigo '{buscado}' SI está en la lista")
    else:
        raise Exception(f"'{buscado}' NO consta en la lista de amigos")
except ValueError:
      print("Intruzca un número correcto")
except Exception as e:
      print(e)

# %% [markdown]
# 32.-Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
# no trabaja aquí

# %%
empleados = { #generamos nuestro diccionario de empleados
    "Juan Torres":"Gerente",
    "Pedro Casado": "Supervisor",
    "Miguel Rodríguez": "Operario",
    "Luis Pérez":"Secretario" 
}
def buscar_nombre(listado): #esta función nos pide que intruzcamos un nombre, debe ser exacto!
    nombre_empleado = input("Intruduzca el nombre del empleado a buscar")
    nombres = list(listado.keys()) #genera una lista con los "nombres" de los empleados (keys)
    if nombre_empleado in nombres:
            puesto = listado.get(nombre_empleado,1) #si encuentra el nombre, entonces busca que puesto ocupa y lo guaarda en una variable
            print(f"El señor {nombre_empleado} trabaja en esta empresa como {puesto}")
    else:
        print("Ese señor no trabaja aquí") # Si el nombre no está en el diccionario, nos informa
    
puesto_info = buscar_nombre(empleados)

# %% [markdown]
# 33.-Crea una función  lambda  que sume elementos correspondientes de dos listas dadas

# %%
suma_listas = lambda list1,list2 : list(map(lambda x,y : x+y,list1, list2)) #creamos una función lambda que recibe dos listas, y aplica una subfunción lambda que suma los elemento de cada tupla y devuelve una lista
unidades = [1,2,3]
decenas = [10,20,30]
parejas = suma_listas(unidades, decenas)
print(parejas)

# %% [markdown]
# 34.-Crea la clase  Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:  
# crecer_tronco ,  nueva_rama ,  crecer_ramas ,  quitar_rama  e  info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.  
# 
# Código a seguir:
# 
#         1.- Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.  
#         2.- Implementar el método  crecer_tronco  para aumentar la longitud del tronco en una unidad.  
#         3.- Implementar el método  nueva_rama  para agregar una nueva rama de longitud 1 a la lista de ramas.  
#         4.- Implementar el método  crecer_ramas  para aumentar en una unidad la longitud de todas las ramas existentes.  
#         5.- Implementar el método  quitar_rama  para eliminar una rama en una posición específica.  
#         6.- Implementar el método info_arbol  para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.  
#         
# Caso de uso:  
# 
#         1.- Crear un árbol.  
#         2.- Hacer crecer el tronco del árbol una unidad.  
#         3.- Añadir una nueva rama al árbol.  
#         4.- Hacer crecer todas las ramas del árbol una unidad.  
#         5.- Añadir dos nuevas ramas al árbol.  
#         6.- Retirar la rama situada en la posición 2.  
#         7.- Obtener información sobre el árbol

# %%
class Rama:
    def __init__(self,nombre,longitud):
        self.nombre = nombre
        self.longitud = longitud
    
    def __repr__(self):
        return f"{self.nombre}: ({self.longitud}cm)"

    def crecer_ramas(self, valor):
        self.longitud += valor

class Arbol:
    def __init__(self,nombre,tronco):
        self.nombre = nombre
        self.tronco = tronco
        self.ramas = []
    
    def __repr__(self):
        return f"{self.nombre}---> Altura:({self.tronco}metros)"

    def crecer_tronco(self,valor):
        self.tronco += valor
        print(f"El tronco del {self.nombre} ahora mide {self.tronco} metros")

    def añadir_rama(self,nombre, tamaño):
        nueva_rama = Rama(nombre, tamaño)
        self.ramas.append(nueva_rama)
        print(f"Se ha AÑADIDO {nueva_rama}")
        
    def crecer_ramas(self, valor):
             for rama in self.ramas:
                rama.crecer_ramas(valor) 

    def quitar_rama_nombre(self, nombre):
        for rama in self.ramas:
            if rama.nombre == nombre:
                self.ramas.remove(rama)
                print(f"Se ha PODADO {rama}")
                break
            else:
                print("no hay ninguna rama con ese nombre")

    def quitar_rama_posicion(self,posicion):
            if len(self.ramas) > 0:
                rama_eliminada = self.ramas.pop(posicion)
                print(f"Se ha PODADO la rama que estaba en la posición {posicion}: {rama_eliminada}")

    def info(self):
        print(f"Mi {self.nombre} tiene una altura de {self.tronco} metros y {len(self.ramas)} ramas: {self.ramas}")
    
sauce = Arbol ("sauce", 8)
pino = Arbol ("pino",6)

print(f"Comenzamos con un {sauce.nombre} que tiene una altura de {sauce.tronco} metros y {len(sauce.ramas)} ramas")
sauce.crecer_tronco(1)
sauce.añadir_rama("Rama_A",20)
sauce.crecer_ramas(15)
sauce.añadir_rama("Rama_B",40)
sauce.añadir_rama("Rama_C",80)
sauce.crecer_ramas(8)
sauce.añadir_rama("Rama_D",50)
sauce.quitar_rama_posicion(2)
sauce.quitar_rama_nombre("Rama_A")
sauce.info()

        

# %% [markdown]
# 36.-Crea la clase  *UsuarioBanco* ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.  
# Proporciona métodos para realizar operaciones como *retirar* dinero, *transferir* dinero desde otro usuario y *agregar* dinero al *saldo*.
# Código a seguir:
# 
#     1.-Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante  True  y  False.  
#     2.-Implementar el método  retirar_dinero  para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.  
#     3.-Implementar el método  transferir_dinero  para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.  
#     4.-Implementar el método  agregar_dinero  para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 
#     1.-Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.  
#     2.-Agregar 20 unidades de saldo de "Bob".  
#     3.-Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".  
#     4.-Retirar 50 unidades de saldo a "Alicia"
# 

# %%
class UsuarioBanco:
    def __init__(self, nombre,saldo,cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
      
    def consulta_saldo(self):
        if self.cuenta_corriente:
            print(f"Hola {self.nombre}, su saldo es de {self.saldo}€\n")
        else:
            print("Primero abra una cuenta con nosotros")
    
    def ingresar(self):
        if self.cuenta_corriente:
             ingreso = int(input("Indique la cantidad a ingresar"))
             self.saldo += ingreso
             print(f"Se han ingresado {ingreso}€ en su cuenta")
             print(f"Su nuevo saldo es de {self.saldo}€\n")
        else:
            print("Primero abra una cuenta con nosotros")
    def retirar(self):
        if self.cuenta_corriente:
            reintegro = int(input("Indique la cantidad que desea sacar"))
            if reintegro < self.saldo:
                self.saldo -= reintegro
                print(f"Ha retirado {reintegro}€ de su cuenta")
                print(f"Su nuevo saldo es de {self.saldo}€\n")
            else:
                print("Usted no tiene tanto dinero\n")
        else:
            print("Primero abra una cuenta con nosotros")

    def transferencia(self,destino,importe):
        if self.cuenta_corriente:
            if importe < self.saldo:
                    self.saldo -= importe
                    destino.saldo += importe
                    print(f"Ha transferido {importe}€ a {destino.nombre}")
                    print(f"Su nuevo saldo es de {self.saldo}€\n")
            else:
                print("Usted no tiene tanto dinero\n")
        else:
            print("Primero abra una cuenta con nosotros")

Alicia = UsuarioBanco ("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True) 
usuarios = {
    "Alicia" : Alicia,
    "Bob" :Bob
}

# %%
#Este bloque solo sirve para comprobar que funciona todo
Alicia.consulta_saldo()
Bob.ingresar()
Alicia.retirar()
Alicia.transferencia(Bob,12)

# %%
login = input("Introduzca su nombre de usuario: ")
if login in usuarios:
    usuario =usuarios[login]
    print(f"Hola {login} ¿Qué operación desea realizar?\n")
    while True:
        print(f"MENÚ PRINCIPAL\n \n 1 : Consulta Saldo\n 2 : Ingresar dinero\n 3 : Sacar dinero\n 4 : Hacer transferencia\n 5 : Salir\n ------------"  )
        opcion = input("Selecione una opción")
        if opcion == "1":
            usuario.consulta_saldo()
        elif opcion == "2":
            usuario.ingresar()
        elif opcion == "3":
            usuario.retirar()
        elif opcion == "4":
            destino = input("Seleccione el destino de la transferencia")
            importe = int(input("Qué cantidad quiere ingresar"))
            usuario.transferencia(usuarios[destino],importe)
        elif opcion == "5":
            print("Hasta pronto!")
            break
else:
     print("Usuario no encontrado")
    


# %% [markdown]
# 37.- Crea una función llamada  procesar_texto  que procesa un texto según la opción especificada:  contar_palabras , reemplazar_palabras ,  eliminar_palabra .  
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función  procesar_texto .
# Código a seguir:
# 
# 1.-Crear una función  contar_palabras  para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.  
# 2.-Crear una función  reemplazar_palabras  para remplazar una  palabra_original  del texto por una  palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.  
# 3.-Crear una función  eliminar_palabra  para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.  
# 4.-Crear la función  procesar_texto  que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# 
# Caso de uso:
# 
# Comprueba el funcionamiento completo de la función  procesar_text

# %%
def contar_palabras(texto):
    lista_palabras = texto.lower().split()
    conteo = {} 
    for p in lista_palabras:
        if p in conteo:
            conteo[p] += 1
        else:
            conteo[p] = 1    
    return conteo 

def reemplazar (texto, palabra_original, palabra_nueva):
    print(f"Se ha sustituido '{palabra_original}' por '{palabra_nueva}'")
    return texto.replace(palabra_original, palabra_nueva)
       
        
   
def eliminar(texto,palabra):
    lista_palabras = texto.lower().split()
    frase = " ".join([p for p in lista_palabras if p != palabra])
    print(f"Se ha eliminado la palabra '{palabra}'")
    return frase


def procesar_texto(texto):
    while True:
        print("-MENÚ PROCESAMIENTO DE TEXTO- Selecione una opción (1-4):\n   1 : CONTAR Palabras\n   2 : REEMPLAZAR palabra\n   3 : ELIMINAR palabra\n   4 : SALIR")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            recuento = contar_palabras(mi_texto)
            print(f"Este es es el recuento de palabras: {recuento}\n")
        elif opcion == "2":
            texto_reemplazado = reemplazar(mi_texto,"amarillo","azul")
            print(f"{texto_reemplazado}\n")
        elif opcion == "3":
            eliminado = eliminar(mi_texto,"sol")
            print(f"{eliminado}\n")
        elif opcion == "4":
            print("Hasta pronto!")
            break
        else:
            print(f"{opcion} no es una opción válida\n")



mi_texto = "El sol es amarillo como el trigo amarillo"    
procesar_texto(mi_texto)


# %% [markdown]
# 38.-Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

# %%
try:
    hora_actual = int(input("por favor, introduzca lo hora actual en formato 24H (0-23)"))
    if hora_actual not in range(0,24):
        print("Por favor, introduzca una hora entre 0 y 23")
    elif  6 <= hora_actual < 12:
        print(f"Buenos días, son las {hora_actual}H")
    elif 12 <= hora_actual <= 19:
        print(f"Buenas tardes, son las {hora_actual}H")
    else: 
        print(f"Buenas noches, son las {hora_actual}H")
except ValueError:
    print("por favor, introduzca una hora correcta")

# %%
#Esta otra versión utliza la hora real (sin necesidad de que el usuario la introduzca)
from datetime import datetime
hora_auto = int(datetime.now().strftime("%H"))
hora_min = datetime.now().strftime("%H:%M")

if hora_auto not in range(0,24):
        print("Por favor, introduzca una hora entre 0 y 23")
elif  6 <= hora_auto < 12:
        print(f"Buenos días, son las {hora_min}H")
elif 12 <= hora_auto <= 19:
        print(f"Buenas tardes, son las {hora_min}H")
else: 
        print(f"Buenas noches, son las {hora_min}H")


# %% [markdown]
# 39.-Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.  
# Las reglas de calificación son:  
# de 0 a 69 insuficiente  
# de 70 a 79 bien  
# de 80 a 89 muy bien  
# de 90 a 100 excelente

# %%
class Alumno:
    def __init__(self, nombre, calificacion): #Definimos la estructura
        self.nombre = nombre
        self.calificacion = calificacion

    def __repr__(self): #Definimos la función que devuelve la calificación
        return f"{self.nombre} tiene una calificacion de {self.calificacion}"

    def evaluar(self): # y la que evalúa la calificación
        nota = self.calificacion
        if  0 <= nota <= 69:
            return "Insuficiente"
        elif 70 <= nota <= 79:
            return "Bien"
        elif 80 <= nota <= 89:
            return "Muy bien"
        elif nota >= 90:
            return "Excelente"
    
Patricia = Alumno("Patricia",50)
Sergio = Alumno("Sergio",65)
Sara = Alumno("Sara", 75)
Daniel = Alumno("Daniel",85)
Amaya = Alumno("Amaya",95)
Manolo = Alumno("Manolo", 70)
Julian = Alumno("Julian",80)
alumnado = [Patricia, Sergio, Sara, Daniel, Amaya, Manolo, Julian]
for n in alumnado:
    print(f"{n} ---> {n.evaluar()}")


# %% [markdown]
# 40.- Escribe una función que tome dos parámetros:  figura  (una cadena que puede ser  "rectangulo" ,  "circulo"  o 
# "triangulo" ) y  datos  (una tupla con los datos necesarios para calcular el área de la figura).

# %%
import math # importamos esta librería para definir "PI"

def calculo_area(forma,datos): #definimos el cálculo del area para cada forma 
    if forma == "circulo":
        radio = datos[0] # tomamos la primera posición de la tupla (único dato)
        return math.pi*(radio**2) #utlizamos math.pi para mayor precisión
    elif forma == "rectangulo":
        base, altura = datos 
        return base * altura
    elif forma == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    
area_cir = round(calculo_area("circulo",(2.6,)),2) #probamos con un círculo de 2.6cm de radio
print(f"El área de su CÍRCULO es de {area_cir} centímetros cuadrados\n")

area_tri = round(calculo_area("triangulo",(2.5,3,)),2) #probamos con un triángulo de 2.5 x 3
print(f"El área de su TRIÁNGULO es de {area_tri} centímetros cuadrados\n") 

area_rec = round(calculo_area("rectangulo", (3.2,2.1,)),2) #probamos con un rectángulo de 3.2 x 2.1
print(f"El área de su RECTÁNGULO es de {area_rec} centímetros cuadrados\n")

# %%
#Esta otra alternativa, funcionaría con datos introducidos por el usuario 
import math 
while True:
        print("-CÁLCULO DE ÁREA- Selecione una opción (1-4):\n   1 : RECTÁNGULO\n   2 : CÍRCULO\n   3 : TRIÁNGULO\n   4 : SALIR")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            altura = float(input("Introduzca la ALTURA del RECTÁNGULO en centímetros"))
            base = float(input("Introduzca el BASE del RECTÁNGULO en centímetros"))
            area = altura * base
            print(f"El área de su RECTÁNGULO es de {area} centímetros cuadrados\n")

        elif opcion == "2":
            radio = float(input("Introduzca el RADIO del CÍRCULO en centímetros"))
            area = round(math.pi*(radio**2),2)
            print(f"El área de su CÍRCULO es de {area} centímetros cuadrados\n")

        elif opcion == "3":
            altura = float(input("Introduzca la ALTURA del TRIÁNGULO en centímetros"))
            base = float(input("Introduzca la BASE del TRIÁNGULO en centímetros"))
            area = round((altura * base)/2,2) 
            print(f"El área de su TRIÁNGULO es de {area} centímetros cuadrados\n")

        elif opcion == "4":
            print("Hasta pronto!")
            break
        
        else:
            print(f"{opcion} no es una opción válida\n")     

# %% [markdown]
# 41.- En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
# programa de Python.

# %%
precio_original = float(input("por favor, introduzca el precio original"))
cupon_dto = str.upper(input("¿Tiene un cupón de descuento? (SI/NO): ")) # nos aseguramos de que funcione con mayúsculas y minúsculas con upper()
if cupon_dto == "SI":
    importe_dto = float(input("Introduzca el valor de su descuento")) # usamos float por si acaso los descuentos son con decimales
    if 0 <= importe_dto <= precio_original: #si el descuento es válido
        precio_final = round((precio_original - importe_dto),2) #lo restamos al precio original
        print(f"El precio final de su compra es de {precio_final} € (descuento de {importe_dto}€)")
    elif 0 > importe_dto: #por si nos dan un valor negativo ¿?
        print(f"El importe de su descuento ({importe_dto}) no es válido")
    elif importe_dto > precio_original: #por si el valor del descuento supera el precio
        print(f"Su compra le sale GRATIS!! pero desperdicia {importe_dto-precio_original}€ de su cupón")
   
else:
    print(f"El precio de su compra es de {precio_original}€") # si no tiene descuento, paga el precio original


