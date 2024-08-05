<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conditional Operators</title>
</head>
<body>
    <?php
        $a = 10;
        $b = 20;

        /* If condition is true the assign a to result otherwise b */
        $result = ($a > $b) ? $a : $b;
        echo "TEST1 : Value of result is $result <br>";

        /* If condition is true then assign a to result otherwise b */
        $result = ($a < $b) ? $a : $b;
        echo "TEST2 : Value of result is $result <br>";
    ?>
</body>
</html>
