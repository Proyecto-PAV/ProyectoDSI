
--EJECUTAR EL COMANDO DE CREACI�N DE LA BASE DE DATOS PRIMERO (SOLO).
--PARA EJECUTAR SOLO ESTA LINEA SE LA DEBE PINTAR Y OPRIMIR EL BOT�N 


CREATE DATABASE MUSEO;

-- LUEGO DE EJECUTAR EL COMANDO DE CREACI�N COMENTAR LA LINEA

use MUSEO;

-- Crear tablas.

CREATE TABLE entradas 
(numero                       INT 
   CONSTRAINT entradas_numero_nn UNIQUE NOT NULL,
 fecha_venta                  DATE, 
 hora_venta                   TIME,
 monto                        FLOAT,
 id_tipo_entrada              INT,
 id_tipo_visita               INT,
 nombre_sede                  INT,
     CONSTRAINT entradas_numero_pk PRIMARY KEY (numero),
     CONSTRAINT entradas_id_te_tv_sede_uk UNIQUE(id_tipo_entrada, id_tipo_visita, nombre_sede))


CREATE TABLE tipoVisitas
(id_tipo_visita            INT
    CONSTRAINT TipoVisitas_id_tipo_visita_nn UNIQUE NOT NULL,
 nombre                    VARCHAR(255)
    CONSTRAINT TipoVisita_nombre_nn NOT NULL,
    CONSTRAINT TipoVisitas_id_nn PRIMARY KEY (id_tipo_visita))


CREATE TABLE TipoEntradas
(id_tipo_entrada            INT
    CONSTRAINT TipoEntradas_id_tipo_entrada_nn UNIQUE NOT NULL,
 nombre                    VARCHAR(50)
    CONSTRAINT TipoEntradas_nombre_nn NOT NULL,
    CONSTRAINT TipoEntradas_id_nn PRIMARY KEY (id_tipo_entrada))


CREATE TABLE tarifas
(id_tipo_entrada        INT
     CONSTRAINT tarifas_id_tipo_entrada_nn NOT NULL,
 id_tipo_visita         INT
    CONSTRAINT tarifas_id_tipo_visita_nn NOT NULL,
 nombre_sede            VARCHAR(50)
    CONSTRAINT tarifas_nombre_sede_nn NOT NULL,
 fecha_fin_vigencia     DATE,
 fecha_inico_vigencia   DATE,
 monto                  FLOAT,
 id_guia                INT,
    CONSTRAINT tarifas_tipent_tipven_sede_pk PRIMARY KEY (id_tipo_visita, id_tipo_entrada, nombre_sede),
    CONSTRAINT tarifas_id_guia_tv_te_uk UNIQUE (id_tipo_visita, id_tipo_entrada, nombre_sede, id_guia),
)


CREATE TABLE empleados
(dni            INT
    CONSTRAINT empleados_dni_nn NOT NULL,
 cuit           INT,
 nombre         VARCHAR(50),
 apellido       VARCHAR(50),
 sexo           VARCHAR(50),
 telefono       VARCHAR(25),
 codigo_validacion  INT,
 domicilio      VARCHAR(400),
 fecha_ingreso  DATE,
 fecha_nacimiento   DATE,
 mail           VARCHAR(100),
 nombre_sede    VARCHAR(50)
    CONSTRAINT empleados_nombre_sede_nn NOT NULL,
    CONSTRAINT empleados_dni_pk PRIMARY KEY (dni),
    CONSTRAINT empleados_sexo_ck
        CHECK(sexo IN ('MASCULINO', 'FEMENINO', 'OTRO')),
    CONSTRAINT empleados_dni_sede_codigo_uk UNIQUE (codigo_validacion,nombre_sede, cuit)
    )


CREATE TABLE sesiones 
(dni        INT
    CONSTRAINT sesiones_dni_nn NOT NULL,
 nombre_usuario VARCHAR(100)
     CONSTRAINT sesiones_nombre_usuario_nn NOT NULL,
 fecha_inico    DATE,
 fecha_fin      DATE,
 hora_incio     TIME,
 hora_fin       TIME,
    CONSTRAINT sesiones_dni_usu_pk PRIMARY KEY (dni, nombre_usuario),
    CONSTRAINT sesiones_dni_usu_uk UNIQUE (dni, nombre_usuario))


CREATE TABLE sedes 
(nombre     VARCHAR(50)
    CONSTRAINT sedes_nombre_nn UNIQUE NOT NULL,
 cant_maxima_visitnates     INT,
    CONSTRAINT sedes_nombre_pk PRIMARY KEY (nombre))


CREATE TABLE exposiciones
(nombre VARCHAR(150)
    CONSTRAINT exposiciones_nombre_nn UNIQUE NOT NULL,
 fehca_fin  DATE,
 fecha_fin_replanificada    DATE,
 fecha_inico    DATE,
 fecha_incio_replanificada  DATE,
 hora_apertura  TIME,
 hora_cierre    TIME,
 nombre_sede    VARCHAR(50)
    CONSTRAINT exposiciones_sede_nn UNIQUE NOT NULL,
 duracion_exposicion    TIME,
    CONSTRAINT exposiones_nombre_pk PRIMARY KEY (nombre)
)


CREATE TABLE detalleExposiciones
(nombre_exposicion VARCHAR(150)
    CONSTRAINT detalleExposiciones_expo_nn UNIQUE NOT NULL,
 nombre_obra    VARCHAR(150)
    CONSTRAINT detalleExposiciones_obra_nn UNIQUE NOT NULL,
 id_operaciones INT
    CONSTRAINT detalleExposiciones_operaciones_nn UNIQUE,
 lugar_asginado VARCHAR(200),
    CONSTRAINT detalleExposiones_expo_obra_pk PRIMARY KEY (nombre_exposicion, nombre_obra))


