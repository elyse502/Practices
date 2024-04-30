/**
 * Enumerating properties of an object
 * - for-in loop
 * - Object.keys()
 * - in operator
 * - Summary
 * 
 */


function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}

const circle = new Circle(10);


// Sometimes we need to iterate over or enumerate the properties in an object. we can do that using a for-in loop.
for (let key in circle) {
    console.log(key, circle[key]); // process of getting all the properties of an object
    if (typeof circle[key] !== 'function') { // only get the properties that are not functions
        console.log(key, circle[key]);
    }
}


// To get all the keys in an object, we can use the Object.keys() method.
const keys = Object.keys(circle); // In this approach, we get all the keys in an object and store them in an array(We can not separate 
console.log(keys);

// Sometimes you want to know if an object has a given property. We can do that using the in operator.
if ('radius' in circle) {
    console.log('Circle has a radius');
}
