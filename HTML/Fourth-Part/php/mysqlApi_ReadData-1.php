<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySqli API - Read Data</title>
</head>
<body>
    <?php
        $con=mysqli_connect("localhost","root","","test_db");
        if (mysqli_connect_errno()) {
            echo "Failed to connect to MySQL: " . mysqli_connect_error();
            exit();
        } else {
            echo "Connection established successful <br />";
        }
        $sql = "SELECT * FROM employee";
        $result=mysqli_query($con,$sql);
        $rowcount=mysqli_num_rows($result);
        for ($i=0; $i<$rowcount; $i++) {
            $row = mysqli_fetch_row($result);
            echo "emp_id => " .$row[0] ."<br />";
            echo "emp_name => " .$row[1] ."<br />";
            echo "emp_address => " .$row[2] ."<br />";
            echo "emp_salary => " .$row[3] ."<br /><br />";
        }
        mysqli_free_result($result);
        mysqli_close($con);
    ?>
</body>
</html>
