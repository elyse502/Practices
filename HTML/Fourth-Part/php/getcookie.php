<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Cookies - Accessing Cookies with PHP</title>
</head>
<body>
    <?php
        if (isset($_COOKIE["name"])) {
            echo "<h1>Welcome " . $_COOKIE["name"] . "</h1><br />";
        } else {
            echo "name not set" . "<br />";
        }

        if (isset($_COOKIE["age"])) {
            echo "<h1>Your age is " . $_COOKIE["age"] . "</h1><br />";
        } else {
            echo "age not set" . "<br />";
        }
    ?>
</body>
</html>
