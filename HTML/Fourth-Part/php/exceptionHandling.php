<?php
    print "Enter first number: ";
    fscanf(STDIN, "%d", $x);
    echo "Enter second number: ";
    fscanf(STDIN, "%d", $y);
    try {
        if ($y == 0) {
            throw new Exception("Division by zero");
        }
        $z = $x / $y;
        echo "Result = $z\n";
    } catch (Exception $e) {
        echo "Exception caught: " . $e->getMessage() . "\n";
    }
?>
