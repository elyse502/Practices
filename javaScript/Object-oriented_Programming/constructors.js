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
function createCircle(radius) { // camelCase
    return { // object literal notation
        radius, // property
        draw: function() { // method
            console.log('draw'); // implementation
        }
    };
}
const circle = createCircle(1);

// Constructor Function
function Circle(radius) { // PascalCase
    console.log('this', this); // this refers to the object that is executing the function
    this.radius = radius; // property
    this.draw = function() { // method
        console.log('draw'); // implementation
    }
}
const another = new Circle(1); // new creates an empty object, then it sets this to point to that object, then it returns the object from the function
