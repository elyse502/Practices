<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySqli API</title>
</head>
<body>
    <?php
        $servername = "localhost";
        $username = "root";
        $password = "";

        // Create connection
        $conn = new mysqli($servername, $username, $password);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        echo "Connected successfully <br />";
        $sql = 'CREATE DATABASE IF NOT EXISTS testdb';
        if ($conn->query($sql) === TRUE) {
            echo "Database created successfully <br />";
        } else {
            echo "Error creating database: " . $conn->error;
        }
        $conn->select_db("testdb");
        $sql = 'CREATE TABLE employee( '.
               'emp_id INT NOT NULL AUTO_INCREMENT, '.
               'emp_name VARCHAR(20) NOT NULL, '.
               'emp_address VARCHAR(20) NOT NULL, '.
               'emp_salary INT NOT NULL, '.
               'PRIMARY KEY ( emp_id ))';
        if ($conn->query($sql) === TRUE) {
            echo "Table created successfully <br />";
        } else {
            echo "Error creating table: " . $conn->error;
        }
        $sql = "INSERT INTO employee (emp_name, emp_address, emp_salary) VALUES ('John', 'London', 23)";
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        $conn->close();
    ?>
</body>
</html>
