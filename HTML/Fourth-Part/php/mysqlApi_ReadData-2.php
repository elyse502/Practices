<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySqli API - Read Data</title>
</head>
<body>
    <?php
        $servername = "localhost";
        $username = "root";
        $password = "";

        // Creaye connection
        $conn = new mysqli($servername, $username, $password, "test_db");

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        echo "Connected successfully <br />";
        $sql = "SELECT * FROM employee";
        $result = $conn->query($sql);

        $num_result=$result->num_rows;
        $num_fields=$result->field_count;
        echo "<table border='1'>";
        echo "<tr>";
        for ($i=0; $i<$num_fields; $i++) {
            echo "<td>" . $result->fetch_field()->name . "</td>";
        }
        for ($i=0; $i<$num_result; $i++) {
            $row=$result->fetch_row();
            echo "<tr>";
            for ($j=0; $j<$num_fields; $j++) {
                echo "<td>" . $row[$j] . "</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    ?>
</body>
</html>
