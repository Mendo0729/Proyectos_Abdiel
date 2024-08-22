<?php
function validarTelefono($telefono) {
    // El patrón de expresión regular para validar el número de teléfono
    $patron = '/^6\d{7}$/';

    // Verifica si el número de teléfono cumple con el patrón
    if (preg_match($patron, $telefono)) {
        return true;  // El número es válido
    } else {
        return false; // El número no es válido
    }
}

?>