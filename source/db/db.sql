CREATE DATABASE BarrioSeguro;

USE BarrioSeguro;

CREATE TABLE Usuario(
    U_User              VARCHAR(25)     NOT NULL,
    U_Password          VARCHAR(50)     NOT NULL,
    DNI                 VARCHAR(8)      NOT NULL UNIQUE,
    FullName            VARCHAR(80)     NOT NULL,
    NTelefono           VARCHAR(9)      NOT NULL UNIQUE,
    Direccion           VARCHAR(60)     NOT NULL,
    CorreoElectronico   VARCHAR(60)     NOT NULL UNIQUE,
    CONSTRAINT PK_Persona PRIMARY KEY(U_User)
);

CREATE TABLE ContactoEmergencia(
    P_User          VARCHAR(25),
    CE_Nombre       VARCHAR(20),
    CE_NTelefono    VARCHAR(9),
    CONSTRAINT FK_ContactoEmergencia_Usuario FOREIGN KEY(P_User) REFERENCES Usuario(U_User),
    CONSTRAINT PK_ContactoEmergencia PRIMARY KEY(P_User, CE_NTelefono)
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