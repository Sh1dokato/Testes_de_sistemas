<?php
//Definir os dados de login (futuramente será via BD)
$usuario_correto = "admin";
$senha_correta = "123456";

// dados do formulário
$usuario = $_POST['username'] ?? '';
$senha = $_POST['password'] ?? '';

// Verificar se os dados estão corretos
if ($usuario === $usuario_correto && $senha === $senha_correta) {
    header("location: index.html");
    exit;
}else{
    //Redireciona de volta com erro
    header("location: login.html?erro=1");
    exit;
}
?>