<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySQL API</title>
</head>
<body>
    <?php
        $dbhost = 'localhost';
        $dbuser = 'root';
        $dbpass = '';
        $dbname = 'test_db';

        // Connect to the database using the MySQLi extension
        $conn = new mysqli($dbhost, $dbuser, $dbpass);
        if ($conn->connect_error) {
            die('Could not connect: ' . $conn->connect_error);
        }
        echo 'Connected successfully <br />';

        // Create the database if it doesn't exist
        $sql = "CREATE DATABASE IF NOT EXISTS $dbname";
        if ($conn->query($sql) === TRUE) {
            echo "Database $dbname created successfully <br />";
        } else {
            echo "Error creating database: " . $conn->error;
        }

        // Select the database
        $conn->select_db($dbname);

        // Create the table
        $sql = 'CREATE TABLE IF NOT EXISTS employee(
            emp_id INT NOT NULL AUTO_INCREMENT,
            emp_name VARCHAR(20) NOT NULL,
            emp_address VARCHAR(20) NOT NULL,
            emp_salary INT NOT NULL,
            PRIMARY KEY (emp_id)
        )';
        if ($conn->query($sql) === TRUE) {
            echo "Table employee created successfully <br /><hr /><br />";
        } else {
            echo "Error creating table: " . $conn->error;
        }

        // Insert data into the table when the form is submitted
        if (isset($_POST['add'])) {
            $emp_name = $_POST['emp_name'];
            $emp_address = $_POST['emp_address'];
            $emp_salary = $_POST['emp_salary'];

            $sql = "INSERT INTO employee (emp_name, emp_address, emp_salary) VALUES('$emp_name', '$emp_address', $emp_salary)";
            if ($conn->query($sql) === TRUE) {
                echo "Entered data successfully <br /><hr /><br />";
            } else {
                echo "Error entering data: " . $conn->error;
            }
        }

        // Close the connection
        $conn->close();
    ?>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
        <table border="0">
            <tr>
                <td width="100">Employee Name</td>
                <td><input type="text" name="emp_name"></td>
            </tr>
            <tr>
                <td width="100">Employee Address</td>
                <td><input type="text" name="emp_address"></td>
            </tr>
            <tr>
                <td width="100">Employee Salary</td>
                <td><input type="text" name="emp_salary"></td>
            </tr>
            <tr>
                <td width="100"> </td>
                <td><input type="submit" name="add" value="Add Employee"></td>
            </tr>
        </table>
    </form>
</body>
</html>
