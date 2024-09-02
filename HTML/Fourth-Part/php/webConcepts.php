<!DOCTYPE html>
<html>
    <body>
        <p><b>Client side and server side script</b></p>
        <script type="text/javascript">
            document.write("Client's date :"+Date()+"<br/>");
        </script>
        <?php
            date_default_timezone_set("Africa/Kigali");
            echo "Server's date is " . date("Y-m-d");
            echo "The time is " . date("h:i:sa");
        ?>
    </body>
</html>
