<?php

$nombre = $_POST['name'];
$email = $_POST['email'];
$apellido = $_POST['lastname'];
$tel = $_POST['tel'];
$consulta = $_POST['consulta'];

$mensaje = "Este mensaje fue enviado por: $nombre \n";
$mensaje = "Este mensaje fue enviado por: $apellido \n";
$mensaje .= "Enviado desde: $email \n";
$mensaje .= "Telefono: $tel \n";
$mensaje .= "Mensaje: $consulta \n";

$para = "adgaribaldi@gmail.com";
$asunto = "Email enviado desde la web";

mail($para, $asunto, $mensaje);

?>