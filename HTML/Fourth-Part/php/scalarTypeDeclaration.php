<?php
    // declare(strict_types = 1);
    echo "<u>Scalar type declaraion</u><br />";
    function average(int $x, int $y): int {
        $value = ($x + $y) / 2;
        return $value;
    }
    
    $avg=average(10, '20');  // It doesn't matter whether the value is an integer or a string unless you use declare(strict_types = 1);
    echo "Average = $avg <br />";
?>
