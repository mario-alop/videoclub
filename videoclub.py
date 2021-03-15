#==============================================
# videoclub
#==============================================
# Programa para la gestión de videoClubs.
#==============================================


from fecha import Fecha, lee_fecha
'''
Created on 16 feb. 2021

@author: mario
'''
#==============================================
# Socio
#==============================================
# Clases para almacenar los datos relativos a un socio.
#==============================================

class Socio():
    '''
    classdocs
    '''
    def __init__(self, dni, nombre, telefono, domicilio):
        '''
        Constructor
        '''
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
    
    def __str__(self):
        return 'DNI: {0}\nNombre: {1}\nTeléfono: {2}\nDomicilio: {3} \n'.format(self.dni,
        self.nombre, self.telefono, self.domicilio)

#==============================================
# Pelicula
#==============================================
# Clase para almacenar los datos relativos a un 
# ejemplar de una película. 
#==============================================
        
class Pelicula():
    
    def __init__(self, titulo, genero, dias_permitidos):
        self.titulo = titulo
        self.genero = genero
        self.alquilada = None
        self.fecha_alquiler = None
        self.dias_permitidos = dias_permitidos
    
    def __str__(self):
        cadena = 'Título: {0}\nGénero: {1}\n'.format(self.titulo, self.genero)
        if self.alquilada == None:
            cadena = cadena + 'Disponible\n'
        else:
            cadena = cadena + 'Alquilada a: {0}\n'.format(self.alquilada)
        return cadena

#==============================================0
# Videoclub
#==============================================0
# Almacena dos listas: una de socios y otra de 
# peliculas. Los elementos de la primera lista 
# son de la clase Socio, y los de la segunda, de
# la clase Película.
#==============================================0
    
class Videoclub():
    
    def __init__(self):
        self.socios = []
        self.peliculas = []
    
    def contiene_socio(self, dni):
        # Devuelve True si exixte algún socio con 
        # DNI y False en caso contrario.
        for socio in self.socios:
            if socio.dni == dni:
                return True
        return False
    
    def contiene_pelicula(self, titulo):
        # Devuelve True si existe alguna película
        # del título que nos pasan y False en caso
        # contraroio.
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                return True
        return False
    
    def alta_socio(self, socio):
        # Añade un socio a la lista de socios.
        # No debe existir nigún socio con el mismo DNI
        self.socios.append(socio)
        
    def baja_socio(self, dni):
        # Elimina al socio cuyo DNI es igual a dni.
        #Debe existir un socio con ese DNI.
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break
    
    def alta_pelicula(self, pelicula, ejemplares):
        # Dar de alta un número dado de ejemplares
        # de una película.
        for i in range(ejemplares):
            nuevo_ejemplar = Pelicula(pelicula.titulo, pelicula.genero,
            pelicula.dias_permitidos)
            self.peliculas.append(nuevo_ejemplar)
        
    def baja_pelicula(self, titulo, ejemplares):
        # Da de baja un número de ejemplares de la película
        # cuyo título nos suministran como argumento.
        # Devuelve el número de ejemplares que se dio de baja
        # efectivamente.
        bajas_efectivas = 0
        i = 0
        while i < len(self.peliculas) and bajas_efectivas < ejemplares:
            if self.peliculas[i].titulo == titulo and self.peliculas[i].alquilada == None:
                del self.peliculas[i]
                bajas_efectivas += 1
            else:
                i += 1
        return bajas_efectivas
    
    def alquilar_pelicula(self, titulo, dni):
        # Alquila un ejemplar de la película cuyo título
        # nos indican, al socio con DNI dni. Si no consige 
        # efectuar el alquiler, debuelve False, y True
        # si lo consigue. La fecha de alquiler se fija 
        # automaticamente al día actual.
        # Debe exixtir un socio con DNI suministrado.
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni
                pelicula.fecha_alquiler = hoy
                return True
        return False
                
    def devolver_pelicula(self, titulo, dni):
        # Devuelve un ejemplar de la película cuyo título
        # nos indican que estaba alquilada, al socio con DNI dni.
        # Devuelve el número de días de retraso,o -1 si ningún  
        # ejemplar de la película está alquilada al socio.
        # Debe exixtir un socio con DNI suministrado.
        
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == dni: 
                pelicula.alquilada = None
                dias_retraso = pelicula.fecha_alquiler.dias_transcurridos(hoy)
                return dias_retraso
        return -1
    
    def listado_por_generos(self, genero):
        # Muestra un listado de las películas cuyo género es
        # el indicado. Cada título aparece una sola vez, al 
        # lado del título aparece si hay o no ejemplares disponibles
        # para alquiler.
        disponibles = []
        alquiladas = [] 
        for pelicula in self.peliculas:
            if pelicula.genero == genero:
                if pelicula.alquilada == None and not (pelicula.titulo in disponibles):
                    disponibles.append(pelicula.titulo)
            if pelicula.alquilada != None and not (pelicula.titulo in alquiladas):
                alquiladas.append(pelicula.titulo)
        for titulo in disponibles:
            print(titulo, 'DISPONIBLE')
        for titulo in alquiladas:
            if not (titulo in disponibles):
                print(titulo, 'NO DISPONIBLE')

