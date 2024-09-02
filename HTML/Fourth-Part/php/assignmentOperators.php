<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Assignment Operators</title>
</head>
<body>
    <?php
        $a = 42;    /* Assignment operator */
        $b = 20;    /* Assignment operator */

        $c = $a + $b;   /* c value was 42 + 20 = 62 */
        echo "Addition Operation Result: $c <br>";

        $c += $a;   /* c value was 62 + 42 = 104 */
        echo "Add AND Assignment Operation Result: $c <br>";

        $c -= $a;   /* c value was 104 - 42 = 62 */
        echo "Subtract AND Assignment Operation Result: $c <br>";

        $c *= $a;   /* c value was 62 * 42 = 2604 */
        echo "Multiply AND Assignment Operation Result: $c <br>";

        $c /= $a;   /* c value was 2604 / 42 = 62 */
        echo "Division AND Assignment Operation Result: $c <br>";

        $c %= $a;   /* c value was 62 % 42 = 20 */
        echo "Modulus AND Assignment Operation Result: $c <br>";
        /* Final value of c will be 20 */
    ?>
</body>
</html>
