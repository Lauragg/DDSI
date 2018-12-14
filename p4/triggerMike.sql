USE ddsi;

delimiter |

DROP TRIGGER IF EXISTS checkUniversoNombre |
CREATE TRIGGER checkUniversoNombre BEFORE INSERT ON Universo
  FOR EACH ROW
  BEGIN
    DECLARE msg varchar(124);
    IF EXISTS (SELECT * FROM Universo as uni WHERE uni.nombre = NEW.nombre) THEN
      SET msg = concat('Error: El nombre de universo "', cast(NEW.nombre as char));
      SET msg = concat(msg, '", ya existe.');
      SIGNAL SQLSTATE '45000' SET message_text = msg;
    END IF;
  END;
|

delimiter ;
