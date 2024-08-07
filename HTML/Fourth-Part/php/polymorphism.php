<?php
    /* interface button {
        public function clicked();
    }

    class MyButton implements button {
        public function clicked() {
            echo "MyButton clicked <br />";
        }
    }

    class YourButton implements button {
        public function clicked() {
            echo "YourButton clicked <br />";
        }
    }


    $b1 = new MyButton();
    $b1->clicked();

    $b2 = new YourButton();
    $b2->clicked(); */


    abstract class shape {
        // Our abstract method only needs to declare function
        abstract protected function area();
    }

    class rectangle extends shape {
        var $l, $b;
        public function __construct($x, $y) {
            $this->l = $x;
            $this->b = $y;
        }
        public function area() {  // implement abstract function
            $a = $this->l * $this->b;
            return $a;
        }
    }

    class circle extends shape {
        var $r;
        public function __construct($x) {
            $this->r = $x;
        }
        public function area() {  // implement abstract function
            $pi = 3.142;
            $a = pow($this->r, 2) * $pi;
            return $a;
        }
    }


    $r1 = new rectangle(10, 20);
    $area = $r1->area();
    echo "Area of rectangle = $area <br />";
    
    $c1 = new circle(10);
    $area = $c1->area();
    echo "Area of circle = $area <br />";
?>
