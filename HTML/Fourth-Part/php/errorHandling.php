<!-- Die Error Handling -->
<?php
    if(!file_exists("test.txt")) {
        die("File not found");
    } else {
        $file = fopen("test.txt", "r");
        print "Opened file successfully";
    }
    fclose($file);
?>
