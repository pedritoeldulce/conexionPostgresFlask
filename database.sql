CREATE TABLE users (
    id SERIAl PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE guia_remision (
    id_guia SERIAL PRIMARY KEY NOT NULL,
    numero VARCHAR (6) NOT NULL,
    punto_partida VARCHAR(255) NOT NULL,
    punto_llegada VARCHAR(255) NOT NULL,
    destinatario VARCHAR(255) NOT NULL,
    descripcion VARCHAR (255) NOT NULL,
    cantidad VARCHAR (255) NOT NULL,
    fecha_traslado DATE NOt NULL ,
    id_trasportista foreign key,
)

CREATE TABLE camion (
    id SERIAL PRIMARY KEY NOT NULL,
    placa VARCHAR(7) NOT NULL,
    marca VARCHAR (30) NOT NULL,
    p_bruto DECIMAL(6,3) NOT NULL,
    p_neto DECIMAL (6,3) NOT NULL,
    carga_util DECIMAL (6,3) NOT NULL
)

CREATE TABLE conductor (
    id SERIAL PRIMARY KEY NOT NULL,
    nombres VARCHAR (255) NOT NULL,
    apellidos VARCHAR (255) NOT NULL,
    licencia VARCHAR (10) NOT NULL,
    clase CHAR(1) NOT NULL,
    categoria VARCHAR(10) NOT NULL,
    telf VARCHAR (10) NOT NULL
)

/*
MEjorar los tipos de datos
ahorrar espacio de memorioa en la BD

- Trasnporte: conductor y camion
*/