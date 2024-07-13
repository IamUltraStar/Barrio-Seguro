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
    Autor           VARCHAR(25),
    CONSTRAINT PK_Reporte PRIMARY KEY(ID_Reporte),
    CONSTRAINT FK_Reporte_Usuario FOREIGN KEY(Autor) REFERENCES Usuario(U_User)
);

CREATE TABLE RememberLogin(
    R_Usuario VARCHAR(25),
    CONSTRAINT FK_RememberLogin_Usuario FOREIGN KEY(R_Usuario) REFERENCES Usuario(U_User)
);