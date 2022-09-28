CREATE TABLE users (
    id SERIAl PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE guia_remision (
    id_guia PRIMARY KEY NOT NULL,
    numero INTEGER NOT NULL,
    punto_partida VARCHAR(255) NOT NULL,
    punto_llegada VARCHAR(255) NOT NULL,
    destinatario VARCHAR(255) NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    cantidad VARCHAR (255) NOT NULL,
    fecha_traslado TIMESTAMP NOt NULL ,
    id_trasportista foreign key,
)

CREATE TABLE camion (
    id_camion PRIMARY KEY NOT NULL,
    placa VARCHAR(10) NOT NULL,
    marca varchar (30) NOT NULL,
    tara FLOAT NOT NULL,
    peso_neto FLOAT NOT NULL
)

CREATE TABLE conductor (
    id_conductor PRIMARY KEY NOT NULL,
    nombres VARCHAR (255) NOT NULL,
    apellidos VARCHAR (255) NOT NULL,
    licencia VARCHAR (255) NOT NULL,
    dni INTEGER NOT NULL
)

/*
MEjorar los tipos de datos
ahorrar espacio de memorioa en la BD

- Trasnporte: conductor y camion
*/