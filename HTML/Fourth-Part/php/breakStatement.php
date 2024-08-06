<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Break Statement</title>
</head>
<body>
    <?php
        // break example
        $y=0;
        while($y<10){
            $y++;
            $x=rand(1,10);
            echo $x . "<br>";
            if($x==5) break;
        }
    ?>
</body>
</html>
