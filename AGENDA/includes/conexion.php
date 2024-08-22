<?php
// Datos de la base de datos
$host = "localhost";     // El servidor de MySQL (por lo general, "localhost")
$usuario = "root";       // Tu nombre de usuario de MySQL
$password = "";          // Tu contraseña de MySQL (por defecto es vacía si usas XAMPP o WAMP)
$dbname = "Contacto";  // El nombre de la base de datos a la que deseas conectarte

// Crear la conexión
$conn = new mysqli($host, $usuario, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Puedes eliminar el siguiente comentario si quieres ver un mensaje de conexión exitosa
// echo "Conexión exitosa";
?>
