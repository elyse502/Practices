<?php
    function exception_handler($exception) {
        echo "Uncaught exception: " . $exception->getMessage() . "\n";
    }

    set_exception_handler('exception_handler');

    print "Enter first number: ";
    fscanf(STDIN, "%d", $x);
    echo "Enter second number: ";
    fscanf(STDIN, "%d", $y);
    
    if ($y == 0) {
        throw new Exception("Division by zero");
    }
    $z = $x / $y;
    echo "Result = $z\n";
?>
