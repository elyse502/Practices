<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Function Statements</title>
</head>
<body>
    <?php
        function swap(&$x, &$y) {
            $t=$x;
            $x=$y;
            $y=$t;
        }
        $a=10;$b=20;
        echo "Before swap: a=$a and b=$b<br>";
        swap($a,$b);
        echo "After swap: a=$a and b=$b<br>";
        echo "<br /><br />";


        // User defined function default arguments
        function percentage($p, $c, $m, $ttl=300) {
            echo "p=$p, c=$c, m=$m, ttl=$ttl<br>";
            $percent = ($p+$c+$m)*100/$ttl;
            echo "Percentage = $percent<br>";
        }
        percentage(50, 60, 70);
        percentage(25, 30, 35, 150);
        echo "<br />";

        function average() {
            $args = func_get_args();
            print_r($args);echo "<br>";
            $sum = 0;
            $count = func_num_args();
            for ($i=0; $i<func_num_args(); $i++) {
                $sum += $args[$i];
            }
            $avg=$sum/$count;
            // echo "Average = $avg";
            return $avg;
        }
        // average(10, 20, 30, 40, 50);
        $avg = average(10, 20, 30, 40, 50);
        echo "Average = $avg";
    ?>
</body>
</html>
