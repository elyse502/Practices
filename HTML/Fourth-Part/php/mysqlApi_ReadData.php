<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySQL API - Read Data</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <?php
        $dbhost = 'localhost';
        $dbuser = 'root';
        $dbpass = '';
        $dbname = 'test_db';

        // Connect to the database using the MySQLi extension
        $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
        if ($conn->connect_error) {
            die('Could not connect: ' . $conn->connect_error);
        }
        echo 'Connected successfully <br />';

        // Query the database to fetch the employee data
        $sql = "SELECT * FROM employee";
        $result = $conn->query($sql);

        // Display the employee data in an HTML table
        if ($result->num_rows > 0) {
            echo "<table>
                    <tr>
                        <th>Employee ID</th>
                        <th>Employee Name</th>
                        <th>Employee Address</th>
                        <th>Employee Salary</th>
                    </tr>";
            while($row = $result->fetch_assoc()) {
                echo "<tr>
                        <td>" . $row["emp_id"]. "</td>
                        <td>" . $row["emp_name"]. "</td>
                        <td>" . $row["emp_address"]. "</td>
                        <td>" . $row["emp_salary"]. "</td>
                    </tr>";
            }
            echo "</table>";
        } else {
            echo "No employees found.";
        }

        // Close the connection
        $conn->close();
    ?>
</body>
</html>
