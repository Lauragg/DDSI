USE ddsi;

DELIMITER |
DROP TRIGGER IF EXISTS dni_validoINSERT |
CREATE TRIGGER dni_validoINSERT BEFORE INSERT ON Jugador
  FOR EACH ROW
  BEGIN
    CALL dni_valido(NEW.dni);
  END |
DELIMITER ;

DELIMITER |
DROP TRIGGER IF EXISTS dni_validoUPDATE |
CREATE TRIGGER dni_validoUPDATE BEFORE UPDATE ON Jugador
  FOR EACH ROW
  BEGIN
    CALL dni_valido(NEW.dni);
  END |
DELIMITER ;

DELIMITER |
DROP PROCEDURE IF EXISTS dni_valido |
CREATE PROCEDURE dni_valido(IN nuevoDNI VARCHAR(9))
READS SQL DATA
  BEGIN
    DECLARE msg varchar(124);
    IF EXISTS (SELECT * FROM Jugador as j WHERE j.dni = nuevoDNI) THEN
      SET msg = concat('Error: El DNI "', cast(nuevoDNI as char));
      SET msg = concat(msg, '", ya existe en la base de datos.');
      SIGNAL SQLSTATE '45000' SET message_text = msg;
    END IF;
  END |
DELIMITER ;
