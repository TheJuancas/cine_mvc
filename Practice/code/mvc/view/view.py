from datetime import datetime
import os

class View:
    def start(self):
        print('--------------------------------------')
        print(' ¡BIENVENIDO AL SISTEMA DE CINE RIZO!  ')
        print('--------------------------------------')

    def end(self):
        print('--------------------------------------')
        print('       ¡GRACIAS, VUELVA PRONTO!       ')
        print('--------------------------------------')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def no_valid_option(self):
        print('Opcion no valida\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('='*(len(str(id))+len(op)+24))
        print(('¡ '+str(id)+' se '+ op +' correctamente !').center(len(str(id))+len(op)+24))
        print('='*(len(str(id))+len(op)+24))

    def error(self, err):
        print('¡ERROR!'.center(len(err)+4))
        print(err.center(len(err)+4))
        print('-'*(len(err)+4))

    #Menus 
    def menu(self):
        
        print('--------------------------------------')
        print('            MENU CINE RIZO            ')
        print('--------------------------------------')
        print('1.- Ver Cartelera')
        print('2.- Administrar')
        print('3.- Salir')
    
    #Administradores
    def menu_admin(self):
        
        print('--------------------------------------')
        print('            ADMINISTRACION            ')
        print('--------------------------------------')
        print('1.- Submenu Funciones')
        print('2.- Submenu Peliculas')
        print('3.- Submenu Salas')
        print('4.- Submenu Administradores')
        print('5.- Salir')

    def leer_admins(self, admins):
        print('-'*22)
        print('ADMINISTRADORES'.center(22))
        print('-'*22)
        print('ID_Admin:'.ljust(11)+'User_name:'.ljust(11))        
        print('-'*55)
        for record in admins:
            print(f'{record[0]:<11}{record[1]:<11}')
        print('-'*22)
    def leer_admin(self, record):
        print('--------------------------------------')
        print('           Administrador:',record[0])
        print('--------------------------------------')
        print('User Name: '.ljust(12), record[1])
        print('Password: '.ljust(12), record[2])
        print('--------------------------------------')
    def menu_funciones(self):
        
        print('--------------------------------------')
        print('          SUBMENU FUNCIONES           ')
        print('--------------------------------------')
        print('1.- Crear Funcion')
        print('2.- Leer Funciones')
        print('3.- Leer Funcion')
        print('4.- Leer Funcion por dia')
        print('5.- Leer Funciones por pelicula')
        print('6.- Leer Funcion por Sala')
        print('7.- Actualizar Funcion')
        print('8.- Eliminar Funciones')
        print('9.- Salir')
    
    def menu_salas(self):
        
        print('--------------------------------------')
        print('            SUBMENU SALAS             ')
        print('--------------------------------------')
        print('1.- Crear Sala')
        print('2.- Leer Salas')
        print('3.- Leer Sala')
        print('4.- Actualizar Sala')
        print('5.- Eliminar Sala')
        print('6.- Salir')

    def menu_peliculas(self):
        
        print('--------------------------------------')
        print('          SUBMENU PELICULAS           ')
        print('--------------------------------------')
        print('1.- Crear Pelicula')
        print('2.- Leer Peliculas')
        print('3.- Leer Pelicula')
        print('4.- Actualizar Pelicula')
        print('5.- Eliminar Pelicula')
        print('6.- Salir')

    def menu_administradores(self):
        
        print('--------------------------------------')
        print('        SUBMENU ADMINISTRADORES       ')
        print('--------------------------------------')
        print('1.- Crear Administrador')
        print('2.- Leer Administradores')
        print('3.- Actualizar Administrador')
        print('4.- Eliminar Administrador')
        print('5.- Salir')

    #Funciones
    def leer_funcion(self, recordP):
        
        print('--------------------------------------')
        print('            Funcion:',recordP[0])
        print('--------------------------------------')
        print('ID: '.ljust(12), recordP[0])
        print('Sala: '.ljust(12), recordP[1])
        print('ID_Pelicula:'.ljust(12), recordP[2])
        print('Fecha: '.ljust(12), recordP[3])
        print('Hora: '.ljust(12), recordP[4])
        print('--------------------------------------')

    def leer_funciones(self, funciones):
        print('-'*55)
        print('FUNCIONES'.center(55))
        print('-'*55)
        print('ID_Funcion:'.ljust(14)+'ID_Sala:'.ljust(11)+'ID_Peli:'.ljust(11)+'Fecha:'.ljust(13)+'Hora:'.ljust(8))        
        print('-'*55)
        for record in funciones:
            print(f'{record[0]:<14}{record[1]:<11}{record[2]:<11}{str(record[3]):<13}{str(record[4]):<8}')
        print('-'*55)

    #Carteleras
    def menu_cartelera(self):
        
        print('--------------------------------------')
        print('               CARTELERA              ')
        print('--------------------------------------')
        print('1.- Cartelera de hoy')
        print('2.- Cartelera de otro dia')
        print('3.- Salir')

    def leer_cartelera_dia(self, peliculas_del_dia,funciones_dia):
        
        for x in peliculas_del_dia:
            self.leer_pelicula(x)
            print('HORARIOS'.center(40))
            for recordF in funciones_dia:
                if recordF[2] == x[0]:
                    print(' '*5,'No. Funcion: ', recordF[0])
                    print(' '*11,'Hora: ', recordF[4])
                    print(' '*11,'Sala: ', recordF[1])
                    print(' '*5,'---------------------')
    
    #Peliculas
    def leer_pelicula(self, recordP):
        print('--------------------------------------')
        print('              ',recordP[1],'           ')
        print('--------------------------------------')
        print('ID Peli: '.ljust(12),recordP[0] )
        print('Duracion: '.ljust(12), recordP[2])
        print('Director: '.ljust(12), recordP[3])
        print('Sinopsis: '.ljust(12),recordP[4])
        print('--------------------------------------')

    def leer_peliculas(self, peliculas):       
        print('-'*55)
        print('PELICULAS'.center(55))
        print('-'*55)
        print('ID:'.ljust(5)+'Titulo:'.ljust(15)+'Duracion:'.ljust(11)+'Director:'.ljust(18)+'Sinopsis:'.ljust(8))        
        print('-'*55)
        for record in peliculas:
            print(f'{record[0]:<5}{record[1]:<15}{str(record[2]):<11}{record[3]:<18}{record[4]:<8}')
        print('-'*55)

    #Salas
    def leer_sala(self, record):
        print('--------------------------------------')
        print('              Sala:',record[0])
        print('--------------------------------------')
        print('Numero de Filas: '.ljust(12), record[1])
        print('Asientos por Fila: '.ljust(12), record[2])
        print('--------------------------------------')

    def leer_salas(self, salas):
        print('-'*35)
        print('Salas'.center(35))
        print('-'*35)
        print('ID:'.ljust(5)+'Num Filas:'.ljust(15)+'Asientos por Fila:'.ljust(20))        
        print('-'*35)
        for record in salas:
            print(f'{record[0]:<5}{record[1]:<15}{record[2]:<20}')
        print('-'*35)

    def leer_asientos_sala(self, caracteres_asientos, sala):
        filas = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L'}  
        print('LOS ASIENTOS OCUPADOS ESTAN MARCADOS CON UNA X')     
        print('  '+'---'*sala[2])
        print('  '+'PANTALLA'.center(sala[2]*3))
        print('')
        i = 0
        cont = 0
        while i < sala[1]:
            j = 0
            print(filas[i+1],end='| ')
            while j < sala[2]:
                print(caracteres_asientos[cont],end='  ')
                j+=1
                cont+=1
            print('')
            i+=1
        i = 0
        print('  '+'---'*sala[2])
        print('   ',end='')
        while i < sala[2]:
            if i+1<10:
                print(i+1,end='  ')
            else:
                print(i+1,end=' ')
            i+=1
        print('')

    def leer_boleto(self,titulo, duracion,fecha, hora,asiento, fila):
        filas = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L'}
        print('--------------------------------------')
        print('              CINE RIZO           ')
        print('--------------------------------------')
        print('Titulo: '.ljust(12),titulo)
        print('Duracion: '.ljust(12), duracion)
        print('Fecha: '.ljust(12), fecha)
        print('Hora: '.ljust(12), hora)
        print('Asiento: '.ljust(12), filas[fila],'-',asiento)
        print('--------------------------------------')
   
                
