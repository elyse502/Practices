/**
 * Every object in JavaScript has a constructor property that references the function that was used to create that object.
 * - The constructor property is a reference to the function that was used to create an object
 * - The constructor property is available on all objects
 * - The constructor property is available on all objects created with a constructor function
 * - The constructor property is available on all objects created with a factory function
 * - The constructor property is available on all built-in objects
 * - The constructor property is available on all primitive values
 * - The constructor property is available on all functions
 * - The constructor property is available on all arrays
 * - The constructor property is available on all regular expressions
 * - The constructor property is available on all dates
 * - The constructor property is available on all numbers
 * - The constructor property is available on all strings
 * - The constructor property is available on all booleans
 * - The constructor property is available on all symbols
 * - The constructor property is available on all maps
 * - The constructor property is available on all sets
 */


new String(); // '', "", ``
new Boolean(); // true, false
new Number(); // 1, 2, 3, ...


// In JavaScript Functions are objects
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}

const Circle1 = new Function('radius', `
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
`); // new Function() is not recommended

const circle = new Circle1(1); // new Function() is not recommended

Circle.call({}, 1); // {} is the value of this
Circle.apply({}, [1]); // {} is the value of this

const another = new Circle(1);