CREATE TABLE reservasVisitas
(numero_reserva INT
    CONSTRAINT reservasVisitas_numero_reserva_nn UNIQUE NOT NULL,
 fecha_creacion     DATE,
 fecha_hora_reserva DATETIME,
 fecha_real         DATE,
 hora_incio_real    TIME,
 hora_fin_real      TIME,
 cantidad_alumnos   INT,
 cantidad_alumnos_confirmada INT,
 nombre_sede        VARCHAR(50),
    CONSTRAINT reservasVisitas_nro_reserva_pk PRIMARY KEY (numero_reserva),
    CONSTRAINT reservaVisitas_sede_uk UNIQUE (nombre_sede))


CREATE TABLE guias
(dni INT
    CONSTRAINT guias_dni_nn UNIQUE NOT NULL,
nombre_sede VARCHAR(50)
    CONSTRAINT guias_sede_nn UNIQUE NOT NULL,
cant_maxima INT,
monto_adicional FLOAT,
    CONSTRAINT guias_dni_pk PRIMARY KEY (dni)
)


CREATE TABLE Reservas_x_Guias
(numero_reserva INT
    CONSTRAINT Reservas_x_Guias_nro_reserva_nn UNIQUE NOT NULL,
 dni INT
    CONSTRAINT Reservas_x_Guias_dni_nn UNIQUE NOT NULL,    
 nombre_sede    VARCHAR(50),
    CONSTRAINT Reservas_x_Guias_nro_dni_pk PRIMARY KEY(numero_reserva, dni) )


CREATE TABLE obras
(nombre_obra    VARCHAR(150)
    CONSTRAINT obras_nombre_nn NOT NULL,
 peso           FLOAT, 
 alto           FLOAT,
 ancho          FLOAT,
 descripcion    VARCHAR(400),
 duracion_extendida TIME,
 duracion_resumida  TIME,
 fecha_creacion     DATE,
 fecha_primer_ingreso   DATE,
 codigo_sensor      INT,
 empleado_ingreso   INT,
    CONSTRAINT obras_nombre_obra_pk PRIMARY KEY (nombre_obra),
    CONSTRAINT obras_nombre_sensor_empleado_uk UNIQUE (nombre_obra, codigo_sensor, empleado_ingreso)
)

CREATE TABLE cambiosEstados
(id_estado INT
    CONSTRAINT cambiosEstados_id_nn NOT NULL,
 nombre_ambito VARCHAR(100)
    CONSTRAINT cambiosEstados_nombre_nn NOT NULL,
 fecha_hora_incio DATETIME
     CONSTRAINT cambiosEstados_fhincio_nn NOT NULL,
 fecha_hora_fin DATETIME
    CONSTRAINT cambiosEstados_fhfin_nn NOT NULL,
    CONSTRAINT cambiosEstados_id_nom_inicio_fin_pk PRIMARY KEY (id_estado, nombre_ambito, fecha_hora_fin, fecha_hora_incio),
    CONSTRAINT cambiosEstados_est_ambito_uk UNIQUE (id_estado, nombre_ambito)
    --HARIA FALTA SABER LOS AMBITOS PARA HACER UN CONSTRAINT CHECK!!)
)

CREATE TABLE estados
(id_estado INT
    CONSTRAINT cambiosEstados_id_nn NOT NULL,
 nombre_ambito VARCHAR(100)
    CONSTRAINT cambiosEstados_ambito_nn NOT NULL,
 descripcion VARCHAR(400),
 estado_reserva VARCHAR(150),
 nombre_estado  VARCHAR(150),
    CONSTRAINT cambiosEstados_id_nom_pk PRIMARY KEY (id_estado, nombre_ambito),
    CONSTRAINT cambiosEstados_nombre_estado_uk UNIQUE (nombre_estado)
      --HARIA FALTA SABER LOS NOMBRES ESTADO PARA HACER UN CONSTRAINT CHECK!!)
      )


CREATE TABLE operaciones
(id_operaciones INT
    CONSTRAINT operaciones_id_nn UNIQUE NOT NULL,
 detalle    VARCHAR(400),
    CONSTRAINT operaciones_id_pk PRIMARY KEY (id_operaciones)
)

CREATE TABLE gestorVentaEntradas
(dni                    INT
    CONSTRAINT gestorVentaEntradas_dni_nn NOT NULL,
 nombre_usuario         VARCHAR(100)
    CONSTRAINT gestorVentaEntradas_nom_usu_nn NOT NULL,
 fecha_hora_actual      DATETIME
    CONSTRAINT gestorVentaEntradas_fh_actual_nn NOT NULL,
 nombre_sede            VARCHAR(50)
    CONSTRAINT gestorVentaEntradas_sede_actual_nn NOT NULL,
 monto_total_pagar      FLOAT,
 hay_guia               BIT,
 cant_entradas_emitir   INT,
 confirmar_venta        BIT,
    CONSTRAINT gestorVentaEntradas_dni_usu_fh_pk PRIMARY KEY (dni, nombre_usuario, fecha_hora_actual),
    -- EL DATATYPE 'BIT' REPRESENTA 0,1 O NULL
)


CREATE TABLE usuarios
(nombre_usuario     VARCHAR(100)
    CONSTRAINT usuarios_nombre_nn UNIQUE NOT NULL,
 caducidad          DATE
    CONSTRAINT usuarios_cad_nn NOT NULL,
 contraseña         VARCHAR(350)
    CONSTRAINT usuarios_conta_nn NOT NULL,
 usuario_log        BIT,
    CONSTRAINT usuarios_nombre_usu_pk PRIMARY KEY (nombre_usuario)
)