use wtf_eat_db;

-- CREAR PROCEDIMIENTO ALMACENADO PARA INSERTAR UN CAMPO EN LA TABLA COMPANIAS
use wtf_eat_db;
DROP PROCEDURE IF EXISTS SP_CREAR_NUEVA_COMPANIAS;

-- DECLARE DELIMITER $$;
-- NOMBRE DEL PROCEDIMIENTO
CREATE PROCEDURE SP_CREAR_NUEVA_COMPANIAS(  
-- PARAMETROS DE ENTRADA P_RAZONSOCIAL
		IN P_RAZONSOCIAL VARCHAR(100), 
    -- PARAMETROS DE ENTRADA P_NOMBRE_MARCA
        IN P_NOMBREMARCA VARCHAR(50), 
        -- VRESULT COMO PARAMETRO DE SALIDA
        OUT VRESULT INT 
        )

BEGIN -- INICIA E CUERPO DEL PROCEDIMIENTO
	
    DECLARE _ROLLBACK bool DEFAULT 0; -- DECLARA VARIABLE PARA MANEJAR EL ESTADO DE LOS ERRORES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET _ROLLBACK = 1; -- ESTABLECE 1 SI HAY UN ERROR EN LA TRANSACCION
    
    START TRANSACTION; -- CUERPO DE LA TRANSACCION
  		INSERT INTO COMPANIAS(RAZON_SOCIAL, NOMBRE_MARCA)
          VALUES(P_RAZONSOCIAL, P_NOMBREMARCA);
          SET VRESULT = 1;
    IF _ROLLBACK THEN
		ROLLBACK;
        SET VRESULT = -1;		
    ELSE
		COMMIT;
	END IF;    
END
-- DELIMITER ;


