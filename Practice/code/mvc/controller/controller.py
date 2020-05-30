from model.model import Model
from view.view import View
from datetime import date
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    def main_menu(self):
        o='0'
        while o!=3:
            self.view.menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.menu_cartelera()
            elif o == '2':
                self.view.ask('Admin: ')
                ad = input()
                self.view.ask('Password: ')
                pass_ad = input()
                out = self.model.login(ad,pass_ad)
                if out == True:
                    self.menu_admin()
                else:
                    self.view.msg('CREDENCIALES INCORRECTAS')
            elif o == '3':
                self.view.end()
                self.model.close_db()
                return
            else:
                self.view.no_valid_option()
        return
    
    #Usuario regular
    def menu_cartelera(self):
        o='0'
        while o!=3:
            self.view.menu_cartelera()
            self.view.option('3')
            o = input()
            if o == '1':
                fecha = date.today()
                self.cartelera_de_dia(fecha)
            elif o == '2':
                self.view.ask('Ingrese la Fecha (YYYY-MM-DD): ')
                fecha = input()
                self.cartelera_de_dia(fecha)
            elif o == '3':
                return
            else:
                self.view.no_valid_option()
        return
    
    def cartelera_de_dia(self, fecha):
        p = self.model.leer_peliculas()
        if type(p) == list:
            f = self.model.leer_funciones_dia(fecha)
            if type(f) == list:
                peliculas_del_dia = []
                cont = 0
                for recordF in f:
                    for recordP in p:
                        contp = 0
                        if recordP[0] == recordF[2]:
                            if cont == 0:
                                peliculas_del_dia.append(recordP)
                            else:
                                for x in peliculas_del_dia:
                                    if recordP == x:
                                        contp+=1
                                if contp==0:
                                    peliculas_del_dia.append(recordP)
                    cont+=1
                self.view.leer_cartelera_dia(peliculas_del_dia,f)
                self.view.ask('¿Desea comprar un boleto?(Y/N): ')
                r = input()
                if r.lower() == 'y':
                    self.view.ask('Ingrese el numero de Funcion: ')
                    f = input()
                    while r.lower() == 'y':                    
                        b = self.comprar_boleto(f)
                        if b == True:
                            self.view.ask('¿Desea comprar OTRO boleto de esta misma funcion?(Y/N): ')
                            r = input()
                        else:
                            r='n'
            else:
                self.view.error('PROBLEMA AL LEER LAS FUNCIONES')
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS')
    
    def comprar_boleto(self, id_funcion):
        caracteres_asientos= []
        funcion = self.model.leer_funcion(id_funcion)
        if type(funcion) == tuple:
            id_sala = funcion[1]
            sala = self.model.leer_sala(id_sala)
            asientos_sala = self.model.leer_asientos_sala(id_sala)
            boletos = self.model.leer_boletos()
            for recordA in asientos_sala:
                j = 0
                for recordB in boletos:
                    if recordB[1] == recordA[0] and recordB[0] == int(id_funcion): 
                        j = 1
                        caracteres_asientos.append('X')
                if j == 0:
                    caracteres_asientos.append('0')
            self.view.leer_asientos_sala(caracteres_asientos,sala)
            self.view.ask('¿Que fila quieres?: ')
            fila = input()
            self.view.ask('¿Que asiento quieres?: ')
            asiento = input()
            filas = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12}
            asi = self.model.leer_asiento(id_sala,asiento,filas[fila.upper()])
            check = self.model.leer_boleto(id_funcion,asi[0])
            if type(check) != tuple: 
                o = self.model.crear_boleto(id_funcion,asi[0],)
                if o == True:
                    self.view.msg('¡Boleto comprado exitosamente!')
                    self.leer_boleto(id_funcion,asiento,filas[fila.upper()])
                else:
                    self.view.error(o)
            else: 
                print('¡Asiento ocupado, escoge otro!')
        else:
            self.view.msg('ERROR. FUNCION INVALIDA')
            return False
        return True
    def leer_boleto(self,id_funcion,asiento, fila):
        fun = self.model.leer_funcion(id_funcion)
        peli = self.model.leer_pelicula(fun[2])
        self.view.leer_boleto(peli[1],peli[2],fun[3],fun[4], asiento, fila)

    #Administracion
    def menu_admin(self):
        o='0'
        while o!=5:
            self.view.menu_admin()
            self.view.option('5')
            o = input()
            if o == '1':
                self.menu_funciones()
            elif o == '2':
                self.menu_peliculas()
            elif o == '3':
                self.menu_salas()
            elif o == '4':
                self.menu_administradores()
            elif o == '5':
                return
            else:
                self.view.no_valid_option()
        return

    #Funciones
    def menu_funciones(self):
        o='0'
        while o!=9:
            self.view.menu_funciones()
            self.view.option('9')
            o = input()
            if o == '1':
                self.crear_funcion()
            elif o == '2':
                self.leer_funciones()
            elif o == '3':
                self.leer_funcion()
            elif o == '4':
                self.leer_funciones_dia()
            elif o == '5':
                self.leer_funciones_peli()
            elif o == '6':
                self.leer_funciones_sala()
            elif o == '7':
                self.actualizar_funcion()
            elif o == '8':
                self.eliminar_funcion()
            elif o == '9':
                return
            else:
                self.view.no_valid_option()
        return
    def ask_fun(self):
        self.view.ask('ID Sala: ')
        id_s = input()
        self.view.ask('ID Pelicula: ')
        id_p = input()
        self.view.ask('Fecha(YYYY-MM-DD): ')
        fe = input()
        self.view.ask('Hora(HH:MM:SS): ')
        ho = input()
        return [id_s, id_p, fe, ho]

    def crear_funcion(self):
        id_s, id_p, fe, ho = self.ask_fun()
        out = self.model.crear_funcion(id_s, id_p, fe, ho)
        if out == True:
            self.view.msg('Funcion agregada correctamente')
        else:
            if out.errno == 1062:
                self.view.error('LA FUNCION ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISE.')
        return
    def leer_funciones(self):
        out = self.model.leer_funciones()
        if type(out) == list:
            self.view.leer_funciones(out)
        else:
            self.view.error('PROBLEMA AL VER FUNCIONES. REVISA.')
        return
    def leer_funcion(self):
        self.view.ask('ID Funcion: ')
        id_f = input()
        out = self.model.leer_funcion(id_f)
        if type(out) == tuple:
            self.view.leer_funcion(out)    
        else:
            if out == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER FUNCION. REVISA.') 
        return
    def leer_funciones_dia(self):
        self.view.ask('Dia(YYYY-MM-DD): ')
        dia = input()
        out = self.model.leer_funciones_dia(dia)
        if type(out) == list:
            self.view.leer_funciones(out)
        else:
            self.view.error('PROBLEMA AL VER FUNCIONES. REVISA.')
        return
    def leer_funciones_peli(self):
        self.view.ask('ID Peli: ')
        id_p = input()
        out = self.model.leer_funciones_pelicula(id_p)
        if type(out) == list:
            self.view.leer_funciones(out)
        else:
            self.view.error('PROBLEMA AL VER FUNCIONES. REVISA.')
        return
    def leer_funciones_sala(self):
        self.view.ask('ID Sala: ')
        id_s = input()
        out = self.model.leer_funciones_sala(id_s)
        if type(out) == list:
            self.view.leer_funciones(out)
        else:
            self.view.error('PROBLEMA AL VER FUNCIONES. REVISA.')
        return

    def actualizar_funcion(self):
        self.view.ask('ID Funcion: ')
        id_f = input()
        out = self.model.leer_funcion(id_f)
        if type(out) == tuple:
            self.view.leer_funcion(out)    
        else:
            if out == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER FUNCION. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_fun()
        fields, vals = self.update_lists(['id_sala','id_peli', 'fecha_f','hora_f'],whole_vals)
        vals.append(id_f)
        vals = tuple(vals)
        out = self.model.actualizar_funcion(fields,vals)
        if out == True:
            self.view.ok(id_f,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA')
        return

    def eliminar_funcion(self):
        self.view.ask('ID Funcion: ')
        id_f = input()
        count = self.model.eliminar_funcion(id_f)
        if count != 0:
            self.view.ok(id_f,'borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION. REVISA.')
        return

    #Salas
    def menu_salas(self):
        o='0'
        while o!=6:
            self.view.menu_salas()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_sala()
            elif o == '2':
                self.leer_salas()
            elif o == '3':
                self.leer_sala()
            elif o == '4':
                self.actualizar_sala()
            elif o == '5':
                self.eliminar_sala()
            elif o == '6':
                return
            else:
                self.view.no_valid_option()
        return
    def ask_sala(self):
        self.view.ask('ID Sala: ')
        id_s = input()
        self.view.ask('Filas: ')
        nf = input()
        self.view.ask('Asientos por fila: ')
        na = input()
        return [id_s,nf, na]

    def ask_sala_update(self):
        self.view.ask('Filas: ')
        nf = input()
        self.view.ask('Asientos por fila: ')
        na = input()
        return [nf, na]

    def crear_sala(self):
        print('DIMENSION MAXIMA: 12 Filas x 25 Asientos por fila')
        id_s, nf, na = self.ask_sala()
        out = self.model.crear_sala(id_s,nf, na)
        if out == True:
            self.view.msg('Sala agregada correctamente.')
            i = 1
            while i < int(nf)+1:
                j = 1
                while j < int(na)+1:
                    self.model.crear_asientos_sala(id_s,j,i)
                    j+=1
                print('fila: ', i)
                i+=1
        else:
            if out.errno == 1062:
                self.view.error('LA SALA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA SALA. REVISE.')
        return

    def leer_salas(self):
        out = self.model.leer_salas()
        if type(out) == list:
            self.view.leer_salas(out)
        else:
            self.view.error('PROBLEMA AL VER SALAS. REVISA.')
        return
    def leer_sala(self):
        self.view.ask('ID Sala: ')
        id_a = input()
        out = self.model.leer_sala(id_a)
        if type(out) == tuple:
            self.view.leer_sala(out)    
        else:
            if out == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER SALA. REVISA.') 
        return
    def actualizar_sala(self):
        self.view.ask('ID Sala: ')
        id_s = input()
        out = self.model.leer_sala(id_s)
        if type(out) == tuple:
            self.view.leer_sala(out)    
        else:
            if out == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_sala_update()
        fields, vals = self.update_lists(['num_filas','asientos_por_fila'],whole_vals)
        vals.append(id_s)
        vals = tuple(vals)
        out = self.model.actualizar_sala(fields,vals)
        if out == True:
            self.view.ok(id_s,'actualizado')
            self.model.eliminar_asientos(id_s)
            i = 1
            while i < out[1]+1:
                j = 1
                while j < (out[2]+1):
                    self.model.crear_asientos_sala(id_s,j,i)
                    j+=1
                i+=1
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA')
            print(out)
        return
    def eliminar_sala(self):
        self.view.ask('ID Sala: ')
        id_s = input()
        count = self.model.eliminar_sala(id_s)
        if count != 0:
            self.view.ok(id_s,'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA.')
        return

    #Peliculas
    def menu_peliculas(self):
        o='0'
        while o!=6:
            self.view.menu_peliculas()
            self.view.option('6')
            o = input()
            if o == '1':
                self.crear_pelicula()
            elif o == '2':
                self.leer_peliculas()
            elif o == '3':
                self.leer_pelicula()
            elif o == '4':
                self.actualizar_pelicula()
            elif o == '5':
                self.eliminar_pelicula()
            elif o == '6':
                return
            else:
                self.view.no_valid_option()
        return
    def ask_peli(self):
        self.view.ask('Titulo: ')
        titu = input()
        self.view.ask('Duracion: ')
        dura = input()
        self.view.ask('Director: ')
        dire = input()
        self.view.ask('Sinopsis: ')
        sino = input()
        return [titu, dura, dire, sino]

    def crear_pelicula(self):
        titu, dura, dire, sino = self.ask_peli()
        out = self.model.crear_pelicula(titu, dura, dire, sino)
        if out == True:
            self.view.ok(titu,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA PELICULA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISE.')
        return

    def leer_peliculas(self):
        out = self.model.leer_peliculas()
        if type(out) == list:
            self.view.leer_peliculas(out)
        else:
            self.view.error('PROBLEMA AL VER PELICULAS. REVISA.')
        return

    def leer_pelicula(self):
        self.view.ask('ID Peli: ')
        id_p = input()
        out = self.model.leer_pelicula(id_p)
        if type(out) == tuple:
            self.view.leer_pelicula(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELICULA. REVISA.') 
        return
    def actualizar_pelicula(self):
        self.view.ask('ID Peli: ')
        id_p = input()
        out = self.model.leer_pelicula(id_p)
        if type(out) == tuple:
            self.view.leer_pelicula(out)    
        else:
            if out == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER PELICULA. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_peli()
        fields, vals = self.update_lists(['titulo_p','duracion_p', 'director_p','sinopsis'],whole_vals)
        vals.append(id_p)
        vals = tuple(vals)
        out = self.model.actualizar_peli(fields,vals)
        if out == True:
            self.view.ok(id_p,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA')
            print(out)
        return
    def eliminar_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_p = input()
        count = self.model.eliminar_peli(id_p)
        if count != 0:
            self.view.ok(id_p,'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return
    #administradores
    def menu_administradores(self):
        o='0'
        while o!=5:
            self.view.menu_administradores()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_admin()
            elif o == '2':
                self.leer_admins()
            elif o == '3':
                self.actualizar_admin()
            elif o == '4':
                self.eliminar_admin()
            elif o == '5':
                return
            else:
                self.view.no_valid_option()
        return

    def ask_admin(self):
        self.view.ask('User: ')
        name = input()
        self.view.ask('Password: ')
        passw = input()
        return [name,passw]

    def crear_admin(self):
        name, passw = self.ask_admin()
        out = self.model.crear_admin(name, passw)
        if out == True:
            self.view.ok(name,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ADMIN ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ADMIN. REVISE.')
        return

    def leer_admins(self):
        out = self.model.leer_administradores()
        if type(out) == list:
            self.view.leer_admins(out)
        else:
            self.view.error('PROBLEMA AL VER ADMINISTRADORES. REVISA.')
        return
    def actualizar_admin(self):
        self.view.ask('ID Admin: ')
        id_a = input()
        out = self.model.leer_admin(id_a)
        if type(out) == tuple:
            self.view.leer_admin(out)    
        else:
            if out == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER ADMINISTRADOR. REVISA.') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['user_admin','pass_admin'],whole_vals)
        vals.append(id_a)
        vals = tuple(vals)
        out = self.model.actualizar_admin(fields,vals)
        if out == True:
            self.view.ok(id_a,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR')
        return

    def eliminar_admin(self):
        self.view.ask('ID Admin: ')
        id_a = input()
        count = self.model.eliminar_admin(id_a)
        if count != 0:
            self.view.ok(id_a,'borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ADMINISTRADOR. REVISA.')
        return
    
    
