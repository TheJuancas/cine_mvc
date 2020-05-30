CREATE DATABASE IF NOT EXISTS cine_db;
USE cine_db;

create table if not exists administradores
(
	id_admin int not null auto_increment,
    user_admin varchar(16) not null,
    pass_admin varchar(16) not null,
    primary key(id_admin)
)engine=INNODB;

create table if not exists salas
(
	id_sala int not null auto_increment,
    num_filas int not null,
    asientos_por_fila int not null,
    primary key(id_sala)
)engine=INNODB;

create table if not exists peliculas
(
	id_peli int not null auto_increment,
    titulo_p varchar(28) not null,
    duracion_p time not null,
    director_p varchar(45)not null,
    sinopsis varchar(100) not null,
    primary key(id_peli)
)engine = INNODB;

create table if not exists asientos
(
	id_as int not null auto_increment,
    id_sala int not null,
    num_as int not null,
    fila_as int not null,
    primary key(id_as),
    CONSTRAINT fk_sala FOREIGN KEY (id_sala)
    REFERENCES salas(id_sala)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)engine= INNODB;

create table if not exists funciones
(
	id_funcion int not null auto_increment,
    id_sala int not null,
    id_peli int not null,
    fecha_f date not null,
    hora_f time not null,
    primary key(id_funcion),
    CONSTRAINT fk_sala2 FOREIGN KEY (id_sala)
    REFERENCES salas(id_sala)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_peli FOREIGN KEY (id_peli)
    REFERENCES peliculas(id_peli)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)engine = INNODB;

create table if not exists boletos
(
	id_funcion int not null,
    id_as int not null,
	CONSTRAINT fk_funcion FOREIGN KEY (id_funcion)
    REFERENCES funciones(id_funcion)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_as FOREIGN KEY (id_as)
    REFERENCES asientos(id_as)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)engine= INNODB;

