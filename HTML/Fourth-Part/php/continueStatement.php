<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Continue Statement</title>
</head>
<body>
    <?php
        // continue example
        $y=0;
        while($y<10){
            $y++;
            $x=rand(1,10);
            if($x==5) continue;
            echo "Random number $y : value : $x <br>";
        }
    ?>
</body>
</html>
