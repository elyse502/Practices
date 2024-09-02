<?php
    /* if (isset($_POST['submit'])) {
        echo "Welcome ". $_POST['name']. "<br />";
        echo "You are ". $_POST['age']. " years old.";

        exit();
    } */

    if (isset($_REQUEST['submit'])) {
        echo "Welcome ". $_REQUEST['name']. "<br />";
        echo "You are ". $_REQUEST['age']. " years old.";

        exit();
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP GET And POST Method</title>
</head>
<body>
    <form action="<?php $_PHP_SELF ?>" method="POST">
        Name: <input type="text" name="name" /><br><br>
        Age: <input type="text" name="age" /><br><br>
        <input type="submit" name="submit" />
    </form>
</body>
</html>
