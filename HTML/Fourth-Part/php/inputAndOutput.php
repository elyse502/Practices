<?php
print "Enter length: ";
fscanf(STDIN, "%d", $a);
echo "Enter breadth: ";
fscanf(STDIN, "%d", $b);
$c = $a * $b;
fprintf(STDOUT, "Area of rectangle = %d", $c);
echo "\n";
?>
