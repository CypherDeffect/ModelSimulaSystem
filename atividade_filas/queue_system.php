<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Filas</title>
</head>
<body>

    <form action="" method="POST">
        <label>Informe a quantidade clientes:</label>
        <input enctype="multipart/form-data" name="clientes">

        <br>

        <label>Quanto tempo levou até outro cliente chegar:</label>
        <input enctype="multipart/form-data" name="intervalo" >

        <br>

        <label>Quanto tempo durou o atendimento:</label>
        <input enctype="multipart/form-data" name="atendimento" >
        <br>
        <input type="submit" value="Enviar">

    </form>

    <?php
        date_default_timezone_set('America/Sao_Paulo');
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $cliente = $_POST['clientes'];
            $intervalo = $_POST['intervalo'];
            $atendimento = $_POST['atendimento'];

            // validação, excluir depois
            echo "Clientes: $cliente";
        }

    /*
        if (filter_var($idade, FILTER_VALIDATE_INT, ["options" => ["min_range" => 0]]) === false) {
            echo "Por favor, insira um número inteiro válido para a idade.";
        } else {
            // Processa o valor válido
            echo "Idade recebida: " . htmlspecialchars($idade);
        }
        */
    ?>



<?php 
    //$qtaClient = echo "Informe a quantidade de clientes";
?>
</body>
</html>

