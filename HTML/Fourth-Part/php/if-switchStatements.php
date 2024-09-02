<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Decision Making</title>
</head>
<body>
    <?php
        $a=rand(1,100);
        echo "Random number is $a <br/>";
        if ($a<25)
            echo "The number is less than 25<br/>";
        elseif ($a<50)
            echo "The number is between 25-50<br/>";
        else
            echo "The number is greater than or equal to 50<br/>";
        echo "<br/><br/>";


        // Switch Statement
        $x=rand(1,10);
        $y=rand(1,10);
        $z=rand(1,4);
        echo "Numbers: $x, $y operation code: $z <br/>";
        switch ($z) {
            case 1: $r=$x+$y; break;
            case 2: $r=$x-$y; break;
            case 3: $r=$x*$y; break;
            case 4: $r=$x/$y; break;
            default: $r=0;
        }
        echo "Result: $r";
    ?>
</body>
</html>
