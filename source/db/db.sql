CREATE DATABASE BarrioSeguro;

USE BarrioSeguro;

CREATE TABLE Usuario(
    DNI                 VARCHAR(8)      NOT NULL,
    PNombre             VARCHAR(20)     NOT NULL,
    SNombre             VARCHAR(20),
    ApellidoP           VARCHAR(20)     NOT NULL,
    ApellidoM           VARCHAR(20)     NOT NULL,
    NTelefono           VARCHAR(9)      NOT NULL UNIQUE,
    Direccion           VARCHAR(60)     NOT NULL,
    CorreoElectronico   VARCHAR(60)     NOT NULL UNIQUE,
    U_User              VARCHAR(25)     NOT NULL UNIQUE,
    U_Password          VARCHAR(50)     NOT NULL,
    CONSTRAINT PK_Persona PRIMARY KEY(DNI)
);

CREATE TABLE ContactoEmergencia(
    U_User          VARCHAR(8),
    CE_Nombre       VARCHAR(20),
    CE_NTelefono    VARCHAR(9),
    CONSTRAINT FK_ContactoEmergencia_Usuario FOREIGN KEY(U_User) REFERENCES Usuario(DNI),
    CONSTRAINT PK_ContactoEmergencia PRIMARY KEY(U_User, CE_NTelefono)
);

CREATE TABLE Reporte(
    ID_Reporte      INT,
    Tipo            VARCHAR(30)     NOT NULL,
    Descripcion     VARCHAR(200)    NOT NULL,
    Ubicacion       VARCHAR(120)    NOT NULL,
    FechaHora       DATETIME        NOT NULL,
    file_path       NVARCHAR(255),
    R_Contacto      VARCHAR(30),
    R_NTelefono     VARCHAR(9),
    CONSTRAINT PK_Reporte PRIMARY KEY(ID_Reporte)
);

CREATE TABLE RememberLogin(
    R_Usuario VARCHAR(25)
);

/* Persona:
- PNombre
- SNombre
- ApellidoP
- ApellidoM
- Correo Electronico
- Usuario
- Contraseña
- N° Teléfono
- Dirección
- DNI(PK)

Contactos:
- Persona(FK)
- Nombre de Contacto
- N° Teléfono
 */