from datetime import date
'''
Created on 14 feb. 2021

@author: mario
'''

class Fecha():
    '''
    classdocs
    '''


    def __init__(self, dia, mes, año):
        '''
        Constructor
        '''
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return '{0}/{1}/{2}'.format(self.dia, self.mes, self.año)

    def formato_largo(self):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        
        return '{0} de {1} de {2}'.format(self.dia, meses[self.mes-1], self.año)
    
    def año_bisiesto(self):
        return self.año % 4 == 0 and (self.año % 100 != 0 or self.año % 400 == 0)
    
    def valida(self):
        
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.año_bisiesto():
            dias_mes[1] += 1
        if self.dia <= 0 or self.dia > dias_mes[self.mes-1]:
            return False 
        if self.mes < 1 or self.mes > 12:
            return False
        '''
        # Si queremos comprobar que el año tiene cuatro digitos
        contador = 0
        if self.año == 0:
            return False
        else:
            contador = 1
            while self.año >= 10:
                contador += 1
                self.año = self.año / 10
            if contador != 4:
                return False 
        '''
        return True 
    
    def es_menor_que(self, la_otra_fecha):
        if self.año < la_otra_fecha.año:
            return True 
        elif self.año > la_otra_fecha.año:
            return False 
        if self.mes < la_otra_fecha.mes:
            return True
        elif self.mes > la_otra_fecha.mes:
            return False 
        return self.dia < la_otra_fecha.dia 
    
    def añadir_dia(self):
        
        self.dia += 1
        return self
    
    def dias_transcurridos(self, fecha2):
        
        fecha1 = date(self.año, self.mes, self.dia)
        fecha2 = date(fecha2.año, fecha2.mes, fecha2.dia)
        contador = (fecha1 - fecha2).days
        return contador
    
    def dia_semana(self):
        fecha = date(self.año, self.mes, self.dia)
        #dia = fecha.strftime('%A')
        dic_dias={'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves',
                'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
        dia = (dic_dias[fecha.strftime('%A').upper()])
        return dia  

def lee_fecha():
    dia = 0
    while dia < 1 or dia > 31:
        dia = int(input('Dia: '))
    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input('Mes: '))
    año = int(input('Año: '))
    
    fecha = Fecha(dia, mes, año)
    
    while fecha.valida():
        return fecha
    else:
        print('La fecha no es correcta introduzcala de nuevo.')
        return lee_fecha()
    

def fecha_es_menor(fecha1, fecha2):
    if fecha1.año < fecha2.año:
        return True 
    elif fecha1.año > fecha2.año:
        return False 
    if fecha1.mes < fecha2.mes:
        return True
    elif fecha1.mes > fecha2.mes:
        return False 
    return fecha1.dia < fecha2.dia         
'''   
    
fecha = lee_fecha()
fecha1 = lee_fecha()  
print(fecha_es_menor(fecha, fecha1))
print(fecha.es_menor_que(fecha1))
print(fecha.añadir_dia())
print(fecha.valida())
print(fecha.formato_largo())
print(fecha.año_bisiesto())

ayer = Fecha(1, 1, 2004)
hoy = Fecha(2, 1, 2004)
print(hoy.dias_transcurridos(ayer))
print(hoy.dia_semana())

'''



