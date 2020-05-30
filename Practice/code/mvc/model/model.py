from mysql import connector

class Model:
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()        
    def close_db(self):
        self.cnx.close()
    
    #CRUD METHODS
    
    #Administradores
    def login(self,user_admin,pass_admin):
        try:
            sql = 'SELECT pass_admin FROM administradores WHERE user_admin = %s' 
            vals = (user_admin, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if type(record) == tuple:
                if record[0]==pass_admin:
                    return True
                else:
                    return False
            else:
                return
        except connector.Error as err:
            return err

    def crear_admin(self, user_admin,pass_admin):
        try:
            sql = 'INSERT INTO administradores (`user_admin`, `pass_admin`) VALUES (%s,%s)' 
            vals = (user_admin, pass_admin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        return

    def leer_administradores(self):
        try:
            sql = 'SELECT id_admin, user_admin FROM administradores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    def leer_admin(self, id_admin):
        try:
            sql = 'SELECT * FROM administradores WHERE id_admin = %s' 
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    def eliminar_admin(self, id_admin):
        try:
            sql = 'DELETE FROM administradores WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def actualizar_admin(self,fields, vals):
        try:
            sql = 'UPDATE administradores SET ' + ','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
        return

    def logout(self):
        return
    
    #Salas
    def crear_sala(self, id_sala, num_filas, asientos_por_fila):
        try:
            sql = 'INSERT INTO salas (`id_sala`,`num_filas`, `asientos_por_fila`) VALUES (%s,%s,%s)' 
            vals = (id_sala, num_filas, asientos_por_fila)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        return

    def leer_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s' 
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    def leer_sala_por_dimension(self, id_sala):
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s' 
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def actualizar_sala(self, fields, vals):
        try:
            sql = 'UPDATE salas SET ' + ','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def eliminar_sala(self, id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Peliculas
    def crear_pelicula(self, titulo_p, duracion_p, director_p, sinopsis):
        try:
            sql = 'INSERT INTO peliculas (`titulo_p`, `duracion_p`,`director_p`, `sinopsis`) VALUES (%s,%s,%s,%s)' 
            vals = (titulo_p, duracion_p, director_p, sinopsis)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        return

    def leer_pelicula(self, id_peli):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_peli = %s' 
            vals = (id_peli,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def actualizar_peli(self, fields, vals):
        try:
            sql = 'UPDATE peliculas SET ' + ','.join(fields)+' WHERE id_peli = %s'
            print(sql)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def eliminar_peli(self, id_peli):
        try:
            sql = 'DELETE FROM peliculas WHERE id_peli = %s'
            vals = (id_peli,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Funciones
    def crear_funcion(self, id_sala, id_peli, fecha_f, hora_f):
        try:
            sql = 'INSERT INTO funciones (`id_sala`, `id_peli`,`fecha_f`, `hora_f`) VALUES (%s,%s,%s,%s)' 
            vals = (id_sala, id_peli, fecha_f, hora_f)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def leer_funcion(self, id_funcion):
        try:
            sql = 'SELECT * FROM funciones WHERE id_funcion = %s' 
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_funciones(self):
        try:
            sql = 'SELECT * FROM funciones'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_funciones_dia(self,fecha_f):
        try:
            sql = 'SELECT * FROM funciones WHERE fecha_f = %s'
            vals = (fecha_f, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_funciones_pelicula(self, id_peli):
        try:
            sql = 'SELECT * FROM funciones WHERE id_peli = %s'
            vals = (id_peli, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_funciones_sala(self,id_sala):
        try:
            sql = 'SELECT * FROM funciones WHERE id_sala = %s'
            vals = (id_sala, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def actualizar_funcion(self, fields, vals):
        try:
            sql = 'UPDATE funciones SET ' + ','.join(fields)+' WHERE id_funcion = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def eliminar_funcion(self,id_funcion):
        try:
            sql = 'DELETE FROM funciones WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Asientos
    def crear_asientos_sala(self, id_sala, num_as, fila_as):
        try:
            sql = 'INSERT INTO asientos (`id_sala`, `num_as`, `fila_as`) VALUES (%s,%s,%s)' 
            vals = (id_sala, num_as, fila_as)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err
    def leer_asientos_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM asientos WHERE id_sala = %s'
            vals = (id_sala, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    def leer_asiento(self, id_sala,num_asiento,num_fila):
        try:
            sql = 'SELECT * FROM asientos WHERE id_sala = %s AND num_as = %s and fila_as = %s' 
            vals = (id_sala, num_asiento, num_fila, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    def eliminar_asientos(self, id_sala):
        try:
            sql = 'DELETE FROM asientos WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Boletos
    def crear_boleto(self, id_funcion, id_as):
        try:
            sql = 'INSERT INTO boletos (`id_funcion`, `id_as`) VALUES (%s,%s)' 
            vals = (id_funcion, id_as)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def eliminar_boleto(self, id_funcion, id_as):
        try:
            sql = 'DELETE FROM boletos WHERE id_funcion = %s AND id_as = %s '
            vals = (id_funcion, id_as,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    def leer_boleto(self, id_funcion, id_as):
        try:
            sql = 'SELECT * FROM boletos WHERE id_funcion = %s AND id_as = %s ' 
            vals = (id_funcion, id_as,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_boletos(self):
        try:
            sql = 'SELECT * FROM boletos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_boletos_funcion(self,id_funcion):
        try:
            sql = 'SELECT * FROM boletos WHERE id_funcion = %s'
            vals = (id_funcion, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    