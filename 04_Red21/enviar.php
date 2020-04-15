<?php

function ValidarDatos($campo){
	//Array con las posibles cabeceras a utilizar por un spammer
    $badHeads = array("Content-Type:",
                                 "MIME-Version:",
                                 "Content-Transfer-Encoding:",
                                 "Return-path:",
                                 "Subject:",
                                 "From:",
                                 "Envelope-to:",
                                 "To:",
                                 "bcc:",
                                 "cc:");

    //Comprobamos que entre los datos no se encuentre alguna de
    //las cadenas del array. Si se encuentra alguna cadena se
    //dirige a una página de Forbidden
    foreach($badHeads as $valor){ 
      if(strpos(strtolower($campo), strtolower($valor)) !== false){ 
        header("HTTP/1.0 403 Forbidden"); 
        exit; 
      }
    } 
 }

//Ejemplo de llamadas a la funcion
ValidarDatos($_POST['nombre']);
ValidarDatos($_POST['email']);
ValidarDatos($_POST['seleccion']);
ValidarDatos($_POST['mensaje']);

//Seleccionando los campos de texto a enviar

$nombre = $_POST["nombre"];
$email = $_POST["email"];
$seleccion = $_POST["seleccion"];
$texto = $_POST["mensaje"];

//Datos para el correo

$destinatario = "pablolupo84@gmail.com";
//$destinatario = "consultas@red21.com";
$asunto = "Contacto Nuevo desde Web";

$carta = "De: $nombre \n ";
$carta .= "Su Correo Es: $email \n"; 
$carta .= "Su Seleccion fue: $seleccion \n";
$carta .= "Su Mensaje es: $texto.";

$remitente="From: consultas@red21.com";

// Enviando Mensaje

mail($destinatario, $asunto, $carta,$remitente);
//header(_"Location:http://www.desdecualquierlugar.com/index.html"_)
header("Location:index.php?i=ok");
// SI EL FORMULARIO SE ENVIO CORRECTAMENTE, PONEME EN LA URL DESPUES DEL INDEX.PHP UN SIGNO DE PREGUNTA, UNA LETRA I, Y UN IGUAL OK
?>