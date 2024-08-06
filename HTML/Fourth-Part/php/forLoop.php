<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP For Loop</title>
</head>
<body>
    <?php
        // first example
        for ($x=1; $x<=10; $x++) {
            echo $x." ";
        }
        echo "<br/><br/>";


        // second example
        for ($x=0; $x!=5;) {
            $x=rand(1,10);
            echo $x." ";
        }
        echo "<br/><br/>";


        // third example
        $arr=array(10, 20, 30, 40, 50);
        for ($x=0; $x<=4; $x++) {
            print $arr[$x]." ";
        }
    ?>
</body>
</html>
