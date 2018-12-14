USE ddsi;

DELIMITER |
DROP TRIGGER IF EXISTS ComprobarExistenciaUniversoINSERT |
CREATE TRIGGER ComprobarExistenciaUniversoINSERT BEFORE INSERT ON Personaje
  FOR EACH ROW
  BEGIN
    CALL ComprobarExistenciaUniverso(NEW.uni_id);
  END |
DELIMITER ;

DELIMITER |
DROP TRIGGER IF EXISTS ComprobarExistenciaUniversoUPDATE |
CREATE TRIGGER ComprobarExistenciaUniversoUPDATE BEFORE UPDATE ON Personaje
  FOR EACH ROW
  BEGIN
    CALL ComprobarExistenciaUniverso(NEW.uni_id);
  END |
DELIMITER ;

DELIMITER |
DROP PROCEDURE IF EXISTS ComprobarExistenciaUniverso |
CREATE PROCEDURE ComprobarExistenciaUniverso(IN nuevoNombre VARCHAR(32))
READS SQL DATA
  BEGIN
    DECLARE msg varchar(124);
    IF NOT EXISTS (SELECT * FROM Universo AS uni WHERE uni.nombre = nuevoNombre) THEN
      SET msg = concat('Error: El nombre de universo "', cast(nuevoNombre as char));
      SET msg = concat(msg, '", no existe.');
      SIGNAL SQLSTATE '45000' SET message_text = msg;
    END IF;
  END |
DELIMITER ;
