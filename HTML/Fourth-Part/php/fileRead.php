<?php
    $filename = "newfile.txt";
    $file = fopen($filename, "r");

    if ($file == false) {
        echo ("Error in opening file");
        exit();
    }
    while (!feof($file)) {
        echo fgets($file) . "<br />";
    }
    fclose($file);
?>
