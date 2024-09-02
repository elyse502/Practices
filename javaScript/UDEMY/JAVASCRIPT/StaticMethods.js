class Calculator{
    add(a, b){
        return a + b;
    }
    static multiply(a, b){
        return a * b;
    }
}
const calculatorInstance = new Calculator();
console.log(calculatorInstance.add(5, 8));

class Circle{
    constructor(radius){
        this.radius = radius;
    }
    calculateArea(){
        return Math.PI * this.radius **2;
    }

    static createFromDiameter(diameter){
        const radius = diameter / 2;
        return new Circle(radius);
    }
}

const smallCircle = new Circle(5);
console.log(smallCircle.calculateArea());

const largeCircle = Circle.createFromDiameter(10);
console.log(largeCircle.calculateArea());