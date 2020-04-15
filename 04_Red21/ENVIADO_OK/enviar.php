<?php

//Seleccionando los campos de texto a enviar

$nombre = $_POST["nombre"];
$email = $_POST["email"];
$seleccion = $_POST["seleccion"];
$texto = $_POST["mensaje"];

//Datos para el correo

$destinatario = "consultas@red21.com";
$asunto = "Contacto Nuevo desde Web";

$carta = "De: $nombre \n ";
$carta .= "Su Correo Es: $email \n"; 
$carta .= "Su Seleccion fue: $telefono \n";
$carta .= "Su Mensaje es: $texto.";

$remitente="From: consultas@red21.com";

// Enviando Mensaje

mail($destinatario, $asunto, $carta,$remitente);
// header(_"Location:http://www.desdecualquierlugar.com/index.html"_)
header("Location:index.php?i=ok");
// SI EL FORMULARIO SE ENVIO CORRECTAMENTE, PONEME EN LA URL DESPUES DEL INDEX.PHP UN SIGNO DE PREGUNTA, UNA LETRA I, Y UN IGUAL OK
?>