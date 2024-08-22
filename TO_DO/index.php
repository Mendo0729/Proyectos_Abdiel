<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TO-DO List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Lista de Tareas</h1>

    <!--Formulario -->
    <form action="" method="post">
    <label for="tarea">Tarea: </label>
    <input type="text" name="tarea" id="tarea" required>

    <label for="descrip">Descripción: </label>
    <textarea name="descrip" id="descrip"></textarea>

    <button type="submit">Guardar</button>
</form>

<h2>Tareas por hacer</h2>
<div class="tarea-por-hacer">
    <?php
    // Verificar si se envió el formulario para agregar tarea
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["tarea"]) && isset($_POST["descrip"])) {
        $tarea = htmlspecialchars($_POST["tarea"]);
        $descrip = htmlspecialchars($_POST["descrip"]);
        
        // Crear un identificador único para la tarea
        $id = uniqid();
    
        // Crear el archivo txt y agregar la tarea con identificador
        $archivo = fopen("tareas.txt", "a");
        fwrite($archivo, "$id|$tarea|$descrip\n");
        fclose($archivo);
    }

    // Verificar si se hizo clic en el botón de completado
    if (isset($_POST["eliminar_id"])) {
        $id_a_eliminar = htmlspecialchars($_POST["eliminar_id"]);

        // Leer todas las tareas
        $tareas = file("tareas.txt");
        
        // Filtrar las tareas para eliminar la seleccionada
        $tareas_nuevas = array_filter($tareas, function($linea) use ($id_a_eliminar) {
            return strpos($linea, "$id_a_eliminar|") === false;
        });

        // Reescribir el archivo sin la tarea eliminada
        file_put_contents("tareas.txt", implode("", $tareas_nuevas));
    }

    // Leer y mostrar las tareas guardadas
    if (file_exists("Agenda.txt")) {
        $mostrar = file("Agenda.txt");
        foreach ($mostrar as $task) {
            // Dividir la línea en partes
            $partes = explode("|", trim($task));
            
            // Verificar si la línea tiene el formato esperado
            if (count($partes) === 3) {
                list($id, $tarea, $descrip) = $partes;
                echo "<p>$tarea: $descrip</p>";
                echo '<form action="" method="post" style="display:inline;">
                          <input type="hidden" name="eliminar_id" value="' . htmlspecialchars($id) . '">
                          <button type="submit">Completado</button>
                      </form>';
            } else {
                echo "<p>Formato de tarea inválido</p>";
            }
        }
    }else{
        echo "<p>No hay tarea Todavia</p>";
    }
    ?>
</div>


</body>
</html>