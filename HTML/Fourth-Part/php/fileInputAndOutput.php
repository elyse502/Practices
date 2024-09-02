<?php
    $filename = "newfile.txt";
    $file = fopen($filename, "w");

    if ($file == false) {
        echo ("Error in opening new file");
        exit();
    }
    $str = <<<STR
        This is first line\n
        This is second line\n
        This is third line
    STR;

    fwrite($file, $str);
    fclose($file);
    echo ("File created successfully");
?>
