<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Arthmetic Operators</title>
</head>
<body>
    <?php
        $a = 42;
        $b = 20;

        $c = $a + $b;
        echo "Addition Operation Result: $c <br>";

        $c = $a - $b;
        echo "Subtraction Operation Result: $c <br>";

        $c = $a * $b;
        echo "Multiplication Operation Result: $c <br>";

        $c = $a / $b;
        echo "Division Operation Result: $c <br>";

        $c = $a % $b;
        echo "Modulo Operation Result: $c <br>";

        $c = $a ** $b;
        echo "Exponentiation Operation Result: $c <br>";

        $c = $a++;
        echo "Increment Operation Result: $c <br>";

        $c = $a--;
        echo "Decrement Operation Result: $c <br>";
    ?>
</body>
</html>
