<?php
include 'includes/funciones.php';
require 'includes/conexion.php';

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agendar</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>
<body>
    <div class="agendar">

        <h1>Agendar Contacto</h1>
    
        <form action="" method="post">

            <label for="name">Nombre: </label>
            <input class="agendar-datos" type="text" name="name" id="name" required>

            <label for="tel">Telefono: </label>
            <input class="agendar-datos" type="text" name="tel" id="tel" required>

            <label for="correo">Correo: </label>
            <input class="agendar-datos" type="email" name="correo" id="correo" required>

            <button class="agendar-boton" type="submit">Guardar</button>
            <a href="agenda.php">Ver Agenda</a>

        </form>
    </div>

    <?php
    // Verificar si se envió el formulario
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["name"]) && isset($_POST["tel"]) && isset($_POST["correo"])) {
        $nombre = htmlspecialchars($_POST["name"]);
        $tel = htmlspecialchars($_POST["tel"]);
        $correo = htmlspecialchars($_POST["correo"]);
    
        // Validar el número de teléfono
        if (validarTelefono($tel)) {
            // Preparar la consulta SQL para insertar el contacto
            $stmt = $conn->prepare("INSERT INTO contactos (nombre, telefono, correo) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $nombre, $tel, $correo);
    
            // Ejecutar la consulta
            if ($stmt->execute()) {
                //echo "Contacto guardado exitosamente.";
            } else {
                echo "Error al guardar el contacto: " . $stmt->error;
            }
    
            // Cerrar la declaración
            $stmt->close();
        } else {
            echo "El número de teléfono no es válido. Debe comenzar con '6' y tener 8 caracteres.";
        }


    }
    
    // Cerrar la conexión
    $conn->close();
?>

</body>
</html>