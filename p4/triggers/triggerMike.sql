USE ddsi;

DELIMITER |
DROP TRIGGER IF EXISTS checkUniversoNombreINSERT |
CREATE TRIGGER checkUniversoNombreINSERT BEFORE INSERT ON Universo
  FOR EACH ROW
  BEGIN
    CALL checkUniversoNombre(NEW.nombre);
  END |
DELIMITER ;

DELIMITER |
DROP TRIGGER IF EXISTS checkUniversoNombreUPDATE |
CREATE TRIGGER checkUniversoNombreUPDATE BEFORE UPDATE ON Universo
  FOR EACH ROW
  BEGIN
    CALL checkUniversoNombre(NEW.nombre);
  END |
DELIMITER ;

DELIMITER |
DROP PROCEDURE IF EXISTS checkUniversoNombre |
CREATE PROCEDURE checkUniversoNombre(IN nuevoNombre VARCHAR(32))
READS SQL DATA
  BEGIN
    DECLARE msg varchar(124);
    IF EXISTS (SELECT * FROM Universo as uni WHERE uni.nombre = nuevoNombre) THEN
      SET msg = concat('Error: El nombre de universo "', cast(nuevoNombre as char));
      SET msg = concat(msg, '", ya existe.');
      SIGNAL SQLSTATE '45000' SET message_text = msg;
    END IF;
  END |
DELIMITER ;
