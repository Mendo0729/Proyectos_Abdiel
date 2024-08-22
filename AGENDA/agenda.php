<?php
require 'includes/conexion.php';

// Aquí puedes realizar tus consultas SQL
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["eliminar_id"])) {
    $id_eliminar = $_POST["eliminar_id"];
    $sql_eliminar = "DELETE FROM contactos WHERE id = ?";
    $stmt = $conn->prepare($sql_eliminar);
    $stmt->bind_param("i", $id_eliminar);

    if ($stmt->execute()) {
        //echo "<p>Contacto eliminado correctamente.</p>";
    } else {
        //echo "<p>Error al eliminar el contacto.</p>";
    }

    $stmt->close();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Contactos</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>
<body>
    <div class="contact-list-container">
        <h2>Contactos Agendados</h2>
        <?php

    $sql = "SELECT id, nombre, telefono, correo FROM contactos";
    $resultado = $conn->query($sql);
    
    if ($resultado->num_rows > 0) {
        // Salida de los datos de cada fila
        while($fila = $resultado->fetch_assoc()) {
            echo "<p>Nombre: " . htmlspecialchars($fila["nombre"]) . "</p>";
            echo "<p>Teléfono: " . htmlspecialchars($fila["telefono"]) . "</p>";
            echo "<p>Correo: " . htmlspecialchars($fila["correo"]) . "</p>";
            echo '<form action="" method="post" style="display:inline;">
                      <input type="hidden" name="eliminar_id" value="' . htmlspecialchars($fila["id"]) . '">
                      <button type="submit">Eliminar</button>
                  </form>';
            echo "<hr>"; // Separador entre contactos
        }
    } else {
        echo "<p>No hay contactos guardados.</p>";
    }
    
    $conn->close();
        ?>
        <!-- Enlace para volver a la página anterior -->
        <a href="index.php">Volver a Agendar</a>
    </div>
</body>
</html>
