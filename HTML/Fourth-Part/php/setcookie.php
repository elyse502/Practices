<?php
    if (isset($_POST['submit'])) {
        $nm = $_POST['name'];
        $age = $_POST['age'];
        setcookie("name", $nm);
        setcookie("age", $age, time() + 3600, "/", "",    0);
        echo "<b>Cookies are set</b> <br>";
        echo "<a href='getcookie.php'><b>Click here to read cookies</b></a>";
    }
?>
