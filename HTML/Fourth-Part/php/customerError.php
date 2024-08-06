<?php
    error_reporting(E_ERROR);
    function handleError($errno, $errstr) {
        echo "Error No: [$errno] $errstr "; echo "\n";
        echo "Terminating PHP Script"; die();
    }
    set_error_handler("handleError");
    $f=fopen("notpresent.txt", "r");
    echo "File opened successfully";
    fclose($f);
?>
