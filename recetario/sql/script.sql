CREATE TABLE recetas(
    id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    descripcion TEXT
);

INSERT INTO recetas(nombre, categoria, descripcion)
VALUES
    ('Pizza', 'salado', 'Masa horneada con queso, jitomate y jamon.'),
    ('Pastel de chocolate', 'dulce', 'Pastel esponjoso cubierto con ganache de chocolate.'),
    ('Costillas agridulces', 'agridulce', 'Costillas de cerdo banadas en salsa agridulce.'),
    ('Alitas picantes', 'picoso', 'Alitas de pollo banadas en salsa habanero.'),
    ('Espagueti al pesto', 'pastas', 'Pasta larga con salsa pesto de albahaca.'),
    ('Mayonesa casera', 'aderezos', 'Aderezo base hecho con huevo, aceite y limon.'),
    ('Filete a la juliana', 'cortes', 'Corte de res cocinado a la parrilla, tipo juliana.'),
    ('Ceviche de camaron', 'mariscos', 'Camaron marinado en limon con verduras picadas.');

SELECT * FROM recetas;
