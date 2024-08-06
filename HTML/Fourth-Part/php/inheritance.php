<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Inheritance</title>
</head>
<body>
    <?php
        class student {
            protected $name, $age, $marks;
            public function __construct() {
                $n=func_num_args();
                if ($n==3) {
                    $this->name=(func_get_arg(0));
                    $this->age=intval(func_get_arg(1));
                    $this->marks=intval(func_get_arg(2));
                }
            }

            public function getDetails() {
                echo "name: $this->name, age: $this->age, marks: $this->marks <br/>";
            }
        }

        class engg extends student {
            private $branch;
            public function __construct(){
                $n=func_num_args();
                if ($n==4) {
                    parent::__construct(func_get_arg(0), func_get_arg(1), func_get_arg(2));
                    $this->branch=func_get_arg(3);
                }
            }

            public function getDetails() {
                parent::getDetails();
                echo "branch = $this->branch <br/>";
            }
        }


        $s1=new engg("John Smith", 20, 80, "IT");
        $s1->getDetails();
    ?>
</body>
</html>