#==============================================
# Funciones
#==============================================

def menu():
    # Muestra el menú por pantalla y lee una opción de teclado
    # que es el resultado devuelto.
    # La función se asegura de la opción esté entre 0 y 8.
    print('*** VIDEOCLUB ***')
    print('0) Fijar fecha actual')
    print('1) Dar de alta nuevo socio')
    print('2) Dar de baja un socio')
    print('3) Dar de alta nueva película')
    print('4) Dar de baja una película')
    print('5) Alquilar película')
    print('6) Devolver película')
    print('7) Listado por género')
    print('8) Salir')
    
    opcion = int(input('Escoge opción: '))
    while opcion < 0 or opcion > 8:
        opcion = int(input('Escoge opción (entre 0 y 8): '))
    return opcion

def nuevo_socio():
    # Pide por teclado los datos de un socio
    # y devuelve un objeto de la clae Socio.
    dni = input('DNI: ')
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    domicilio = input('Domicilio: ')
    return Socio(dni, nombre, telefono, domicilio)

def nueva_pelicula():
    # Pide por teclado los datos de una nueva 
    # película y devuelve un objeto de la clase Película.
    titulo = input('Título: ')
    genero = input('Género: ')
    dias_permitidos = input('Días permitidos: ')
    return Pelicula(titulo, genero, dias_permitidos)

#==============================================================
# Programa principal
#==============================================================
    
# Fijar fecha actual
hoy = lee_fecha()

videoclub = Videoclub()

opcion = menu()

while opcion != 8:
    
    if opcion == 0:
        print('Cambiar fecha actual')
        hoy = lee_fecha()
    
    elif opcion == 1:
        print('Alta de socio')
        socio = nuevo_socio()
        if videoclub.contiene_socio(socio.dni):
            print('Ya existía un socio con DNI: ', socio.dni)
        else:
            videoclub.alta_socio(socio)
    
    elif opcion == 2:
        print('Baja de socio')
        dni = input('DNI: ')
        if videoclub.contiene_socio(dni):
            videoclub.baja_socio(dni)
            print('Socio con DNI: ', dni, 'dado de baja')
        else:
            print('No existe ningún socio con DNI: ', dni)
    
    elif opcion == 3:
        print('Alta de película')
        pelicula = nueva_pelicula()
        ejemplares = int(input('Ejemplares: '))
        videoclub.alta_pelicula(pelicula, ejemplares)
    
    elif opcion == 4:
        print('Baja de película')
        titulo = input('Título')
        ejemplares = int(input('Ejemplares: '))
        bajas = videoclub.baja_pelicula(titulo, ejemplares)
        if bajas < ejemplares:
            print('Solo puede dar de baja', bajas, 'ejemplares')
        else:
            print('Operación realizada')
    
    elif opcion == 5:
        print('Alquiler de película')
        titulo = input('Título de la película: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            if videoclub.alquilar_pelicula(titulo, dni):
                print('Operación realizada')
            else:
                print('La película no está disponible')
        else:
            if not hay_pelicula:
                print('No hay película títulada ', titulo)
            if not hay_socio:
                print('No hay socio con DNI: ', dni)
    
    elif opcion == 6:
        print('Devolve película: ')
        titulo = input('Título de la película: ')
        dni = input('DNI del socio: ')
        hay_pelicula = videoclub.contiene_pelicula(titulo)
        hay_socio = videoclub.contiene_socio(dni)
        if hay_pelicula and hay_socio:
            resultado = videoclub.devolver_pelicula(titulo, dni)
            if resultado == 0:
                print('Operación realizada')
            elif resultado > 0:
                print('Película entregada con un retraso de ', resultado, ' días')
            else:
                print('La película ', titulo, ' no está alquilada al socio ', dni)
        else:
            if not hay_pelicula:
                print('No hay película títulada ', titulo)
            if not hay_socio:
                print('No hay socio con DNI ', dni)
    
    elif opcion == 7:
        print('Listado por género')
        genero = input('Género: ')
        videoclub.listado_por_generos(genero)
    
    opcion = menu()


        
        
        
        
        
        
    

   