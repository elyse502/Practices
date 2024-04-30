/**
 * Objective: Understand the difference between Factory Functions and Constructor Functions in JavaScript(ES6 - Both used to create objects)
 * - Factory Functions: A function that returns an object 
 * - Constructor Functions: A function that returns an object
 * - The difference is how they are called
 * - Factory Functions: camelCase
 * - Constructor Functions: PascalCase
 * - Constructor Functions: use the 'new' keyword
 * - Factory Functions: do not use the 'new' keyword
 * - Constructor Functions: use 'this' to set properties
 * - Factory Functions: do not use 'this' to set properties
*/


// Factory Function
function createCircle(radius) {
    return {
        radius,
        draw: function() {
            console.log('draw');
        }
    };
}
const circle = createCircle(1);

// Constructor Function
function Circle(radius) {
    console.log('this', this); // this refers to the object that is executing the function
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}
const another = new Circle(1); // new creates an empty object, then it sets this to point to that object, then it returns the object from the function
