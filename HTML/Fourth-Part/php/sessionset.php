<?php
    if(isset($_POST['submit'])) {
        session_start();
        $_SESSION['user'] = $_POST['name'];
        echo "Session variable set <br />";
        echo "<a href='checksession.php'><b>Read session variables</b></a>";
        exit();
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Sessions</title>
</head>
<body>
    <form action="<?php $_PHP_SELF ?>" method="POST">
        Name: <input type="text" name="name" /><br /><br />
        Age: <input type="text" name="age" /><br /><br />
        <input type="submit" name="submit" /><br /><br />
    </form>
</body>
</html>
