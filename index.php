<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Libro de Visitas</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Libro de Visitas</h1>
    
    <!-- Formulario para enviar el mensaje -->
    <form action="" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit">Enviar</button>
    </form>

    <h2>Mensajes Anteriores:</h2>
    <div class="messages">
        <?php
        // Verifica si se envió el formulario
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $name = htmlspecialchars($_POST["name"]);
            $message = htmlspecialchars($_POST["message"]);
            
            // Guarda el mensaje en el archivo
            $file = fopen("mensajes.txt", "a");
            fwrite($file, "$name: $message\n");
            fclose($file);
        }

        // Lee y muestra los mensajes guardados
        if (file_exists("mensajes.txt")) {
            $messages = file("mensajes.txt");
            foreach ($messages as $msg) {
                echo "<p>$msg</p>";
            }
        } else {
            echo "<p>No hay mensajes todavía.</p>";
        }
        ?>
    </div>
</body>
</html>
