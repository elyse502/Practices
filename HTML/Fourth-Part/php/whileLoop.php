<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP While Loop</title>
</head>
<body>
    <?php
        // first example
        $i = 0;
        while ($i < 10) {
            $i++;
            echo "Number: $i <br/>";
        }
        echo "<br/><br/>";

        // second example
        $x=0;
        while($x!=5){
            $x=rand(1,10);
            echo "Random number: $x <br/>";
        }
    ?>
</body>
</html>