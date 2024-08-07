<?php
    echo "<p>Coalesc operator in PHP</P>";
    $user = $_GET['user'] ?? 'not passed';
    echo "User name $user<br />";
    echo "<p>Ternary operator result</p>";
    $user = isset($_GET['user']) ? $_GET['user'] : 'not passed';
    print("User name ". $user ."<br />");
?>
