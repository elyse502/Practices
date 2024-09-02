<?php
    echo "5 <=> 10/2 = " . (5 <=> 10/2) . "<br />";
    echo "5 <=> 10/2.1 = " . (5 <=> 10/2.1) . "<br />";
    echo "3.142 <=> 22/7 = " . (3.142 <=> 22/7) . "<br />";
    echo "substr('Hello World', 0, 5) = ";
    echo (substr('Hello World', 0, 5) <=> "Hello") . "<br />";
?>
