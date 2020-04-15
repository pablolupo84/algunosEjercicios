<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DesdeCualquierLugar</title>
    <link rel="shortcut icon" href="/img/libro.png" type="image/png">
    <link href="https://fonts.googleapis.com/css?family=Arvo|Baloo+Da+2&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/normalize.css">
    <link rel="stylesheet" href="/css/style.css">
</head>

<body>

    <header>

        <div class="rellenoBlog">

            <nav class="navegacion">
                <a href="index.html">Inicio</a>
                <a href="libro.html">Libro</a>
                <a href="continuacion.html">Consejos</a>
                <a href="contacto.html">Contacto</a>
            </nav>

        </div>

        <div class="rellenoBlog">
            <div class="titulo">
                <img class="ajuste4" src="/img/ilustracion-edificio.png" alt="edificio+isla">
                <h1 class="">DESDE <span>CUALQUIER</span> LUGAR</h1>
            </div>
        </div>
    </header>
    <!--Fin del titulo y la barra de navegacion -->

    <main class="rellenoBlog">

        <div class="contactoOrden">

            <img class="ajuste3" src="/img/libro3partes.png" alt="">

            <div class="formulario">

                <form  action="enviar.php" method="post" enctype="multipart/form-data">

                    <label for="name">Nombre:</label><br>
                    <input required placeholder="Nombre . . ." class="textoA" type="text" name="nombre" max-size="30" minlength="3"><br><br>

                    <label for="mail">E-mail:</label><br>
                    <input required placeholder="ejemplo@ejemplo.com" class="textoA" type="email" name="email" id=""><br><br>

                    <label for="seleccion">Selección:</label><br>
                    <select name="seleccion" id="seleccion">
                        <option value="Seleccion 1">Lei el libro</option>
                        <option value="Seleccion 2">Quiero comprar el libro</option>
                        <option value="Seleccion 3">Otro motivo</option>
                    </select><br><br>

                    <label for="mensaje">Mensaje:</label><br>
                    <textarea class="msg" name="mensaje" placeholder="Escribe tu mensaje . . ." style="height: 150px;"></textarea><br><br>

                    <input type="submit">

                </form>
                
            </div>

        </div>

    </main>


    <footer>
        <p>DESDE <span>CUALQUIER</span> LUGAR - Todos los derechos reservados 2020</p>
        
    </footer>
    
</body>

</html>