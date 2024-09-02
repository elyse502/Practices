<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Anonymous Class</title>
</head>
<body>
    <?php
        $obj = new class(10) {
            private $x;

            function __construct($x) {
                $this->x = $x;
            }

            function add($y) {
                return $this->x + $y;
            }
            function sub($y) {
                return $this->x - $y;
            }
        };
        $result = $obj->add(20);
        echo "Addition = $result <br/>";
        $result = $obj->sub(5);
        echo "Subtraction = $result <br/>";
    ?>
</body>
</html>
